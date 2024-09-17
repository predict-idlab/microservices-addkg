import logging
from copy import deepcopy
from typing import Set

from kubernetes import client as K8sClient, config as K8sConfig
import networkx as nx
from prometheus_api_client import PrometheusConnect
from prometheus_api_client.utils import parse_datetime
from rdflib import Graph, URIRef, Literal

from ontology import deucalion


# https://prometheus.io/docs/guides/cadvisor/
# kwargs: container, pod
cadvisor_metrics = {
    "container_cpu_usage_seconds_total": {
        "name": "CPU Usage (Container)",
        "description": "The cgroup\"s total CPU usage in seconds",
        "type": "DISTRIBUTION",
        "property": deucalion.hasCPU
    },
    "container_memory_usage_bytes": {
        "name": "Memory Usage (Container)",
        "description": "The cgroup\"s total memory usage in bytes",
        "type": "DISTRIBUTION",
        "property": deucalion.hasMemory
    },
    # "container_network_transmit_bytes_total": {
    #     "name": "TX (Container)",
    #     "description": "Bytes transmitted over the network by the container per second",
    #     "type": "DISTRIBUTION"
    # },
    # "container_network_receive_bytes_total": {
    #     "name": "RX (Container)",
    #     "description": "Bytes received over the network by the container per second",
    #     "type": "DISTRIBUTION"
    # },
}

# https://prometheus.io/docs/guides/node-exporter/
# https://stackoverflow.com/a/66644946/5394571
# kwargs: node
node_exporter_metrics = {
    "node_cpu_seconds_total": {
        "name": "CPU Usage (Node)",
        "description": "The average amount of CPU time spent in system mode, per second in seconds",
        "type": "DISTRIBUTION",
        "query": 'sum(rate(node_cpu_seconds_total{{node="{node}"}}[5m])) by (node)',
        "property": deucalion.hasCPU
    },
    "node_memory_Active_bytes": {
        "name": "Memory Usage (Node)",
        "description": "The average amount of memory (in %) that is in active use",
        "type": "DISTRIBUTION",
        "query": 'sum(avg_over_time(node_memory_Active_bytes{{node="{node}"}}[5m])) by (node) / sum(avg_over_time(node_memory_MemTotal_bytes{{node="{node}"}}[5m])) by (node)',
        "property": deucalion.hasMemory
    }
    # "node_filesystem_avail_bytes": {
    #     "name": "Filesystem available (Node)",
    #     "description": "The filesystem space available to non-root users in bytes",
    #     "type": "DISTRIBUTION",
    #     "property": deucalion.hasFileSystemAvailable
    # },
    # "node_filesystem_free_bytes": {
    #     "name": "Filesystem free (Node)",
    #     "description": "The filesystem space free in bytes",
    #     "type": "DISTRIBUTION"
    # },
    # "node_filesystem_size_bytes": {
    #     "name": "Filesystem size (Node)",
    #     "description": "The filesystem size in bytes",
    #     "type": "DISTRIBUTION",
    #     "property": deucalion.hasFileSystemSize
    # },
    # "node_network_receive_bytes_total": {
    #     "name": "RX (Node)",
    #     "description": "The average network traffic received, per second in bytes",
    #     "type": "DISTRIBUTION"
    # }
}

# https://istio.io/latest/docs/reference/config/metrics/
# kwargs: source, destination
istio_metrics = {
    "istio_requests_total": {
        "name": "Request Count",
        "description": "This is a COUNTER incremented for every request handled by an Istio proxy.",
        "type": "COUNTER",
        "query": 'sum(rate(istio_requests_total{{'
                 'pod="{source}", '
                 'destination_service="{destination}", '
                 'reporter="source"'
                 '}}[5m])) by (pod, destination_service)',
        "property": deucalion.hasRequestCount
    },
    "istio_requests_total_4xx": {
        "name": "Request Count with 4XX response codes",
        "description": "This is a COUNTER incremented for every request handled by an Istio proxy.",
        "type": "COUNTER",
        "query": 'sum(rate(istio_requests_total{{'
                 'pod="{source}", '
                 'destination_service="{destination}", '
                 'reporter="source",'
                 'response_code=~"4.*"'
                 '}}[5m])) by (pod, destination_service)',
        "property": deucalion.hasRequestCount4XX
    },
    "istio_requests_total_5xx": {
        "name": "Request Count with 5XX response codes",
        "description": "This is a COUNTER incremented for every request handled by an Istio proxy.",
        "type": "COUNTER",
        "query": 'sum(rate(istio_requests_total{{'
                 'pod="{source}", '
                 'destination_service="{destination}", '
                 'reporter="source",'
                 'response_code=~"5.*"'
                 '}}[5m])) by (pod, destination_service)',
        "property": deucalion.hasRequestCount5XX
    },
    "istio_requests_duration_milliseconds": {
        "name": "Request Duration",
        "description": "This is a DISTRIBUTION which measures the duration of requests.",
        "type": "DISTRIBUTION",
        "query": 'sum(rate(istio_request_duration_milliseconds_sum{{'
                 'pod="{source}", '
                 'destination_service="{destination}", '
                 'reporter="source"'
                 '}}[5m])) by (destination_service) / '
                 'sum(rate(istio_request_duration_milliseconds_count{{'
                 'pod="{source}", '
                 'destination_service="{destination}", '
                 'reporter="source"'
                 '}}[5m])) by (destination_service)',
        "property": deucalion.hasRequestDuration
    },
    "istio_request_bytes": {
        "name": "Request Size",
        "description": "This is a DISTRIBUTION which measures HTTP request body sizes.",
        "type": "DISTRIBUTION",
        "query": 'sum(rate(istio_request_bytes_sum{{'
                 'pod="{source}", '
                 'destination_service="{destination}", '
                 'reporter="source"'
                 '}}[5m])) by (destination_service) / '
                 'sum(rate(istio_request_bytes_count{{'
                 'pod="{source}", '
                 'destination_service="{destination}", '
                 'reporter="source"'
                 '}}[5m])) by (destination_service)',
        "property": deucalion.hasRequestSize
    },
    # "istio_response_bytes": {
    #     "name": "Response Size",
    #     "description": "This is a DISTRIBUTION which measures HTTP response body sizes.",
    #     "type": "DISTRIBUTION"
    # },
    # "istio_request_messages_total": {
    #     "name": "gRPC Request Message Count",
    #     "description": "This is a COUNTER incremented for every gRPC message sent from a client.",
    #     "type": "COUNTER"
    # },
    # "istio_response_messages_total": {
    #     "name": "gRPC Response Message Count",
    #     "description": "This is a COUNTER incremented for every gRPC message sent from a server.",
    #     "type": "COUNTER"
    # },
    # "istio_tcp_sent_bytes_total": {
    #     "name": "Tcp Bytes Sent",
    #     "description": "This is a COUNTER which measures the size of total bytes sent during response in case of a TCP connection.",
    #     "type": "COUNTER"
    # },
    # "istio_tcp_received_bytes_total": {
    #     "name": "Tcp Bytes Received",
    #     "description": "This is a COUNTER which measures the size of total bytes received during request in case of a TCP connection.",
    #     "type": "COUNTER"
    # },
    # "istio_tcp_connections_opened_total": {
    #     "name": "Tcp Connections Opened",
    #     "description": "This is a COUNTER incremented for every opened connection.",
    #     "type": "COUNTER"
    # },
    # "istio_tcp_connections_closed_total": {
    #     "name": "Tcp Connections Closed",
    #     "description": "This is a COUNTER incremented for every closed connection.",
    #     "type": "COUNTER"
    # }
}


class DataCollector:

    def __init__(self, host: str = "http://localhost:9090", namespace: str = None, log_level="INFO", log_file=None):
        self.client = PrometheusConnect(url=host, disable_ssl=True)
        self.namespace = namespace

        # Logging
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger(__name__)
        formatter = logging.Formatter('[%(asctime)s] - [%(name)s] - [%(levelname)s] %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        if log_file:
            fh = logging.FileHandler(log_file)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

    def fetch_infrastructure_topology(self) -> Graph:
        K8sConfig.load_config()

        v1 = K8sClient.CoreV1Api()

        cluster = deucalion.Cluster("cluster.local")
        for node in v1.list_node().items:
            node_ = deucalion.Node(node.metadata.name)
            if hasattr(cluster, "has_node"):
                cluster.has_node.append(node_)
            else:
                cluster.has_node = node_

        if not self.namespace:
            services = v1.list_service_for_all_namespaces().items
        else:
            services = v1.list_namespaced_service(self.namespace).items

        services_targets = {}
        for service in services:
            service_ = deucalion.Service(f"{service.metadata.name}.{service.metadata.namespace}.svc.cluster.local")
            services_targets[service_] = service.metadata.labels

        if not self.namespace:
            pods = v1.list_pod_for_all_namespaces().items
        else:
            pods = v1.list_namespaced_pod(self.namespace).items

        for pod in pods:
            pod_ = deucalion.Pod(pod.metadata.name)

            for owner in pod.metadata.owner_references:
                owner_ = None
                if owner.kind == "ReplicaSet":
                    owner_ = deucalion.ReplicaSet(owner.name)
                elif owner.kind == "Deployment":
                    owner_ = deucalion.Deployment(owner.name)

                if owner_ is not None:
                    if hasattr(owner_, "controls"):
                        owner_.controls.append(pod_)
                    else:
                        owner_.controls = pod_
                    pod_.is_controlled_by = owner_

            for service_, targets in services_targets.items():
                for k, v in pod.metadata.labels.items():
                    if k in targets.keys() and v == targets[k]:
                        if hasattr(service_, "serves"):
                            service_.serves.append(pod_)
                        else:
                            service_.serves = pod_
                        pod_.is_served_by = service_

            node_ = deucalion.Node(pod.spec.node_name)

            if hasattr(node_, "has_pod"):
                node_.has_pod.append(pod_)
            else:
                node_.has_pod = pod_

            for container in pod.spec.containers:
                container_ = deucalion.Container(f"{pod.metadata.name}.{container.name}")

                image_ = deucalion.Image(container.image)
                image_name = container.image.split(":")
                image_.has_name = image_name[0]
                image_.has_tag = image_name[1] if len(image_name) >= 2 else "latest"

                container_.has_image = image_

                if hasattr(pod_, "has_container"):
                    pod_.has_container.append(container_)
                else:
                    pod_.has_container = container_

        return deucalion.world

    def fetch_network_topology(self, namespace=".+") -> nx.Graph:
        requests_data = self.client.get_metric_range_data(
            metric_name=f'istio_requests_total{{namespace=~"{namespace}"}}',
            start_time=parse_datetime("5m"),
            end_time=parse_datetime("now")
        )

        topology = nx.Graph()

        for dp_ in requests_data:
            metric = dp_["metric"]

            if not metric["source_workload"] == "unknown" and \
                    not metric["source_workload"] == "unknown":
                topology.add_edge(
                    f"{metric['source_workload']}.{metric['source_workload_namespace']}",
                    f"{metric['destination_workload']}.{metric['destination_workload_namespace']}"
                )

        return topology

    def query_container_metric(self, graph: Graph, container_: deucalion.Container, start_time=parse_datetime("5m"), end_time=parse_datetime("now")):
        pod_id = container_.name.split(".")[0]
        container_id = container_.name.split(".")[1]

        for metric_id, metric in cadvisor_metrics.items():
            data = self.client.get_metric_aggregation(
                query=f'sum(rate({metric_id}{{container="{container_id}", pod="{pod_id}"}}[5m])) by (container, pod)',
                operations=["min", "max", "average", "percentile_50", "percentile_90", "percentile_95", "deviation", "variance"],
                start_time=start_time,
                end_time=end_time
            )

            if data is not None:
                for k, v in data.items():
                    graph.add((container_.ref, URIRef(f'{metric["property"]}_{k}'), Literal(v)))

    def query_node_metric(self, graph: Graph, node_: deucalion.Node, start_time=parse_datetime("5m"), end_time=parse_datetime("now")):
        for metric_id, metric in node_exporter_metrics.items():
            data = self.client.get_metric_aggregation(
                query=metric["query"].format(node=node_.name),
                operations=["min", "max", "average", "percentile_50", "percentile_90", "percentile_95", "deviation", "variance"],
                start_time=start_time,
                end_time=end_time
            )

            if data is not None:
                for k, v in data.items():
                    graph.add((node_.ref, URIRef(f'{metric["property"]}_{k}'), Literal(v)))

    def get_network_connections_pod(self, pod_: deucalion.Pod, start_time=parse_datetime("5m"), end_time=parse_datetime("now")) -> Set[deucalion.Service]:
        data = self.client.custom_query_range(
            query=f'sum(rate(istio_requests_total{{pod="{pod_.name}", reporter="source"}}[5m])) by (pod, destination_service)',
            start_time=start_time,
            end_time=end_time,
            step="15"
        )

        external_source = self.client.custom_query_range(
            query=f'sum(rate(istio_requests_total{{pod="{pod_.name}", reporter="destination"}}[5m])) by (pod, destination_service)',
            start_time=start_time,
            end_time=end_time,
            step="15"
        )

        connections_ = set()
        if data:
            for entry in data:
                connections_.add(deucalion.Service(entry["metric"]["destination_service"]))
        return connections_

    def query_network_connection_metric(self, graph: Graph, source_: deucalion.Pod, destination_: deucalion.Service, start_time=parse_datetime("5m"), end_time=parse_datetime("now")):
        connection = deucalion.Connection(name=f'Connection?source={source_.name}&destination={destination_.name}')

        for metric_id, metric in istio_metrics.items():
            data = self.client.get_metric_aggregation(
                query=metric["query"].format(source=source_.name, destination=destination_.name),
                operations=["min", "max", "average", "percentile_50", "percentile_90", "percentile_95", "deviation", "variance"],
                start_time=start_time,
                end_time=end_time
            )

            if data:
                for k, v in data.items():
                    graph.add((connection.ref, URIRef(f'{metric["property"]}_{k}'), Literal(v)))
            else:
                for k in ["min", "max", "average", "percentile_50", "percentile_90", "percentile_95", "deviation", "variance"]:
                    graph.add((connection.ref, URIRef(f'{metric["property"]}_{k}'), Literal(0)))

        graph.add((connection.ref, deucalion.hasSource.ref, source_.ref))
        graph.add((connection.ref, deucalion.hasDestination.ref, destination_.ref))
        graph.add((source_.ref, deucalion.hasConnection.ref, connection.ref))

    def query_network_pod_metric(self, graph: Graph, pod_: deucalion.Pod, start_time=parse_datetime("5m"), end_time=parse_datetime("now")):
        for metric_id, metric in istio_metrics.items():
            data = self.client.get_metric_aggregation(
                query=metric["query"].format(source=pod_.name, destination=pod_.name),
                operations=["min", "max", "average", "percentile_50", "percentile_90", "percentile_95", "deviation", "variance"],
                start_time=start_time,
                end_time=end_time,
            )

            if data is not None:
                for k, v in data.items():
                    graph.add((pod_.ref, URIRef(f'{metric["property"]}_{k}'), Literal(v)))

    def fetch_monitoring_data(self, start_time=parse_datetime("5m"), end_time=parse_datetime("now")):
        graph = deepcopy(self.fetch_infrastructure_topology())

        for id_, node in deucalion.Node.instances.items():
            self.logger.info(f"Querying metrics for node {node.name}")
            self.query_node_metric(graph, node, start_time, end_time)

        for id_, pod in deucalion.Pod.instances.items():
            self.logger.info(f"Querying metrics for pod {pod.name}")
            self.query_network_pod_metric(graph, pod, start_time, end_time)

            connections = self.get_network_connections_pod(pod, start_time, end_time)
            for destination in connections:
                self.query_network_connection_metric(graph, pod, destination, start_time, end_time)

        # for metric, metric_info in cadvisor_metrics.items():
        for id_, container in deucalion.Container.instances.items():
            self.logger.info(f"Querying metrics for container {container.name}")
            self.query_container_metric(graph, container, start_time, end_time)

        return graph

