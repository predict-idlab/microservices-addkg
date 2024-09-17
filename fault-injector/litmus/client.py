from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from litmus.schema import Query, Mutation, Subscription, ChaosExperimentRequest


class ChaosClient:
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def execute(self, operation):
        headers = {"Authorization": self.token}
        endpoint = HTTPEndpoint(self.url, base_headers=headers)

        return endpoint(query=operation)

    def list_infrastructures(self, project_id):
        op = Operation(Query)
        op.list_infras(project_id=project_id)
        op.list_infras.infras.infra_id()
        op.list_infras.infras.name()

        return self.execute(op)

    def list_experiment(self, project_id):
        op = Operation(Query)
        op.list_experiment(project_id=project_id, request={})
        op.list_experiment.experiments.experiment_id()
        op.list_experiment.experiments.name()

        return self.execute(op)

    def get_experiment(self, project_id, experiment_id):
        op = Operation(Query)
        op.get_experiment(project_id=project_id, experiment_id=experiment_id)
        op.get_experiment.experiment_details().name()
        op.get_experiment.experiment_details().description()
        op.get_experiment.experiment_details().tags()
        op.get_experiment.experiment_details().created_at()
        op.get_experiment.experiment_details().created_by()
        op.get_experiment.experiment_details().updated_at()
        op.get_experiment.experiment_details().updated_by()
        op.get_experiment.average_resiliency_score()

        return self.execute(op)

    def create_experiment(self, project_id, infra_id, experiment_name,
                          experiment_description, experiment_manifest,
                          run_experiment=False, cron_syntax="",
                          tags=None, weightages=None, is_custom_experiment=False):
        op = Operation(Mutation)

        op.create_chaos_experiment(project_id=project_id, request=ChaosExperimentRequest(infra_id=infra_id, experiment_name=experiment_name, experiment_description=experiment_description, experiment_manifest=experiment_manifest, run_experiment=run_experiment, cron_syntax=cron_syntax, tags=tags or [], weightages=weightages or [], is_custom_experiment=is_custom_experiment))
        op.create_chaos_experiment().experiment_id()

        return self.execute(op)

    def update_experiment(self, project_id, infra_id, experiment_id, experiment_name,
                          experiment_description, experiment_manifest,
                          run_experiment=False, cron_syntax="",
                          tags=None, weightages=None, is_custom_experiment=False):
        op = Operation(Mutation)

        op.update_chaos_experiment(project_id=project_id, request=ChaosExperimentRequest(infra_id=infra_id, experiment_id=experiment_id, experiment_name=experiment_name, experiment_description=experiment_description, experiment_manifest=experiment_manifest, run_experiment=run_experiment, cron_syntax=cron_syntax, tags=tags or [], weightages=weightages or [], is_custom_experiment=is_custom_experiment))
        op.update_chaos_experiment().experiment_id()

        return self.execute(op)

    def delete_experiment(self, project_id, experiment_id):
        op = Operation(Mutation)

        op.delete_chaos_experiment(project_id=project_id, experiment_id=experiment_id)

        return self.execute(op)

    def list_experiment_run(self, project_id, experiment_id):
        op = Operation(Query)

        op.list_experiment_run(project_id=project_id, request={"experimentIDs": [experiment_id]})
        op.list_experiment_run.experiment_runs.experiment_run_id()
        op.list_experiment_run.experiment_runs.notify_id()
        op.list_experiment_run.experiment_runs.phase()
        op.list_experiment_run.experiment_runs.created_at()
        op.list_experiment_run.experiment_runs.updated_at()

        return self.execute(op)

    def get_experiment_run(self, project_id, experiment_run_id=None, notify_id=None):
        op = Operation(Query)

        if experiment_run_id is not None:
            op.get_experiment_run(project_id=project_id, experiment_run_id=experiment_run_id)
        elif notify_id is not None:
            op.get_experiment_run(project_id=project_id, notify_id=notify_id)
        else:
            raise Exception("Either experiment_run_id or notify_id is required")

        op.get_experiment_run.experiment_run_id()
        op.get_experiment_run.notify_id()
        op.get_experiment_run.phase()
        op.get_experiment_run.created_at()
        op.get_experiment_run.updated_at()
        op.get_experiment_run.execution_data()

        return self.execute(op)

    def run_chaos_experiment(self, project_id, experiment_id):
        op = Operation(Mutation)

        op.run_chaos_experiment(project_id=project_id, experiment_id=experiment_id)
        op.run_chaos_experiment().notify_id()

        return self.execute(op)
