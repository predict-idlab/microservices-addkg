from abc import ABC
from jinja2 import Environment, FileSystemLoader
import json
from kubernetes import client as K8sClient, config as K8sConfig
import logging
import random
from ruamel.yaml import YAML
import string
import time

from litmus import client


class Result:
    def __init__(self,
                 experiment_created_at: str,
                 experiment_started_at: str, experiment_finished_at: str,
                 fault_name, fault_started_at: str, fault_finished_at: str,
                 experiment_status: str, experiment_verdict: str,
                 **kwargs):
        self.experiment_created_at = experiment_created_at
        self.experiment_started_at = experiment_started_at
        self.experiment_finished_at = experiment_finished_at

        self.fault_name = fault_name
        self.fault_kwargs = kwargs
        self.fault_started_at = fault_started_at
        self.fault_finished_at = fault_finished_at

        self.experiment_status = experiment_status
        self.experiment_verdict = experiment_verdict

    def __dict__(self):
        return {
            "experiment_created_at": self.experiment_created_at,
            "experiment_started_at": self.experiment_started_at,
            "experiment_finished_at": self.experiment_finished_at,

            "fault_name": self.fault_name,
            "fault_started_at": self.fault_started_at,
            "fault_finished_at": self.fault_finished_at,
            "fault_kwargs": self.fault_kwargs,

            "experiment_status": self.experiment_status,
            "experiment_verdict": self.experiment_verdict
        }


class Fault(ABC):

    def __init__(self, name: str, description: str, template: str, tags: [str]):
        self.name = name
        self.description = description
        self.template = template
        self.tags = tags

        K8sConfig.load_config()
        self.k8s_client = K8sClient.CoreV1Api()

        # Logging
        self.logger = logging.getLogger(__name__)
        formatter = logging.Formatter('[%(asctime)s] - [%(name)s] - [%(levelname)s] %(message)s')
        ch = logging.StreamHandler()
        fh = logging.FileHandler(f'app.log')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def execute(self, litmus_client: client.ChaosClient, project_id: str, infra_id: str, *args, **kwargs):
        # Experiment variables
        # Workaround for ChaosCenter limitation
        experiment_name = f"{self.name}-{''.join(random.choice(string.ascii_lowercase) for i in range(8))}"
        experiment_description = self.description

        # Fault variables
        jinja = Environment(loader=FileSystemLoader("litmus/faults/templates"), trim_blocks=True, lstrip_blocks=True)
        template = jinja.get_template(self.template)

        yaml = YAML()
        manifest = yaml.load(
            template.render(experimentName=experiment_name, **kwargs))

        # ChaosCenter API does not yet correctly support updating the manifest of existing experiments.
        # Once they support it, extra logic should be added to check if the experiments exists, update it and run it.
        # https://github.com/litmuschaos/litmus/issues/4336
        # experiment_id = None
        # experiments = litmus_client.list_experiments(project_id=project_id)["data"]["listExperiment"]["experiments"]
        # for experiment in experiments:
        #     if experiment["name"] == experiment_name:
        #         experiment_id = experiment["experimentID"]
        #         break

        self.logger.info(f"Creating experiment {experiment_name}, with kwargs {kwargs}.")
        # Create new experiment
        result = litmus_client.create_experiment(project_id=project_id,
                                                 infra_id=infra_id,
                                                 experiment_name=experiment_name,
                                                 experiment_description=experiment_description,
                                                 experiment_manifest=json.dumps(manifest),
                                                 run_experiment=False, cron_syntax="", tags=self.tags, weightages=None,
                                                 is_custom_experiment=True)

        if "errors" in result:
            self.logger.warning(result)
            return None
        else:
            experiment_id = result["data"]["createChaosExperiment"]["experimentID"]
            # Run the experiment (currently not implemented because Litmus runs the experiment automatically, even with the run_experiment flag set to false)
            # https://github.com/litmuschaos/litmus/issues/4362
            # Instead we fetch the automatically executed run
            time.sleep(5)  # Wait for experiment to be created
            experiment_run_id = litmus_client.list_experiment_run(project_id=project_id, experiment_id=experiment_id) \
                ["data"]["listExperimentRun"]["experimentRuns"][0]["experimentRunID"]
            success, experiment_run_result = self.wait_for_execution(litmus_client, project_id,
                                                            experiment_run_id=experiment_run_id)

            data = json.loads(experiment_run_result["data"]["getExperimentRun"]["executionData"])
            experiment_created_at = data["creationTimestamp"]
            experiment_started_at = data["startedAt"]
            experiment_finished_at = data["finishedAt"]

            if success:
                for k, node_ in data["nodes"].items():
                    if node_["name"] == self.name:
                        started_at = node_["startedAt"]
                        finished_at = node_["finishedAt"]
                        experiment_status = node_["chaosData"]["experimentStatus"]
                        experiment_verdict = node_["chaosData"]["experimentVerdict"]

                        self.logger.info(f"Experiment {experiment_name} completed.")
                        return Result(experiment_created_at, experiment_started_at, experiment_finished_at,
                                      self.name, started_at, finished_at, experiment_status, experiment_verdict,
                                      **kwargs)

            return Result(experiment_created_at, experiment_started_at, experiment_finished_at,
                          self.name, "", "", "Error", "Fail", **kwargs)

    def wait_for_execution(self, litmus_client: client.ChaosClient, project_id, experiment_run_id=None, notify_id=None):
        result = litmus_client.get_experiment_run(project_id=project_id, experiment_run_id=experiment_run_id)
        phase = result["data"]["getExperimentRun"]["phase"]

        if phase == "Error":
            self.logger.warning(result)
            return False, result
        elif phase == "Completed":
            return True, result
        else:
            self.logger.info("Waiting for experiment to complete...")
            time.sleep(15)
            return self.wait_for_execution(litmus_client, project_id, experiment_run_id=experiment_run_id)


class NodeCPUHog(Fault):
    NAME = "node-cpu-hog"
    DESCRIPTION = "Give a CPU spike on a node belonging to a deployment"
    TEMPLATE = "node-cpu-hog.yaml.j2"
    TAGS = ["deucalion", "node-cpu-hog"]

    def __init__(self, app_namespace: str, app_node: str = None,
                 experiment_duration: int = None, experiment_ramp_time: int = None):
        self.app_namespace = app_namespace
        self.app_node = app_node

        self.experiment_duration = experiment_duration
        self.experiment_ramp_time = experiment_ramp_time

        super().__init__(self.NAME, self.DESCRIPTION, self.TEMPLATE, self.TAGS)

    def execute(self, litmus_client: client.ChaosClient, project_id: str, infra_id: str, *args, **kwargs):
        if not self.app_node:
            nodes = self.k8s_client.list_node(label_selector="chaos=target").items

            target = random.choice(nodes)
            self.app_node = target.metadata.name

        if self.experiment_duration is None:
            self.experiment_duration = random.randint(60, 300)
        if self.experiment_ramp_time is None:
            self.experiment_ramp_time = random.randint(0, 30)

        return super().execute(litmus_client, project_id, infra_id, appNamespace=self.app_namespace,
                               appNode=self.app_node, experimentDuration=self.experiment_duration,
                               experimentRampTime=self.experiment_ramp_time)


class NodeDrain(Fault):
    NAME = "node-drain"
    DESCRIPTION = "Drain the node where application pod is scheduled"
    TEMPLATE = "node-drain.yaml.j2"
    TAGS = ["deucalion", "node-drain"]

    def __init__(self, app_namespace: str, app_node: str = None, app_label: str = "chaos=target",
                 experiment_duration: int = None, experiment_ramp_time: int = None):
        self.app_namespace = app_namespace
        self.app_node = app_node
        self.app_label = app_label

        self.experiment_duration = experiment_duration
        self.experiment_ramp_time = experiment_ramp_time

        super().__init__(self.NAME, self.DESCRIPTION, self.TEMPLATE, self.TAGS)

    def execute(self, litmus_client: client.ChaosClient, project_id: str, infra_id: str, *args, **kwargs):
        if not self.app_node:
            nodes = self.k8s_client.list_node(label_selector="chaos=target").items

            target = random.choice(nodes)
            self.app_node = target.metadata.name

        if self.experiment_duration is None:
            self.experiment_duration = random.randint(60, 300)
        if self.experiment_ramp_time is None:
            self.experiment_ramp_time = random.randint(0, 30)

        return super().execute(litmus_client, project_id, infra_id, appNamespace=self.app_namespace,
                               appNode=self.app_node, appLabel=self.app_label,
                               experimentDuration=self.experiment_duration,
                               experimentRampTime=self.experiment_ramp_time)



class NodeMemoryHog(Fault):
    NAME = "node-memory-hog"
    DESCRIPTION = "Give a memory spike on a node belonging to a deployment"
    TEMPLATE = "node-memory-hog.yaml.j2"
    TAGS = ["deucalion", "node-memory-hog"]

    def __init__(self, app_namespace: str, app_node: str = None,
                 experiment_duration: int = None, experiment_ramp_time: int = None):
        self.app_namespace = app_namespace
        self.app_node = app_node

        self.experiment_duration = experiment_duration
        self.experiment_ramp_time = experiment_ramp_time

        super().__init__(self.NAME, self.DESCRIPTION, self.TEMPLATE, self.TAGS)

    def execute(self, litmus_client: client.ChaosClient, project_id: str, infra_id: str, *args, **kwargs):
        if not self.app_node:
            nodes = self.k8s_client.list_node(label_selector="chaos=target").items

            target = random.choice(nodes)
            self.app_node = target.metadata.name

        if self.experiment_duration is None:
            self.experiment_duration = random.randint(60, 300)
        if self.experiment_ramp_time is None:
            self.experiment_ramp_time = random.randint(0, 30)

        return super().execute(litmus_client, project_id, infra_id,
                               appNamespace=self.app_namespace, appNode=self.app_node,
                               experimentDuration=self.experiment_duration,
                               experimentRampTime=self.experiment_ramp_time)


class PodAutoscaler(Fault):
    NAME = "pod-autoscaler"
    DESCRIPTION = ""
    TEMPLATE = "pod-autoscaler.yaml.j2"
    TAGS = ["deucalion", "pod-autoscaler"]

    def __init__(self, app_namespace: str, app_label: str = None,
                 app_kind: str = "deployment", app_replica_count: int = None,
                 experiment_duration: int = None, experiment_ramp_time: int = None):
        self.app_namespace = app_namespace
        self.app_kind = app_kind
        self.app_label = app_label
        self.app_replica_count = app_replica_count

        self.experiment_duration = experiment_duration
        self.experiment_ramp_time = experiment_ramp_time

        super().__init__(self.NAME, self.DESCRIPTION, self.TEMPLATE, self.TAGS)

    def execute(self, litmus_client: client.ChaosClient, project_id: str, infra_id: str, *args, **kwargs):
        if not self.app_label:
            pods = self.k8s_client.list_namespaced_pod(self.app_namespace, label_selector="chaos=target").items

            target = random.choice(pods)
            self.app_label = target.metadata.labels['app']
            print("Target: ", target.metadata.labels['app'])

        if self.app_replica_count is None:
            self.app_replica_count = random.randint(2, 3)

        if self.experiment_duration is None:
            self.experiment_duration = random.randint(600, 1800)

        print("Replica Count: ", self.app_replica_count)
        print("Duration: ", self.experiment_duration)
        print("Ramp Time: ", self.experiment_ramp_time)

        return super().execute(litmus_client, project_id, infra_id,
                               appNamespace=self.app_namespace, appLabel=self.app_label,
                               appKind=self.app_kind, appReplicaCount=self.app_replica_count,
                               experimentDuration=self.experiment_duration)


class PodCPUHog(Fault):
    NAME = "pod-cpu-hog"
    DESCRIPTION = ""
    TEMPLATE = "pod-cpu-hog.yaml.j2"
    TAGS = ["deucalion", "pod-cpu-hog"]

    def __init__(self, app_namespace: str, app_label: str = None,
                 app_kind: str = "deployment", app_container: str = None,
                 experiment_duration: int = None, experiment_ramp_time: int = None):
        self.app_namespace = app_namespace
        self.app_kind = app_kind
        self.app_label = app_label
        self.app_container = app_container

        self.experiment_duration = experiment_duration
        self.experiment_ramp_time = experiment_ramp_time

        super().__init__(self.NAME, self.DESCRIPTION, self.TEMPLATE, self.TAGS)

    def execute(self, litmus_client: client.ChaosClient, project_id: str, infra_id: str, *args, **kwargs):
        if not self.app_label:
            pods = self.k8s_client.list_namespaced_pod(self.app_namespace, label_selector="chaos=target").items

            target = random.choice(pods)
            self.app_label = target.metadata.labels['app']
            self.app_container = target.spec.containers[0].name

        if self.experiment_duration is None:
            self.experiment_duration = random.randint(60, 300)
        if self.experiment_ramp_time is None:
            self.experiment_ramp_time = random.randint(0, 30)

        return super().execute(litmus_client, project_id, infra_id, appNamespace=self.app_namespace,
                               appLabel=self.app_label,
                               appKind=self.app_kind, appContainer=self.app_container,
                               experimentDuration=self.experiment_duration,
                               experimentRampTime=self.experiment_ramp_time)


class PodDelete(Fault):
    NAME = "pod-delete"
    DESCRIPTION = ""
    TEMPLATE = "pod-delete.yaml.j2"
    TAGS = ["deucalion", "pod-delete"]

    def __init__(self, app_namespace: str, app_label: str = None,
                 app_kind: str = "deployment"):
        self.app_namespace = app_namespace
        self.app_label = app_label
        self.app_kind = app_kind

        super().__init__(self.NAME, self.DESCRIPTION, self.TEMPLATE, self.TAGS)

    def execute(self, litmus_client: client.ChaosClient, project_id: str, infra_id: str, *args, **kwargs):
        if not self.app_label:
            pods = self.k8s_client.list_namespaced_pod(self.app_namespace, label_selector="chaos=target").items

            target = random.choice(pods)
            self.app_label = target.metadata.labels['app']

        return super().execute(litmus_client, project_id, infra_id, appNamespace=self.app_namespace,
                               appLabel=self.app_label,
                               appKind=self.app_kind)


class PodMemoryHog(Fault):
    NAME = "pod-memory-hog"
    DESCRIPTION = ""
    TEMPLATE = "pod-memory-hog.yaml.j2"
    TAGS = ["deucalion", "pod-memory-hog"]

    def __init__(self, app_namespace: str, app_label: str = None,
                 app_kind: str = "deployment", app_container: str = "server",
                 experiment_duration: int = None, experiment_ramp_time: int = None):
        self.app_namespace = app_namespace
        self.app_label = app_label
        self.app_kind = app_kind
        self.app_container = app_container

        self.experiment_duration = experiment_duration
        self.experiment_ramp_time = experiment_ramp_time

        super().__init__(self.NAME, self.DESCRIPTION, self.TEMPLATE, self.TAGS)

    def execute(self, litmus_client: client.ChaosClient, project_id: str, infra_id: str, *args, **kwargs):
        if not self.app_label:
            pods = self.k8s_client.list_namespaced_pod(self.app_namespace, label_selector="chaos=target").items

            target = random.choice(pods)
            self.app_label = target.metadata.labels['app']
            self.app_container = target.spec.containers[0].name

        if self.experiment_duration is None:
            self.experiment_duration = random.randint(60, 300)
        if self.experiment_ramp_time is None:
            self.experiment_ramp_time = random.randint(0, 30)

        return super().execute(litmus_client, project_id, infra_id, appNamespace=self.app_namespace,
                               appLabel=self.app_label,
                               appKind=self.app_kind, appContainer=self.app_container)


class PodNetworkLatency(Fault):
    NAME = "pod-network-latency"
    DESCRIPTION = ""
    TEMPLATE = "pod-network-latency.yaml.j2"
    TAGS = ["deucalion", "pod-network-latency"]

    def __init__(self, app_namespace: str, app_label: str = None,
                 app_kind: str = "deployment", app_container: str = "server",
                 app_network_latency: int = None, app_jitter: int = None,
                 experiment_duration: int = None, experiment_ramp_time: int = None):
        self.app_namespace = app_namespace
        self.app_label = app_label
        self.app_kind = app_kind
        self.app_container = app_container
        self.app_network_latency = app_network_latency
        self.app_jitter = app_jitter

        self.experiment_duration = experiment_duration
        self.experiment_ramp_time = experiment_ramp_time

        super().__init__(self.NAME, self.DESCRIPTION, self.TEMPLATE, self.TAGS)

    def execute(self, litmus_client: client.ChaosClient, project_id: str, infra_id: str, *args, **kwargs):
        if not self.app_label:
            pods = self.k8s_client.list_namespaced_pod(self.app_namespace, label_selector="chaos=target").items

            target = random.choice(pods)
            self.app_label = target.metadata.labels['app']
            self.app_container = target.spec.containers[0].name
            print("Target: ", target.metadata.labels['app'])

        if self.app_network_latency is None:
            self.app_network_latency = random.randint(500, 2000)
        if self.app_jitter is None:
            self.app_jitter = random.randint(0, 100)

        if self.experiment_duration is None:
            self.experiment_duration = random.randint(60, 300)
        if self.experiment_ramp_time is None:
            self.experiment_ramp_time = random.randint(0, 30)

        return super().execute(litmus_client, project_id, infra_id, appNamespace=self.app_namespace,
                               appLabel=self.app_label,
                               appKind=self.app_kind, appContainer=self.app_container,
                               appNetworkLatency=self.app_network_latency,
                               appJitter=self.app_jitter,
                               experimentDuration=self.experiment_duration,
                               experimentRampTime=self.experiment_ramp_time)
