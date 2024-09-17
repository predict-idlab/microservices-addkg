import sgqlc.types

chaos = sgqlc.types.Schema()

__docformat__ = 'markdown'


########################################################################
# Scalars and Enumerations
########################################################################
class AuthType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `BASIC`
    * `NONE`
    * `SSH`
    * `TOKEN`
    '''
    __schema__ = chaos
    __choices__ = ('BASIC', 'NONE', 'SSH', 'TOKEN')


Boolean = sgqlc.types.Boolean


class EnvironmentSortingField(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `NAME`
    * `TIME`
    '''
    __schema__ = chaos
    __choices__ = ('NAME', 'TIME')


class EnvironmentType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `NON_PROD`
    * `PROD`
    '''
    __schema__ = chaos
    __choices__ = ('NON_PROD', 'PROD')


class ExperimentRunStatus(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `All`
    * `Completed`
    * `Completed_With_Error`
    * `Error`
    * `NA`
    * `Running`
    * `Skipped`
    * `Stopped`
    * `Timeout`
    '''
    __schema__ = chaos
    __choices__ = (
        'All', 'Completed', 'Completed_With_Error', 'Error', 'NA', 'Running', 'Skipped', 'Stopped', 'Timeout')


class ExperimentSortingField(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `NAME`
    * `TIME`
    '''
    __schema__ = chaos
    __choices__ = ('NAME', 'TIME')


class ExperimentType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `All`
    * `ChaosEngine`
    * `ChaosSchedule`
    * `CronExperiment`
    * `Experiment`
    '''
    __schema__ = chaos
    __choices__ = ('All', 'ChaosEngine', 'ChaosSchedule', 'CronExperiment', 'Experiment')


class FileType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CSV`
    * `ENGINE`
    * `EXPERIMENT`
    * `WORKFLOW`
    '''
    __schema__ = chaos
    __choices__ = ('CSV', 'ENGINE', 'EXPERIMENT', 'WORKFLOW')


Float = sgqlc.types.Float


class HubType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `GIT`
    * `REMOTE`
    '''
    __schema__ = chaos
    __choices__ = ('GIT', 'REMOTE')


ID = sgqlc.types.ID


class INFRA_SCOPE(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `cluster`
    * `namespace`
    '''
    __schema__ = chaos
    __choices__ = ('cluster', 'namespace')


class ImagePullPolicy(sgqlc.types.Enum):
    '''Defines the different types of Image Pull Policy

    Enumeration Choices:

    * `Always`
    * `IfNotPresent`
    * `Never`
    '''
    __schema__ = chaos
    __choices__ = ('Always', 'IfNotPresent', 'Never')


class InfrastructureType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `Kubernetes`
    '''
    __schema__ = chaos
    __choices__ = ('Kubernetes',)


Int = sgqlc.types.Int


class Invitation(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `Accepted`
    * `Pending`
    '''
    __schema__ = chaos
    __choices__ = ('Accepted', 'Pending')


class MemberRole(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `Editor`
    * `Owner`
    * `Viewer`
    '''
    __schema__ = chaos
    __choices__ = ('Editor', 'Owner', 'Viewer')


class Mode(sgqlc.types.Enum):
    '''Defines the different modes of Probes

    Enumeration Choices:

    * `Continuous`
    * `EOT`
    * `Edge`
    * `OnChaos`
    * `SOT`
    '''
    __schema__ = chaos
    __choices__ = ('Continuous', 'EOT', 'Edge', 'OnChaos', 'SOT')


class ProbeStatus(sgqlc.types.Enum):
    '''Defines the different statuses of Probes

    Enumeration Choices:

    * `Completed`
    * `Error`
    * `NA`
    * `Queued`
    * `Running`
    * `Stopped`
    '''
    __schema__ = chaos
    __choices__ = ('Completed', 'Error', 'NA', 'Queued', 'Running', 'Stopped')


class ProbeType(sgqlc.types.Enum):
    '''Defines the different types of Probes

    Enumeration Choices:

    * `cmdProbe`
    * `httpProbe`
    * `k8sProbe`
    * `promProbe`
    '''
    __schema__ = chaos
    __choices__ = ('cmdProbe', 'httpProbe', 'k8sProbe', 'promProbe')


class ProbeVerdict(sgqlc.types.Enum):
    '''Defines the older different statuses of Probes

    Enumeration Choices:

    * `Awaited`
    * `Failed`
    * `NA`
    * `Passed`
    '''
    __schema__ = chaos
    __choices__ = ('Awaited', 'Failed', 'NA', 'Passed')


class ScheduleType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ALL`
    * `CRON`
    * `NON_CRON`
    '''
    __schema__ = chaos
    __choices__ = ('ALL', 'CRON', 'NON_CRON')


String = sgqlc.types.String


class UpdateStatus(sgqlc.types.Enum):
    '''UpdateStatus represents if infra needs to be updated

    Enumeration Choices:

    * `AVAILABLE`
    * `MANDATORY`
    * `NOT_REQUIRED`
    '''
    __schema__ = chaos
    __choices__ = ('AVAILABLE', 'MANDATORY', 'NOT_REQUIRED')


########################################################################
# Input Objects
########################################################################
class CMDProbeRequest(sgqlc.types.Input):
    '''Defines the input for CMD probe properties'''
    __schema__ = chaos
    __field_names__ = (
        'probe_timeout', 'interval', 'retry', 'attempt', 'probe_polling_interval', 'initial_delay',
        'evaluation_timeout',
        'stop_on_failure', 'command', 'comparator', 'source')
    probe_timeout = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='probeTimeout')
    '''Timeout of the Probe'''

    interval = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='interval')
    '''Interval of the Probe'''

    retry = sgqlc.types.Field(Int, graphql_name='retry')
    '''Retry interval of the Probe'''

    attempt = sgqlc.types.Field(Int, graphql_name='attempt')
    '''Attempt contains the total attempt count for the probe'''

    probe_polling_interval = sgqlc.types.Field(String, graphql_name='probePollingInterval')
    '''Polling interval of the Probe'''

    initial_delay = sgqlc.types.Field(String, graphql_name='initialDelay')
    '''Initial delay interval of the Probe in seconds'''

    evaluation_timeout = sgqlc.types.Field(String, graphql_name='evaluationTimeout')
    '''EvaluationTimeout is the timeout window in which the SLO metrics'''

    stop_on_failure = sgqlc.types.Field(Boolean, graphql_name='stopOnFailure')
    '''Is stop on failure enabled in the Probe'''

    command = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='command')
    '''Command of the Probe'''

    comparator = sgqlc.types.Field(sgqlc.types.non_null('ComparatorInput'), graphql_name='comparator')
    '''Comparator of the Probe'''

    source = sgqlc.types.Field(String, graphql_name='source')
    '''Source of the Probe'''


class ChaosExperimentRequest(sgqlc.types.Input):
    '''Defines the details for a chaos experiment'''
    __schema__ = chaos
    __field_names__ = (
        'experiment_id', 'run_experiment', 'experiment_manifest', 'experiment_type', 'cron_syntax', 'experiment_name',
        'experiment_description', 'weightages', 'is_custom_experiment', 'infra_id', 'tags')
    experiment_id = sgqlc.types.Field(String, graphql_name='experimentID')
    '''ID of the experiment'''

    run_experiment = sgqlc.types.Field(Boolean, graphql_name='runExperiment')
    '''Boolean check indicating if the created scenario will be executed
    or not
    '''

    experiment_manifest = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentManifest')
    '''Manifest of the experiment'''

    experiment_type = sgqlc.types.Field(ExperimentType, graphql_name='experimentType')
    '''Type of the experiment'''

    cron_syntax = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cronSyntax')
    '''Cron syntax of the experiment schedule'''

    experiment_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentName')
    '''Name of the experiment'''

    experiment_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentDescription')
    '''Description of the experiment'''

    weightages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WeightagesInput'))),
                                   graphql_name='weightages')
    '''Array containing weightage and name of each chaos experiment in
    the experiment
    '''

    is_custom_experiment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCustomExperiment')
    '''Bool value indicating whether the experiment is a custom
    experiment or not
    '''

    infra_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='infraID')
    '''ID of the target infra in which the experiment will run'''

    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    '''Tags of the infra'''


class ChaosHubFilterInput(sgqlc.types.Input):
    '''Defines filter options for ChaosHub'''
    __schema__ = chaos
    __field_names__ = ('chaos_hub_name', 'tags', 'description')
    chaos_hub_name = sgqlc.types.Field(String, graphql_name='chaosHubName')
    '''Name of the ChaosHub'''

    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    '''Tags of a chaos hub'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Description of a chaos hub'''


class CloningInput(sgqlc.types.Input):
    __schema__ = chaos
    __field_names__ = (
        'name', 'repo_branch', 'repo_url', 'is_private', 'auth_type', 'token', 'user_name', 'password',
        'ssh_private_key',
        'is_default')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Name of the chaos hub'''

    repo_branch = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repoBranch')
    '''Branch of the git repository'''

    repo_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repoURL')
    '''URL of the git repository'''

    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    '''Bool value indicating whether the hub is private or not.'''

    auth_type = sgqlc.types.Field(sgqlc.types.non_null(AuthType), graphql_name='authType')
    '''Type of authentication used:    BASIC, SSH,     TOKEN'''

    token = sgqlc.types.Field(String, graphql_name='token')
    '''Token for authentication of private chaos hub'''

    user_name = sgqlc.types.Field(String, graphql_name='userName')
    '''Git username'''

    password = sgqlc.types.Field(String, graphql_name='password')
    '''Git password'''

    ssh_private_key = sgqlc.types.Field(String, graphql_name='sshPrivateKey')

    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')


class ComparatorInput(sgqlc.types.Input):
    '''Defines the input properties of the comparator'''
    __schema__ = chaos
    __field_names__ = ('type', 'value', 'criteria')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    '''Type of the Comparator'''

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    '''Value of the Comparator'''

    criteria = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='criteria')
    '''Operator of the Comparator'''


class CreateChaosHubRequest(sgqlc.types.Input):
    '''Defines the details required for creating a chaos hub'''
    __schema__ = chaos
    __field_names__ = (
        'name', 'tags', 'description', 'repo_url', 'repo_branch', 'is_private', 'auth_type', 'token', 'user_name',
        'password', 'ssh_private_key', 'ssh_public_key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Name of the chaos hub'''

    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    '''Tags of the ChaosHub'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Description of ChaosHub'''

    repo_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repoURL')
    '''URL of the git repository'''

    repo_branch = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repoBranch')
    '''Branch of the git repository'''

    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    '''Bool value indicating whether the hub is private or not.'''

    auth_type = sgqlc.types.Field(sgqlc.types.non_null(AuthType), graphql_name='authType')
    '''Type of authentication used:    BASIC, SSH,     TOKEN'''

    token = sgqlc.types.Field(String, graphql_name='token')
    '''Token for authentication of private chaos hub'''

    user_name = sgqlc.types.Field(String, graphql_name='userName')
    '''Git username'''

    password = sgqlc.types.Field(String, graphql_name='password')
    '''Git password'''

    ssh_private_key = sgqlc.types.Field(String, graphql_name='sshPrivateKey')
    '''Private SSH key for authenticating into private chaos hub'''

    ssh_public_key = sgqlc.types.Field(String, graphql_name='sshPublicKey')
    '''Public SSH key for authenticating into private chaos hub'''


class CreateEnvironmentRequest(sgqlc.types.Input):
    __schema__ = chaos
    __field_names__ = ('environment_id', 'name', 'type', 'description', 'tags')
    environment_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='environmentID')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    type = sgqlc.types.Field(sgqlc.types.non_null(EnvironmentType), graphql_name='type')

    description = sgqlc.types.Field(String, graphql_name='description')

    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')


class CreateRemoteChaosHub(sgqlc.types.Input):
    __schema__ = chaos
    __field_names__ = ('name', 'tags', 'description', 'repo_url')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Name of the chaos hub'''

    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    '''Tags of the ChaosHub'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Description of ChaosHub'''

    repo_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repoURL')
    '''URL of the git repository'''


class DateRange(sgqlc.types.Input):
    '''Defines the start date and end date for the filtering the data'''
    __schema__ = chaos
    __field_names__ = ('start_date', 'end_date')
    start_date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='startDate')
    '''Start date'''

    end_date = sgqlc.types.Field(String, graphql_name='endDate')
    '''End date'''


class EnvironmentFilterInput(sgqlc.types.Input):
    '''Defines filter options for infras'''
    __schema__ = chaos
    __field_names__ = ('name', 'description', 'type', 'tags')
    name = sgqlc.types.Field(String, graphql_name='name')
    '''Name of the environment'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''ID of the environment'''

    type = sgqlc.types.Field(String, graphql_name='type')
    '''Type name of environment'''

    tags = sgqlc.types.Field(sgqlc.types.list_of(EnvironmentType), graphql_name='tags')
    '''Tags of an environment'''


class EnvironmentSortInput(sgqlc.types.Input):
    '''Defines sorting options for experiment'''
    __schema__ = chaos
    __field_names__ = ('field', 'ascending')
    field = sgqlc.types.Field(sgqlc.types.non_null(EnvironmentSortingField), graphql_name='field')
    '''Field in which sorting will be done'''

    ascending = sgqlc.types.Field(Boolean, graphql_name='ascending')
    '''Bool value indicating whether the sorting will be done in
    ascending order
    '''


class ExperimentFilterInput(sgqlc.types.Input):
    '''Defines filter options for experiments'''
    __schema__ = chaos
    __field_names__ = (
        'experiment_name', 'infra_name', 'infra_id', 'infra_active', 'schedule_type', 'status', 'date_range',
        'infra_types')
    experiment_name = sgqlc.types.Field(String, graphql_name='experimentName')
    '''Name of the experiment'''

    infra_name = sgqlc.types.Field(String, graphql_name='infraName')
    '''Name of the infra in which the experiment is running'''

    infra_id = sgqlc.types.Field(String, graphql_name='infraID')
    '''ID of the infra in which the experiment is running'''

    infra_active = sgqlc.types.Field(Boolean, graphql_name='infraActive')
    '''Bool value indicating if Chaos Infrastructure is active'''

    schedule_type = sgqlc.types.Field(ScheduleType, graphql_name='scheduleType')
    '''Scenario type of the experiment i.e. CRON or NON_CRON'''

    status = sgqlc.types.Field(String, graphql_name='status')
    '''Status of the latest experiment run'''

    date_range = sgqlc.types.Field(DateRange, graphql_name='dateRange')
    '''Date range for filtering purpose'''

    infra_types = sgqlc.types.Field(sgqlc.types.list_of(InfrastructureType), graphql_name='infraTypes')
    '''Type of infras'''


class ExperimentRequest(sgqlc.types.Input):
    __schema__ = chaos
    __field_names__ = ('category', 'experiment_name', 'hub_id')
    category = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='category')
    '''Name of the chart being used'''

    experiment_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentName')
    '''Name of the experiment'''

    hub_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='hubID')
    '''ID of the hub'''


class ExperimentRunFilterInput(sgqlc.types.Input):
    '''Defines input type for experiment run filter'''
    __schema__ = chaos
    __field_names__ = (
        'experiment_name', 'infra_id', 'experiment_type', 'experiment_status', 'date_range', 'experiment_run_id',
        'experiment_run_status', 'infra_types')
    experiment_name = sgqlc.types.Field(String, graphql_name='experimentName')
    '''Name of the experiment'''

    infra_id = sgqlc.types.Field(String, graphql_name='infraID')
    '''Name of the infra infra'''

    experiment_type = sgqlc.types.Field(ScheduleType, graphql_name='experimentType')
    '''Type of the experiment'''

    experiment_status = sgqlc.types.Field(ExperimentRunStatus, graphql_name='experimentStatus')
    '''Status of the experiment run'''

    date_range = sgqlc.types.Field(DateRange, graphql_name='dateRange')
    '''Date range for filtering purpose'''

    experiment_run_id = sgqlc.types.Field(String, graphql_name='experimentRunID')
    '''ID of experiment run'''

    experiment_run_status = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='experimentRunStatus')
    '''Array of experiment run status'''

    infra_types = sgqlc.types.Field(sgqlc.types.list_of(InfrastructureType), graphql_name='infraTypes')
    '''Type of infras'''


class ExperimentRunRequest(sgqlc.types.Input):
    '''Defines the details for a experiment run'''
    __schema__ = chaos
    __field_names__ = (
        'experiment_id', 'notify_id', 'experiment_run_id', 'experiment_name', 'execution_data', 'infra_id',
        'revision_id',
        'completed', 'is_removed', 'updated_by')
    experiment_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentID')
    '''ID of the experiment'''

    notify_id = sgqlc.types.Field(String, graphql_name='notifyID')
    '''notifyID is required to give an ack for non cron experiment
    execution
    '''

    experiment_run_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentRunID')
    '''ID of the experiment run which is to be queried'''

    experiment_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentName')
    '''Name of the experiment'''

    execution_data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='executionData')
    '''Stores all the experiment run details related to the nodes of DAG
    graph and chaos results of the experiments
    '''

    infra_id = sgqlc.types.Field(sgqlc.types.non_null('InfraIdentity'), graphql_name='infraID')
    '''ID of the infra infra in which the experiment is running'''

    revision_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='revisionID')
    '''ID of the revision which consists manifest details'''

    completed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='completed')
    '''Bool value indicating if the experiment run has completed'''

    is_removed = sgqlc.types.Field(Boolean, graphql_name='isRemoved')
    '''Bool value indicating if the experiment run has removed'''

    updated_by = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='updatedBy')
    '''User who has updated the experiment'''


class ExperimentRunSortInput(sgqlc.types.Input):
    '''Defines sorting options for experiment runs'''
    __schema__ = chaos
    __field_names__ = ('field', 'ascending')
    field = sgqlc.types.Field(sgqlc.types.non_null(ExperimentSortingField), graphql_name='field')
    '''Field in which sorting will be done'''

    ascending = sgqlc.types.Field(Boolean, graphql_name='ascending')
    '''Bool value indicating whether the sorting will be done in
    ascending order
    '''


class ExperimentSortInput(sgqlc.types.Input):
    '''Defines sorting options for experiment'''
    __schema__ = chaos
    __field_names__ = ('field', 'ascending')
    field = sgqlc.types.Field(sgqlc.types.non_null(ExperimentSortingField), graphql_name='field')
    '''Field in which sorting will be done'''

    ascending = sgqlc.types.Field(Boolean, graphql_name='ascending')
    '''Bool value indicating whether the sorting will be done in
    ascending order
    '''


class GETRequest(sgqlc.types.Input):
    '''Details for input of GET request'''
    __schema__ = chaos
    __field_names__ = ('criteria', 'response_code')
    criteria = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='criteria')
    '''Criteria of the request'''

    response_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='responseCode')
    '''Response Code of the request'''


class GetProbeYAMLRequest(sgqlc.types.Input):
    '''Defines the input requests for GetProbeYAML query'''
    __schema__ = chaos
    __field_names__ = ('probe_name', 'mode')
    probe_name = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='probeName')
    '''Probe name of the probe'''

    mode = sgqlc.types.Field(sgqlc.types.non_null(Mode), graphql_name='mode')
    '''Mode of the Probe (SoT, EoT, Edge, Continuous or OnChaos)'''


class GitConfig(sgqlc.types.Input):
    '''Details of setting a Git repository'''
    __schema__ = chaos
    __field_names__ = ('branch', 'repo_url', 'auth_type', 'token', 'user_name', 'password', 'ssh_private_key')
    branch = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='branch')
    '''Git branch where the chaos charts will be pushed and synced'''

    repo_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repoURL')
    '''URL of the Git repository'''

    auth_type = sgqlc.types.Field(sgqlc.types.non_null(AuthType), graphql_name='authType')
    '''Type of authentication used:    BASIC, SSH,     TOKEN'''

    token = sgqlc.types.Field(String, graphql_name='token')
    '''Token used for private repository'''

    user_name = sgqlc.types.Field(String, graphql_name='userName')
    '''Git username'''

    password = sgqlc.types.Field(String, graphql_name='password')
    '''Git password'''

    ssh_private_key = sgqlc.types.Field(String, graphql_name='sshPrivateKey')
    '''Private SSH key authenticating into git repository'''


class HTTPProbeRequest(sgqlc.types.Input):
    '''Defines the input for HTTP probe properties'''
    __schema__ = chaos
    __field_names__ = (
        'probe_timeout', 'interval', 'retry', 'attempt', 'probe_polling_interval', 'initial_delay',
        'evaluation_timeout',
        'stop_on_failure', 'url', 'method', 'insecure_skip_verify')
    probe_timeout = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='probeTimeout')
    '''Timeout of the Probe'''

    interval = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='interval')
    '''Interval of the Probe'''

    retry = sgqlc.types.Field(Int, graphql_name='retry')
    '''Retry interval of the Probe'''

    attempt = sgqlc.types.Field(Int, graphql_name='attempt')
    '''Attempt contains the total attempt count for the probe'''

    probe_polling_interval = sgqlc.types.Field(String, graphql_name='probePollingInterval')
    '''Polling interval of the Probe'''

    initial_delay = sgqlc.types.Field(String, graphql_name='initialDelay')
    '''Initial delay interval of the Probe in seconds'''

    evaluation_timeout = sgqlc.types.Field(String, graphql_name='evaluationTimeout')
    '''EvaluationTimeout is the timeout window in which the SLO metrics'''

    stop_on_failure = sgqlc.types.Field(Boolean, graphql_name='stopOnFailure')
    '''Is stop on failure enabled in the Probe'''

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    '''URL of the Probe'''

    method = sgqlc.types.Field(sgqlc.types.non_null('MethodRequest'), graphql_name='method')
    '''HTTP method of the Probe'''

    insecure_skip_verify = sgqlc.types.Field(Boolean, graphql_name='insecureSkipVerify')
    '''If Insecure HTTP verification should  be skipped'''


class ImageRegistryInput(sgqlc.types.Input):
    '''Defines input data for querying the details of an image registry'''
    __schema__ = chaos
    __field_names__ = (
        'is_default', 'image_registry_name', 'image_repo_name', 'image_registry_type', 'secret_name',
        'secret_namespace',
        'enable_registry')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    '''Bool value indicating if the image registry is default or not; by
    default workflow uses LitmusChaos registry
    '''

    image_registry_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='imageRegistryName')
    '''Name of Image Registry'''

    image_repo_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='imageRepoName')
    '''Name of image repository'''

    image_registry_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='imageRegistryType')
    '''Type of the image registry: public/private'''

    secret_name = sgqlc.types.Field(String, graphql_name='secretName')
    '''Secret which is used for private registry'''

    secret_namespace = sgqlc.types.Field(String, graphql_name='secretNamespace')
    '''Namespace where the secret is available'''

    enable_registry = sgqlc.types.Field(Boolean, graphql_name='enableRegistry')
    '''Bool value indicating if image registry is enabled or not'''


class InfraFilterInput(sgqlc.types.Input):
    '''Defines filter options for infras'''
    __schema__ = chaos
    __field_names__ = ('name', 'infra_id', 'description', 'platform_name', 'infra_scope', 'is_active', 'tags')
    name = sgqlc.types.Field(String, graphql_name='name')
    '''Name of the infra'''

    infra_id = sgqlc.types.Field(String, graphql_name='infraID')
    '''ID of the infra'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''ID of the infra'''

    platform_name = sgqlc.types.Field(String, graphql_name='platformName')
    '''Platform name of infra'''

    infra_scope = sgqlc.types.Field(INFRA_SCOPE, graphql_name='infraScope')
    '''Scope of infra'''

    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    '''Status of infra'''

    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')
    '''Tags of an infra'''


class InfraIdentity(sgqlc.types.Input):
    __schema__ = chaos
    __field_names__ = ('infra_id', 'access_key', 'version')
    infra_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='infraID')

    access_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accessKey')

    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='version')


class K8SProbeRequest(sgqlc.types.Input):
    '''Defines the input for K8S probe properties'''
    __schema__ = chaos
    __field_names__ = (
        'probe_timeout', 'interval', 'retry', 'attempt', 'probe_polling_interval', 'initial_delay',
        'evaluation_timeout',
        'stop_on_failure', 'group', 'version', 'resource', 'namespace', 'resource_names', 'field_selector',
        'label_selector', 'operation')
    probe_timeout = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='probeTimeout')
    '''Timeout of the Probe'''

    interval = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='interval')
    '''Interval of the Probe'''

    retry = sgqlc.types.Field(Int, graphql_name='retry')
    '''Retry interval of the Probe'''

    attempt = sgqlc.types.Field(Int, graphql_name='attempt')
    '''Attempt contains the total attempt count for the probe'''

    probe_polling_interval = sgqlc.types.Field(String, graphql_name='probePollingInterval')
    '''Polling interval of the Probe'''

    initial_delay = sgqlc.types.Field(String, graphql_name='initialDelay')
    '''Initial delay interval of the Probe in seconds'''

    evaluation_timeout = sgqlc.types.Field(String, graphql_name='evaluationTimeout')
    '''EvaluationTimeout is the timeout window in which the SLO metrics'''

    stop_on_failure = sgqlc.types.Field(Boolean, graphql_name='stopOnFailure')
    '''Is stop on failure enabled in the Probe'''

    group = sgqlc.types.Field(String, graphql_name='group')
    '''Group of the Probe'''

    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='version')
    '''Version of the Probe'''

    resource = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resource')
    '''Resource of the Probe'''

    namespace = sgqlc.types.Field(String, graphql_name='namespace')
    '''Namespace of the Probe'''

    resource_names = sgqlc.types.Field(String, graphql_name='resourceNames')
    '''Resource Names of the Probe'''

    field_selector = sgqlc.types.Field(String, graphql_name='fieldSelector')
    '''Field Selector of the Probe'''

    label_selector = sgqlc.types.Field(String, graphql_name='labelSelector')
    '''Label Selector of the Probe'''

    operation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='operation')
    '''Operation of the Probe'''


class KubeGVRRequest(sgqlc.types.Input):
    __schema__ = chaos
    __field_names__ = ('group', 'version', 'resource')
    group = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='group')

    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='version')

    resource = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resource')


class KubeObjectData(sgqlc.types.Input):
    '''Defines the details of Kubernetes object'''
    __schema__ = chaos
    __field_names__ = ('request_id', 'infra_id', 'kube_obj')
    request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='requestID')
    '''Unique request ID for fetching Kubernetes object details'''

    infra_id = sgqlc.types.Field(sgqlc.types.non_null(InfraIdentity), graphql_name='infraID')
    '''ID of the infra in which the Kubernetes object is present'''

    kube_obj = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='kubeObj')
    '''Type of the Kubernetes object'''


class KubeObjectRequest(sgqlc.types.Input):
    '''Defines details for fetching Kubernetes object data'''
    __schema__ = chaos
    __field_names__ = ('infra_id', 'kube_obj_request', 'object_type', 'workloads')
    infra_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='infraID')
    '''ID of the infra in which the Kubernetes object is present'''

    kube_obj_request = sgqlc.types.Field(KubeGVRRequest, graphql_name='kubeObjRequest')
    '''GVR Request'''

    object_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectType')

    workloads = sgqlc.types.Field(sgqlc.types.list_of('Workload'), graphql_name='workloads')


class KubernetesCMDProbeRequest(sgqlc.types.Input):
    '''Defines the input for Kubernetes CMD probe properties'''
    __schema__ = chaos
    __field_names__ = (
        'probe_timeout', 'interval', 'retry', 'attempt', 'probe_polling_interval', 'initial_delay',
        'evaluation_timeout',
        'stop_on_failure', 'command', 'comparator', 'source')
    probe_timeout = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='probeTimeout')
    '''Timeout of the Probe'''

    interval = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='interval')
    '''Interval of the Probe'''

    retry = sgqlc.types.Field(Int, graphql_name='retry')
    '''Retry interval of the Probe'''

    attempt = sgqlc.types.Field(Int, graphql_name='attempt')
    '''Attempt contains the total attempt count for the probe'''

    probe_polling_interval = sgqlc.types.Field(String, graphql_name='probePollingInterval')
    '''Polling interval of the Probe'''

    initial_delay = sgqlc.types.Field(String, graphql_name='initialDelay')
    '''Initial delay interval of the Probe in seconds'''

    evaluation_timeout = sgqlc.types.Field(String, graphql_name='evaluationTimeout')
    '''EvaluationTimeout is the timeout window in which the SLO metrics'''

    stop_on_failure = sgqlc.types.Field(Boolean, graphql_name='stopOnFailure')
    '''Is stop on failure enabled in the Probe'''

    command = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='command')
    '''Command of the Probe'''

    comparator = sgqlc.types.Field(sgqlc.types.non_null(ComparatorInput), graphql_name='comparator')
    '''Comparator of the Probe'''

    source = sgqlc.types.Field(String, graphql_name='source')
    '''Source of the Probe'''


class KubernetesHTTPProbeRequest(sgqlc.types.Input):
    '''Defines the input for Kubernetes HTTP probe properties'''
    __schema__ = chaos
    __field_names__ = (
        'probe_timeout', 'interval', 'retry', 'attempt', 'probe_polling_interval', 'initial_delay',
        'evaluation_timeout',
        'stop_on_failure', 'url', 'method', 'insecure_skip_verify')
    probe_timeout = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='probeTimeout')
    '''Timeout of the Probe'''

    interval = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='interval')
    '''Interval of the Probe'''

    retry = sgqlc.types.Field(Int, graphql_name='retry')
    '''Retry interval of the Probe'''

    attempt = sgqlc.types.Field(Int, graphql_name='attempt')
    '''Attempt contains the total attempt count for the probe'''

    probe_polling_interval = sgqlc.types.Field(String, graphql_name='probePollingInterval')
    '''Polling interval of the Probe'''

    initial_delay = sgqlc.types.Field(String, graphql_name='initialDelay')
    '''Initial delay interval of the Probe in seconds'''

    evaluation_timeout = sgqlc.types.Field(String, graphql_name='evaluationTimeout')
    '''EvaluationTimeout is the timeout window in which the SLO metrics'''

    stop_on_failure = sgqlc.types.Field(Boolean, graphql_name='stopOnFailure')
    '''Is stop on failure enabled in the Probe'''

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    '''URL of the Probe'''

    method = sgqlc.types.Field(sgqlc.types.non_null('MethodRequest'), graphql_name='method')
    '''HTTP method of the Probe'''

    insecure_skip_verify = sgqlc.types.Field(Boolean, graphql_name='insecureSkipVerify')
    '''If Insecure HTTP verification should  be skipped'''


class ListChaosHubRequest(sgqlc.types.Input):
    __schema__ = chaos
    __field_names__ = ('chaos_hub_ids', 'filter')
    chaos_hub_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='chaosHubIDs')
    '''Array of ChaosHub IDs for which details will be fetched'''

    filter = sgqlc.types.Field(ChaosHubFilterInput, graphql_name='filter')
    '''Details for fetching filtered data'''


class ListEnvironmentRequest(sgqlc.types.Input):
    __schema__ = chaos
    __field_names__ = ('environment_ids', 'pagination', 'filter', 'sort')
    environment_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='environmentIDs')
    '''Environment ID'''

    pagination = sgqlc.types.Field('Pagination', graphql_name='pagination')
    '''Details for fetching paginated data'''

    filter = sgqlc.types.Field(EnvironmentFilterInput, graphql_name='filter')
    '''Details for fetching filtered data'''

    sort = sgqlc.types.Field(EnvironmentSortInput, graphql_name='sort')
    '''Details for fetching sorted data'''


class ListExperimentRequest(sgqlc.types.Input):
    '''Defines the details for a experiment'''
    __schema__ = chaos
    __field_names__ = ('experiment_ids', 'pagination', 'sort', 'filter')
    experiment_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='experimentIDs')
    '''Array of experiment IDs for which details will be fetched'''

    pagination = sgqlc.types.Field('Pagination', graphql_name='pagination')
    '''Details for fetching paginated data'''

    sort = sgqlc.types.Field(ExperimentSortInput, graphql_name='sort')
    '''Details for fetching sorted data'''

    filter = sgqlc.types.Field(ExperimentFilterInput, graphql_name='filter')
    '''Details for fetching filtered data'''


class ListExperimentRunRequest(sgqlc.types.Input):
    '''Defines the details for experiment runs'''
    __schema__ = chaos
    __field_names__ = ('experiment_run_ids', 'experiment_ids', 'pagination', 'sort', 'filter')
    experiment_run_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='experimentRunIDs')
    '''Array of experiment run IDs for which details will be fetched'''

    experiment_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='experimentIDs')
    '''Array of experiment IDs for which details will be fetched'''

    pagination = sgqlc.types.Field('Pagination', graphql_name='pagination')
    '''Details for fetching paginated data'''

    sort = sgqlc.types.Field(ExperimentRunSortInput, graphql_name='sort')
    '''Details for fetching sorted data'''

    filter = sgqlc.types.Field(ExperimentRunFilterInput, graphql_name='filter')
    '''Details for fetching filtered data'''


class ListInfraRequest(sgqlc.types.Input):
    '''Defines the details for a infra'''
    __schema__ = chaos
    __field_names__ = ('infra_ids', 'environment_ids', 'pagination', 'filter')
    infra_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='infraIDs')
    '''Array of infra IDs for which details will be fetched'''

    environment_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='environmentIDs')
    '''Environment ID'''

    pagination = sgqlc.types.Field('Pagination', graphql_name='pagination')
    '''Details for fetching paginated data'''

    filter = sgqlc.types.Field(InfraFilterInput, graphql_name='filter')
    '''Details for fetching filtered data'''


class MethodRequest(sgqlc.types.Input):
    '''Defines the input for methods of the probe properties'''
    __schema__ = chaos
    __field_names__ = ('get', 'post')
    get = sgqlc.types.Field(GETRequest, graphql_name='get')
    '''A GET request'''

    post = sgqlc.types.Field('POSTRequest', graphql_name='post')
    '''A POST request'''


class NewInfraEventRequest(sgqlc.types.Input):
    __schema__ = chaos
    __field_names__ = ('event_name', 'description', 'infra_id', 'access_key')
    event_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='eventName')

    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')

    infra_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='infraID')

    access_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accessKey')


class POSTRequest(sgqlc.types.Input):
    '''Details for input of the POST request'''
    __schema__ = chaos
    __field_names__ = ('content_type', 'body', 'body_path', 'criteria', 'response_code')
    content_type = sgqlc.types.Field(String, graphql_name='contentType')
    '''Content Type of the request'''

    body = sgqlc.types.Field(String, graphql_name='body')
    '''Body of the request'''

    body_path = sgqlc.types.Field(String, graphql_name='bodyPath')
    '''Body Path of the request for Body'''

    criteria = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='criteria')
    '''Criteria of the request'''

    response_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='responseCode')
    '''Response Code of the request'''


class PROMProbeRequest(sgqlc.types.Input):
    '''Defines the input for PROM probe properties'''
    __schema__ = chaos
    __field_names__ = (
        'probe_timeout', 'interval', 'retry', 'attempt', 'probe_polling_interval', 'initial_delay',
        'evaluation_timeout',
        'stop_on_failure', 'endpoint', 'query', 'query_path', 'comparator')
    probe_timeout = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='probeTimeout')
    '''Timeout of the Probe'''

    interval = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='interval')
    '''Interval of the Probe'''

    retry = sgqlc.types.Field(Int, graphql_name='retry')
    '''Retry interval of the Probe'''

    attempt = sgqlc.types.Field(Int, graphql_name='attempt')
    '''Attempt contains the total attempt count for the probe'''

    probe_polling_interval = sgqlc.types.Field(String, graphql_name='probePollingInterval')
    '''Polling interval of the Probe'''

    initial_delay = sgqlc.types.Field(String, graphql_name='initialDelay')
    '''Initial delay interval of the Probe in seconds'''

    evaluation_timeout = sgqlc.types.Field(String, graphql_name='evaluationTimeout')
    '''EvaluationTimeout is the timeout window in which the SLO metrics'''

    stop_on_failure = sgqlc.types.Field(Boolean, graphql_name='stopOnFailure')
    '''Is stop on failure enabled in the Probe'''

    endpoint = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='endpoint')
    '''Endpoint of the Probe'''

    query = sgqlc.types.Field(String, graphql_name='query')
    '''Query of the Probe'''

    query_path = sgqlc.types.Field(String, graphql_name='queryPath')
    '''Query path of the Probe'''

    comparator = sgqlc.types.Field(sgqlc.types.non_null(ComparatorInput), graphql_name='comparator')
    '''Comparator of the Probe'''


class Pagination(sgqlc.types.Input):
    '''Defines data required to fetch paginated data'''
    __schema__ = chaos
    __field_names__ = ('page', 'limit')
    page = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='page')
    '''Page number for which data will be fetched'''

    limit = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='limit')
    '''Number of data to be fetched'''


class PodLog(sgqlc.types.Input):
    '''Response received for querying pod logs'''
    __schema__ = chaos
    __field_names__ = ('infra_id', 'request_id', 'experiment_run_id', 'pod_name', 'pod_type', 'log')
    infra_id = sgqlc.types.Field(sgqlc.types.non_null(InfraIdentity), graphql_name='infraID')
    '''ID of the cluster'''

    request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='requestID')
    '''Unique request ID of a particular node which is being queried'''

    experiment_run_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='experimentRunID')
    '''ID of a experiment run'''

    pod_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='podName')
    '''Name of the pod for which logs are required'''

    pod_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='podType')
    '''Type of the pod: chaosengine'''

    log = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='log')
    '''Logs for the pod'''


class PodLogRequest(sgqlc.types.Input):
    '''Defines the details for fetching the pod logs'''
    __schema__ = chaos
    __field_names__ = (
        'infra_id', 'experiment_run_id', 'pod_name', 'pod_namespace', 'pod_type', 'exp_pod', 'runner_pod',
        'chaos_namespace')
    infra_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='infraID')
    '''ID of the cluster'''

    experiment_run_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='experimentRunID')
    '''ID of a experiment run'''

    pod_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='podName')
    '''Name of the pod for which logs are required'''

    pod_namespace = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='podNamespace')
    '''Namespace where the pod is running'''

    pod_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='podType')
    '''Type of the pod: chaosEngine or not pod'''

    exp_pod = sgqlc.types.Field(String, graphql_name='expPod')
    '''Name of the experiment pod fetched from execution data'''

    runner_pod = sgqlc.types.Field(String, graphql_name='runnerPod')
    '''Name of the runner pod fetched from execution data'''

    chaos_namespace = sgqlc.types.Field(String, graphql_name='chaosNamespace')
    '''Namespace where the experiment is executing'''


class ProbeFilterInput(sgqlc.types.Input):
    '''Defines the input for Probe filter'''
    __schema__ = chaos
    __field_names__ = ('name', 'date_range', 'type')
    name = sgqlc.types.Field(String, graphql_name='name')
    '''Name of the Probe'''

    date_range = sgqlc.types.Field(DateRange, graphql_name='dateRange')
    '''Date range for filtering purpose'''

    type = sgqlc.types.Field(sgqlc.types.list_of(ProbeType), graphql_name='type')
    '''Type of the Probe [From list of ProbeType enum]'''


class ProbeRequest(sgqlc.types.Input):
    '''Defines the details required for creating a Chaos Probe'''
    __schema__ = chaos
    __field_names__ = ('name', 'description', 'tags', 'type', 'infrastructure_type', 'kubernetes_httpproperties',
                       'kubernetes_cmdproperties', 'k8s_properties', 'prom_properties')
    name = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='name')
    '''Name of the Probe'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Description of the Probe'''

    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    '''Tags of the Probe'''

    type = sgqlc.types.Field(sgqlc.types.non_null(ProbeType), graphql_name='type')
    '''Type of the Probe [From list of ProbeType enum]'''

    infrastructure_type = sgqlc.types.Field(sgqlc.types.non_null(InfrastructureType), graphql_name='infrastructureType')
    '''Infrastructure type of the Probe'''

    kubernetes_httpproperties = sgqlc.types.Field(KubernetesHTTPProbeRequest, graphql_name='kubernetesHTTPProperties')
    '''HTTP Properties of the specific type of the Probe'''

    kubernetes_cmdproperties = sgqlc.types.Field(KubernetesCMDProbeRequest, graphql_name='kubernetesCMDProperties')
    '''CMD Properties of the specific type of the Probe'''

    k8s_properties = sgqlc.types.Field(K8SProbeRequest, graphql_name='k8sProperties')
    '''K8S Properties of the specific type of the Probe'''

    prom_properties = sgqlc.types.Field(PROMProbeRequest, graphql_name='promProperties')
    '''PROM Properties of the specific type of the Probe'''


class RegisterInfraRequest(sgqlc.types.Input):
    '''Defines the details for the new infra being connected'''
    __schema__ = chaos
    __field_names__ = (
        'name', 'environment_id', 'infrastructure_type', 'description', 'platform_name', 'infra_namespace',
        'service_account', 'infra_scope', 'infra_ns_exists', 'infra_sa_exists', 'skip_ssl', 'node_selector',
        'tolerations',
        'tags')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Name of the infra'''

    environment_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='environmentID')
    '''Environment ID for the infra'''

    infrastructure_type = sgqlc.types.Field(sgqlc.types.non_null(InfrastructureType), graphql_name='infrastructureType')
    '''Type of Infra : internal/external'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Description of the infra'''

    platform_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='platformName')
    '''Infra Platform Name eg. GKE,AWS, Others'''

    infra_namespace = sgqlc.types.Field(String, graphql_name='infraNamespace')
    '''Namespace where the infra is being installed'''

    service_account = sgqlc.types.Field(String, graphql_name='serviceAccount')
    '''Name of service account used by infra'''

    infra_scope = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='infraScope')
    '''Scope of the infra : ns or infra'''

    infra_ns_exists = sgqlc.types.Field(Boolean, graphql_name='infraNsExists')
    '''Bool value indicating whether infra ns used already exists on
    infra or not
    '''

    infra_sa_exists = sgqlc.types.Field(Boolean, graphql_name='infraSaExists')
    '''Bool value indicating whether service account used already exists
    on infra or not
    '''

    skip_ssl = sgqlc.types.Field(Boolean, graphql_name='skipSsl')
    '''Bool value indicating whether infra will skip ssl checks or not'''

    node_selector = sgqlc.types.Field(String, graphql_name='nodeSelector')
    '''Node selectors used by infra'''

    tolerations = sgqlc.types.Field(sgqlc.types.list_of('Toleration'), graphql_name='tolerations')
    '''Node tolerations used by infra'''

    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    '''Tags of the infra'''


class SaveChaosExperimentRequest(sgqlc.types.Input):
    '''Defines the details for a chaos experiment'''
    __schema__ = chaos
    __field_names__ = ('id', 'type', 'name', 'description', 'manifest', 'infra_id', 'tags')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    '''ID of the experiment'''

    type = sgqlc.types.Field(ExperimentType, graphql_name='type')
    '''Type of the experiment'''

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Name of the experiment'''

    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    '''Description of the experiment'''

    manifest = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='manifest')
    '''Manifest of the experiment'''

    infra_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='infraID')
    '''ID of the target infrastructure in which the experiment will run'''

    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    '''Tags of the infrastructure'''


class Toleration(sgqlc.types.Input):
    __schema__ = chaos
    __field_names__ = ('toleration_seconds', 'key', 'operator', 'effect', 'value')
    toleration_seconds = sgqlc.types.Field(Int, graphql_name='tolerationSeconds')

    key = sgqlc.types.Field(String, graphql_name='key')

    operator = sgqlc.types.Field(String, graphql_name='operator')

    effect = sgqlc.types.Field(String, graphql_name='effect')

    value = sgqlc.types.Field(String, graphql_name='value')


class UpdateChaosHubRequest(sgqlc.types.Input):
    __schema__ = chaos
    __field_names__ = (
        'id', 'name', 'description', 'tags', 'repo_url', 'repo_branch', 'is_private', 'auth_type', 'token', 'user_name',
        'password', 'ssh_private_key', 'ssh_public_key')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    '''ID of the chaos hub'''

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Name of the chaos hub'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Description of the infra'''

    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    '''Tags of the infra'''

    repo_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repoURL')
    '''URL of the git repository'''

    repo_branch = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repoBranch')
    '''Branch of the git repository'''

    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    '''Bool value indicating whether the hub is private or not.'''

    auth_type = sgqlc.types.Field(sgqlc.types.non_null(AuthType), graphql_name='authType')
    '''Type of authentication used:    BASIC, SSH,     TOKEN'''

    token = sgqlc.types.Field(String, graphql_name='token')
    '''Token for authentication of private chaos hub'''

    user_name = sgqlc.types.Field(String, graphql_name='userName')
    '''Git username'''

    password = sgqlc.types.Field(String, graphql_name='password')
    '''Git password'''

    ssh_private_key = sgqlc.types.Field(String, graphql_name='sshPrivateKey')
    '''Private SSH key for authenticating into private chaos hub'''

    ssh_public_key = sgqlc.types.Field(String, graphql_name='sshPublicKey')
    '''Public SSH key for authenticating into private chaos hub'''


class UpdateEnvironmentRequest(sgqlc.types.Input):
    __schema__ = chaos
    __field_names__ = ('environment_id', 'name', 'description', 'tags', 'type')
    environment_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='environmentID')

    name = sgqlc.types.Field(String, graphql_name='name')

    description = sgqlc.types.Field(String, graphql_name='description')

    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')

    type = sgqlc.types.Field(EnvironmentType, graphql_name='type')


class WeightagesInput(sgqlc.types.Input):
    '''Defines the details of the weightages of each chaos fault in the
    experiment
    '''
    __schema__ = chaos
    __field_names__ = ('fault_name', 'weightage')
    fault_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='faultName')
    '''Name of the fault'''

    weightage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='weightage')
    '''Weightage of the fault'''


class Workload(sgqlc.types.Input):
    __schema__ = chaos
    __field_names__ = ('name', 'kind', 'namespace')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    kind = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='kind')

    namespace = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='namespace')


########################################################################
# Output Objects and Interfaces
########################################################################
class Audit(sgqlc.types.Interface):
    __schema__ = chaos
    __field_names__ = ('updated_at', 'created_at', 'updated_by', 'created_by')
    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')

    created_at = sgqlc.types.Field(String, graphql_name='createdAt')

    updated_by = sgqlc.types.Field('UserDetails', graphql_name='updatedBy')

    created_by = sgqlc.types.Field('UserDetails', graphql_name='createdBy')


class CommonProbeProperties(sgqlc.types.Interface):
    '''Defines the common probe properties shared across different
    ProbeTypes
    '''
    __schema__ = chaos
    __field_names__ = (
        'probe_timeout', 'interval', 'retry', 'attempt', 'probe_polling_interval', 'initial_delay',
        'evaluation_timeout',
        'stop_on_failure')
    probe_timeout = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='probeTimeout')
    '''Timeout of the Probe'''

    interval = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='interval')
    '''Interval of the Probe'''

    retry = sgqlc.types.Field(Int, graphql_name='retry')
    '''Retry interval of the Probe'''

    attempt = sgqlc.types.Field(Int, graphql_name='attempt')
    '''Attempt contains the total attempt count for the probe'''

    probe_polling_interval = sgqlc.types.Field(String, graphql_name='probePollingInterval')
    '''Polling interval of the Probe'''

    initial_delay = sgqlc.types.Field(String, graphql_name='initialDelay')
    '''Initial delay interval of the Probe in seconds'''

    evaluation_timeout = sgqlc.types.Field(String, graphql_name='evaluationTimeout')
    '''EvaluationTimeout is the timeout window in which the SLO metrics'''

    stop_on_failure = sgqlc.types.Field(Boolean, graphql_name='stopOnFailure')
    '''Is stop on failure enabled in the Probe'''


class ResourceDetails(sgqlc.types.Interface):
    __schema__ = chaos
    __field_names__ = ('name', 'description', 'tags')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    description = sgqlc.types.Field(String, graphql_name='description')

    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')


class ActionPayload(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('request_id', 'request_type', 'k8s_manifest', 'namespace', 'external_data', 'username')
    request_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='requestID')

    request_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='requestType')

    k8s_manifest = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='k8sManifest')

    namespace = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='namespace')

    external_data = sgqlc.types.Field(String, graphql_name='externalData')

    username = sgqlc.types.Field(String, graphql_name='username')


class Annotation(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('categories', 'vendor', 'created_at', 'repository', 'support', 'chart_description')
    categories = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='categories')

    vendor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vendor')

    created_at = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createdAt')

    repository = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repository')

    support = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='support')

    chart_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='chartDescription')


class ChaosExperimentResponse(sgqlc.types.Type):
    '''Defines the response received for querying the details of chaos
    experiment
    '''
    __schema__ = chaos
    __field_names__ = (
        'experiment_id', 'project_id', 'cron_syntax', 'experiment_name', 'experiment_description',
        'is_custom_experiment',
        'tags')
    experiment_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentID')
    '''ID of the experiment'''

    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectID')

    cron_syntax = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cronSyntax')
    '''Cron syntax of the experiment schedule'''

    experiment_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentName')
    '''Name of the experiment'''

    experiment_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentDescription')
    '''Description of the experiment'''

    is_custom_experiment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCustomExperiment')
    '''Bool value indicating whether the experiment is a custom
    experiment or not
    '''

    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    '''Tags of the infra'''


class Chart(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('api_version', 'kind', 'metadata', 'spec', 'package_info')
    api_version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='apiVersion')

    kind = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='kind')

    metadata = sgqlc.types.Field(sgqlc.types.non_null('Metadata'), graphql_name='metadata')

    spec = sgqlc.types.Field(sgqlc.types.non_null('Spec'), graphql_name='spec')

    package_info = sgqlc.types.Field(sgqlc.types.non_null('PackageInformation'), graphql_name='packageInfo')


class Comparator(sgqlc.types.Type):
    '''Defines the properties of the comparator'''
    __schema__ = chaos
    __field_names__ = ('type', 'value', 'criteria')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    '''Type of the Comparator'''

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    '''Value of the Comparator'''

    criteria = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='criteria')
    '''Operator of the Comparator'''


class ConfirmInfraRegistrationResponse(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('is_infra_confirmed', 'new_access_key', 'infra_id')
    is_infra_confirmed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isInfraConfirmed')

    new_access_key = sgqlc.types.Field(String, graphql_name='newAccessKey')

    infra_id = sgqlc.types.Field(String, graphql_name='infraID')


class ExecutedByExperiment(sgqlc.types.Type):
    '''Defines the Executed by which experiment details for Probes'''
    __schema__ = chaos
    __field_names__ = ('experiment_id', 'experiment_name', 'updated_at', 'updated_by')
    experiment_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentID')
    '''Experiment ID'''

    experiment_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentName')
    '''Experiment Name'''

    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='updatedAt')
    '''Timestamp at which the experiment was last updated'''

    updated_by = sgqlc.types.Field('UserDetails', graphql_name='updatedBy')
    '''User who has updated the experiment'''


class ExecutionHistory(sgqlc.types.Type):
    '''Defines the Execution History of experiment referenced by the
    Probe
    '''
    __schema__ = chaos
    __field_names__ = ('mode', 'fault_name', 'status', 'executed_by_experiment')
    mode = sgqlc.types.Field(sgqlc.types.non_null(Mode), graphql_name='mode')
    '''Probe Mode'''

    fault_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='faultName')
    '''Fault Name'''

    status = sgqlc.types.Field(sgqlc.types.non_null('Status'), graphql_name='status')
    '''Fault Status'''

    executed_by_experiment = sgqlc.types.Field(sgqlc.types.non_null(ExecutedByExperiment),
                                               graphql_name='executedByExperiment')
    '''Fault executed by which experiment'''


class ExperimentDetails(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('engine_details', 'experiment_details')
    engine_details = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='engineDetails')
    '''Engine Manifest'''

    experiment_details = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentDetails')
    '''Experiment Manifest'''


class Experiments(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('name', 'csv', 'desc')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    csv = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='CSV')

    desc = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='desc')


class FaultDetails(sgqlc.types.Type):
    '''Fault Detail consists of all the fault related details'''
    __schema__ = chaos
    __field_names__ = ('fault', 'engine', 'csv')
    fault = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fault')
    '''fault consists of fault.yaml'''

    engine = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='engine')
    '''engine consists engine.yaml'''

    csv = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='csv')
    '''csv consists chartserviceversion.yaml'''


class FaultList(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('name', 'display_name', 'description', 'plan')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')

    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')

    plan = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='plan')


class GET(sgqlc.types.Type):
    '''Details of GET request'''
    __schema__ = chaos
    __field_names__ = ('criteria', 'response_code')
    criteria = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='criteria')
    '''Criteria of the request'''

    response_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='responseCode')
    '''Response Code of the request'''


class GetChaosHubStatsResponse(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('total_chaos_hubs',)
    total_chaos_hubs = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalChaosHubs')
    '''Total number of chaoshubs'''


class GetExperimentResponse(sgqlc.types.Type):
    '''Defines the details for a given experiment with some additional
    data
    '''
    __schema__ = chaos
    __field_names__ = ('experiment_details', 'average_resiliency_score')
    experiment_details = sgqlc.types.Field(sgqlc.types.non_null('Experiment'), graphql_name='experimentDetails')
    '''Details of experiment'''

    average_resiliency_score = sgqlc.types.Field(Float, graphql_name='averageResiliencyScore')
    '''Average resiliency score of the experiment'''


class GetExperimentRunStatsResponse(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('total_experiment_runs', 'total_completed_experiment_runs', 'total_terminated_experiment_runs',
                       'total_running_experiment_runs', 'total_stopped_experiment_runs',
                       'total_errored_experiment_runs')
    total_experiment_runs = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalExperimentRuns')
    '''Total number of experiment runs'''

    total_completed_experiment_runs = sgqlc.types.Field(sgqlc.types.non_null(Int),
                                                        graphql_name='totalCompletedExperimentRuns')
    '''Total number of completed experiments runs'''

    total_terminated_experiment_runs = sgqlc.types.Field(sgqlc.types.non_null(Int),
                                                         graphql_name='totalTerminatedExperimentRuns')
    '''Total number of stopped experiment runs'''

    total_running_experiment_runs = sgqlc.types.Field(sgqlc.types.non_null(Int),
                                                      graphql_name='totalRunningExperimentRuns')
    '''Total number of running experiment runs'''

    total_stopped_experiment_runs = sgqlc.types.Field(sgqlc.types.non_null(Int),
                                                      graphql_name='totalStoppedExperimentRuns')
    '''Total number of stopped experiment runs'''

    total_errored_experiment_runs = sgqlc.types.Field(sgqlc.types.non_null(Int),
                                                      graphql_name='totalErroredExperimentRuns')
    '''Total number of errored experiment runs'''


class GetExperimentStatsResponse(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('total_experiments', 'total_exp_categorized_by_resiliency_score')
    total_experiments = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalExperiments')
    '''Total number of experiments'''

    total_exp_categorized_by_resiliency_score = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of('ResilienceScoreCategory')),
        graphql_name='totalExpCategorizedByResiliencyScore')
    '''Total number of cron experiments'''


class GetInfraStatsResponse(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('total_infrastructures', 'total_active_infrastructure', 'total_inactive_infrastructures',
                       'total_confirmed_infrastructure', 'total_non_confirmed_infrastructures')
    total_infrastructures = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalInfrastructures')
    '''Total number of infrastructures'''

    total_active_infrastructure = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalActiveInfrastructure')
    '''Total number of active infrastructures'''

    total_inactive_infrastructures = sgqlc.types.Field(sgqlc.types.non_null(Int),
                                                       graphql_name='totalInactiveInfrastructures')
    '''Total number of inactive infrastructures'''

    total_confirmed_infrastructure = sgqlc.types.Field(sgqlc.types.non_null(Int),
                                                       graphql_name='totalConfirmedInfrastructure')
    '''Total number of confirmed infrastructures'''

    total_non_confirmed_infrastructures = sgqlc.types.Field(sgqlc.types.non_null(Int),
                                                            graphql_name='totalNonConfirmedInfrastructures')
    '''Total number of non confirmed infrastructures'''


class GetProbeReferenceResponse(sgqlc.types.Type):
    '''Defines the response of the Probe reference API'''
    __schema__ = chaos
    __field_names__ = ('project_id', 'name', 'total_runs', 'recent_executions')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectID')
    '''Harness identifiers'''

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Name of the Probe'''

    total_runs = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRuns')
    '''Total Runs'''

    recent_executions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('RecentExecutions')),
                                          graphql_name='recentExecutions')
    '''Recent Executions of the probe'''


class GetProbesInExperimentRunResponse(sgqlc.types.Type):
    '''Defines the response for Get Probe In Experiment Run Query'''
    __schema__ = chaos
    __field_names__ = ('probe', 'mode', 'status')
    probe = sgqlc.types.Field(sgqlc.types.non_null('Probe'), graphql_name='probe')
    '''Probe Object'''

    mode = sgqlc.types.Field(sgqlc.types.non_null(Mode), graphql_name='mode')
    '''Mode of the probe'''

    status = sgqlc.types.Field(sgqlc.types.non_null('Status'), graphql_name='status')
    '''Status of the Probe'''


class GitConfigResponse(sgqlc.types.Type):
    '''Response received after configuring GitOps'''
    __schema__ = chaos
    __field_names__ = (
        'enabled', 'project_id', 'branch', 'repo_url', 'auth_type', 'token', 'user_name', 'password', 'ssh_private_key')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    '''Bool value indicating whether GitOps is enabled or not'''

    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectID')
    '''ID of the project where GitOps is configured'''

    branch = sgqlc.types.Field(String, graphql_name='branch')
    '''Git branch where the chaos charts will be pushed and synced'''

    repo_url = sgqlc.types.Field(String, graphql_name='repoURL')
    '''URL of the Git repository'''

    auth_type = sgqlc.types.Field(AuthType, graphql_name='authType')
    '''Type of authentication used:    BASIC, SSH,     TOKEN'''

    token = sgqlc.types.Field(String, graphql_name='token')
    '''Token used for private repository'''

    user_name = sgqlc.types.Field(String, graphql_name='userName')
    '''Git username'''

    password = sgqlc.types.Field(String, graphql_name='password')
    '''Git password'''

    ssh_private_key = sgqlc.types.Field(String, graphql_name='sshPrivateKey')
    '''Private SSH key authenticating into git repository'''


class ImageRegistry(sgqlc.types.Type):
    '''Defines details for image registry'''
    __schema__ = chaos
    __field_names__ = (
        'is_default', 'image_registry_name', 'image_repo_name', 'image_registry_type', 'secret_name',
        'secret_namespace',
        'enable_registry')
    is_default = sgqlc.types.Field(Boolean, graphql_name='isDefault')
    '''Bool value indicating if the image registry is default or not; by
    default workflow uses LitmusChaos registry
    '''

    image_registry_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='imageRegistryName')
    '''Name of Image Registry'''

    image_repo_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='imageRepoName')
    '''Name of image repository'''

    image_registry_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='imageRegistryType')
    '''Type of the image registry: public/private'''

    secret_name = sgqlc.types.Field(String, graphql_name='secretName')
    '''Secret which is used for private registry'''

    secret_namespace = sgqlc.types.Field(String, graphql_name='secretNamespace')
    '''Namespace where the secret is available'''

    enable_registry = sgqlc.types.Field(Boolean, graphql_name='enableRegistry')
    '''Bool value indicating if image registry is enabled or not'''


class InfraActionResponse(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('project_id', 'action')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectID')

    action = sgqlc.types.Field(sgqlc.types.non_null(ActionPayload), graphql_name='action')


class InfraEventResponse(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('event_id', 'event_type', 'event_name', 'description', 'infra')
    event_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='eventID')

    event_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='eventType')

    event_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='eventName')

    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')

    infra = sgqlc.types.Field(sgqlc.types.non_null('Infra'), graphql_name='infra')


class InfraVersionDetails(sgqlc.types.Type):
    """InfraVersionDetails returns the details of compatible infra
    versions and the latest infra version supported
    """
    __schema__ = chaos
    __field_names__ = ('latest_version', 'compatible_versions')
    latest_version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='latestVersion')
    '''Latest infra version supported'''

    compatible_versions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
                                            graphql_name='compatibleVersions')
    '''List of all infra versions supported'''


class KubeObject(sgqlc.types.Type):
    """KubeObject consists of the namespace and the available resources
    in the same
    """
    __schema__ = chaos
    __field_names__ = ('namespace', 'data')
    namespace = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='namespace')
    '''Namespace of the resource'''

    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ObjectData')), graphql_name='data')
    '''Details of the resource'''


class KubeObjectResponse(sgqlc.types.Type):
    """Response received for querying Kubernetes Object"""
    __schema__ = chaos
    __field_names__ = ('infra_id', 'kube_obj')
    infra_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='infraID')
    '''ID of the infra in which the Kubernetes object is present'''

    kube_obj = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(KubeObject)), graphql_name='kubeObj')
    '''Type of the Kubernetes object'''


class Link(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('name', 'url')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class ListEnvironmentResponse(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('total_no_of_environments', 'environments')
    total_no_of_environments = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalNoOfEnvironments')
    '''Total number of environment'''

    environments = sgqlc.types.Field(sgqlc.types.list_of('Environment'), graphql_name='environments')


class ListExperimentResponse(sgqlc.types.Type):
    """Defines the details for a experiment with total experiment count"""
    __schema__ = chaos
    __field_names__ = ('total_no_of_experiments', 'experiments')
    total_no_of_experiments = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalNoOfExperiments')
    '''Total number of experiments'''

    experiments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Experiment')), graphql_name='experiments')
    '''Details related to the experiments'''


class ListExperimentRunResponse(sgqlc.types.Type):
    """Defines the details of a experiment to sent as response"""
    __schema__ = chaos
    __field_names__ = ('total_no_of_experiment_runs', 'experiment_runs')
    total_no_of_experiment_runs = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalNoOfExperimentRuns')
    '''Total number of experiment runs'''

    experiment_runs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ExperimentRun')),
                                        graphql_name='experimentRuns')
    '''Defines details of experiment runs'''


class ListInfraResponse(sgqlc.types.Type):
    """Defines the details for a infras with total infras count"""
    __schema__ = chaos
    __field_names__ = ('total_no_of_infras', 'infras')
    total_no_of_infras = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalNoOfInfras')
    '''Total number of infras'''

    infras = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Infra')), graphql_name='infras')
    '''Details related to the infras'''


class Maintainer(sgqlc.types.Type):
    """Defines the details of the maintainer"""
    __schema__ = chaos
    __field_names__ = ('name', 'email')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Name of the maintainer'''

    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    '''Email of the maintainer'''


class Metadata(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('name', 'version', 'annotations')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='version')

    annotations = sgqlc.types.Field(sgqlc.types.non_null(Annotation), graphql_name='annotations')


class Method(sgqlc.types.Type):
    '''Defines the methods of the probe properties'''
    __schema__ = chaos
    __field_names__ = ('get', 'post')
    get = sgqlc.types.Field(GET, graphql_name='get')
    '''A GET request'''

    post = sgqlc.types.Field('POST', graphql_name='post')
    '''A POST request'''


class Mutation(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = (
        'create_chaos_experiment', 'save_chaos_experiment', 'update_chaos_experiment', 'delete_chaos_experiment',
        'update_cron_experiment_state', 'chaos_experiment_run', 'run_chaos_experiment', 'stop_experiment_runs',
        'register_infra', 'confirm_infra_registration', 'delete_infra', 'get_manifest_with_infra_id', 'pod_log',
        'kube_obj',
        'add_chaos_hub', 'add_remote_chaos_hub', 'save_chaos_hub', 'sync_chaos_hub', 'generate_sshkey',
        'update_chaos_hub',
        'delete_chaos_hub', 'create_environment', 'update_environment', 'delete_environment', 'gitops_notifier',
        'enable_git_ops', 'disable_git_ops', 'update_git_ops', 'create_image_registry', 'update_image_registry',
        'delete_image_registry', 'add_probe', 'update_probe', 'delete_probe')
    create_chaos_experiment = sgqlc.types.Field(sgqlc.types.non_null(ChaosExperimentResponse),
                                                graphql_name='createChaosExperiment', args=sgqlc.types.ArgDict((
            ('request',
             sgqlc.types.Arg(sgqlc.types.non_null(ChaosExperimentRequest), graphql_name='request', default=None)),
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
        ))
                                                )
    '''Creates a new experiment and applies its manifest

    Arguments:

    * `request` (`ChaosExperimentRequest!`)
    * `project_id` (`ID!`)
    '''

    save_chaos_experiment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='saveChaosExperiment',
                                              args=sgqlc.types.ArgDict((
                                                  ('request',
                                                   sgqlc.types.Arg(sgqlc.types.non_null(SaveChaosExperimentRequest),
                                                                   graphql_name='request', default=None)),
                                                  ('project_id',
                                                   sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                                   default=None)),
                                              ))
                                              )
    '''Saves a new experiment or updates if already exists

    Arguments:

    * `request` (`SaveChaosExperimentRequest!`)
    * `project_id` (`ID!`)
    '''

    update_chaos_experiment = sgqlc.types.Field(sgqlc.types.non_null(ChaosExperimentResponse),
                                                graphql_name='updateChaosExperiment', args=sgqlc.types.ArgDict((
            ('request', sgqlc.types.Arg(ChaosExperimentRequest, graphql_name='request', default=None)),
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
        ))
                                                )
    '''Updates the experiment

    Arguments:

    * `request` (`ChaosExperimentRequest`)
    * `project_id` (`ID!`)
    '''

    delete_chaos_experiment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteChaosExperiment',
                                                args=sgqlc.types.ArgDict((
                                                    ('experiment_id', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                      graphql_name='experimentID',
                                                                                      default=None)),
                                                    ('experiment_run_id',
                                                     sgqlc.types.Arg(String, graphql_name='experimentRunID',
                                                                     default=None)),
                                                    ('project_id',
                                                     sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                                     default=None)),
                                                ))
                                                )
    '''Removes a experiment from infra

    Arguments:

    * `experiment_id` (`String!`)
    * `experiment_run_id` (`String`)
    * `project_id` (`ID!`)
    '''

    update_cron_experiment_state = sgqlc.types.Field(sgqlc.types.non_null(Boolean),
                                                     graphql_name='updateCronExperimentState',
                                                     args=sgqlc.types.ArgDict((
                                                         ('experiment_id', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                           graphql_name='experimentID',
                                                                                           default=None)),
                                                         ('disable', sgqlc.types.Arg(sgqlc.types.non_null(Boolean),
                                                                                     graphql_name='disable',
                                                                                     default=None)),
                                                         ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID),
                                                                                        graphql_name='projectID',
                                                                                        default=None)),
                                                     ))
                                                     )
    '''Enable/Disable cron experiment state

    Arguments:

    * `experiment_id` (`String!`)
    * `disable` (`Boolean!`)
    * `project_id` (`ID!`)
    '''

    chaos_experiment_run = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='chaosExperimentRun',
                                             args=sgqlc.types.ArgDict((
                                                 ('request', sgqlc.types.Arg(sgqlc.types.non_null(ExperimentRunRequest),
                                                                             graphql_name='request', default=None)),
                                             ))
                                             )
    '''Creates a new experiment run and sends it to subscriber

    Arguments:

    * `request` (`ExperimentRunRequest!`)
    '''

    run_chaos_experiment = sgqlc.types.Field(sgqlc.types.non_null('RunChaosExperimentResponse'),
                                             graphql_name='runChaosExperiment', args=sgqlc.types.ArgDict((
            ('experiment_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='experimentID', default=None)),
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
        ))
                                             )
    '''Run the chaos experiment (used by frontend)

    Arguments:

    * `experiment_id` (`String!`)
    * `project_id` (`ID!`)
    '''

    stop_experiment_runs = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='stopExperimentRuns',
                                             args=sgqlc.types.ArgDict((
                                                 ('project_id',
                                                  sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                                  default=None)),
                                                 ('experiment_id', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                   graphql_name='experimentID',
                                                                                   default=None)),
                                                 ('experiment_run_id',
                                                  sgqlc.types.Arg(String, graphql_name='experimentRunID',
                                                                  default=None)),
                                                 ('notify_id',
                                                  sgqlc.types.Arg(String, graphql_name='notifyID', default=None)),
                                             ))
                                             )
    '''stopExperiment will halt all the ongoing runs of a particular
    experiment

    Arguments:

    * `project_id` (`ID!`)
    * `experiment_id` (`String!`)
    * `experiment_run_id` (`String`)
    * `notify_id` (`String`)
    '''

    register_infra = sgqlc.types.Field(sgqlc.types.non_null('RegisterInfraResponse'), graphql_name='registerInfra',
                                       args=sgqlc.types.ArgDict((
                                           ('project_id',
                                            sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                            default=None)),
                                           ('request', sgqlc.types.Arg(sgqlc.types.non_null(RegisterInfraRequest),
                                                                       graphql_name='request', default=None)),
                                       ))
                                       )
    '''Connect a new infra for a user in a specified project

    Arguments:

    * `project_id` (`ID!`)
    * `request` (`RegisterInfraRequest!`)
    '''

    confirm_infra_registration = sgqlc.types.Field(sgqlc.types.non_null(ConfirmInfraRegistrationResponse),
                                                   graphql_name='confirmInfraRegistration', args=sgqlc.types.ArgDict((
            ('request', sgqlc.types.Arg(sgqlc.types.non_null(InfraIdentity), graphql_name='request', default=None)),
        ))
                                                   )
    '''Confirms the subscriber's registration with the control plane

    Arguments:

    * `request` (`InfraIdentity!`)
    '''

    delete_infra = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteInfra',
                                     args=sgqlc.types.ArgDict((
                                         ('project_id',
                                          sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                          default=None)),
                                         ('infra_id',
                                          sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='infraID',
                                                          default=None)),
                                     ))
                                     )
    '''Disconnects an infra and deletes its configuration from the
    control plane

    Arguments:

    * `project_id` (`ID!`)
    * `infra_id` (`String!`)
    '''

    get_manifest_with_infra_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='getManifestWithInfraID',
                                                   args=sgqlc.types.ArgDict((
                                                       ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID),
                                                                                      graphql_name='projectID',
                                                                                      default=None)),
                                                       ('infra_id', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                    graphql_name='infraID',
                                                                                    default=None)),
                                                       ('access_key', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                      graphql_name='accessKey',
                                                                                      default=None)),
                                                   ))
                                                   )
    '''Fetches manifest details

    Arguments:

    * `project_id` (`ID!`)
    * `infra_id` (`String!`)
    * `access_key` (`String!`)
    '''

    pod_log = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='podLog', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(PodLog), graphql_name='request', default=None)),
    ))
                                )
    '''Receives pod logs for experiments from infra

    Arguments:

    * `request` (`PodLog!`)
    '''

    kube_obj = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='kubeObj', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(KubeObjectData), graphql_name='request', default=None)),
    ))
                                 )
    '''Receives kubernetes object data from subscriber

    Arguments:

    * `request` (`KubeObjectData!`)
    '''

    add_chaos_hub = sgqlc.types.Field(sgqlc.types.non_null('ChaosHub'), graphql_name='addChaosHub',
                                      args=sgqlc.types.ArgDict((
                                          ('project_id',
                                           sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                           default=None)),
                                          ('request', sgqlc.types.Arg(sgqlc.types.non_null(CreateChaosHubRequest),
                                                                      graphql_name='request', default=None)),
                                      ))
                                      )
    '''Add a ChaosHub (includes the git clone operation)

    Arguments:

    * `project_id` (`ID!`)
    * `request` (`CreateChaosHubRequest!`)
    '''

    add_remote_chaos_hub = sgqlc.types.Field(sgqlc.types.non_null('ChaosHub'), graphql_name='addRemoteChaosHub',
                                             args=sgqlc.types.ArgDict((
                                                 ('project_id',
                                                  sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                                  default=None)),
                                                 ('request', sgqlc.types.Arg(sgqlc.types.non_null(CreateRemoteChaosHub),
                                                                             graphql_name='request', default=None)),
                                             ))
                                             )
    '''Add a ChaosHub (remote hub download)

    Arguments:

    * `project_id` (`ID!`)
    * `request` (`CreateRemoteChaosHub!`)
    '''

    save_chaos_hub = sgqlc.types.Field(sgqlc.types.non_null('ChaosHub'), graphql_name='saveChaosHub',
                                       args=sgqlc.types.ArgDict((
                                           ('project_id',
                                            sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                            default=None)),
                                           ('request', sgqlc.types.Arg(sgqlc.types.non_null(CreateChaosHubRequest),
                                                                       graphql_name='request', default=None)),
                                       ))
                                       )
    '''Save a ChaosHub configuration without cloning it

    Arguments:

    * `project_id` (`ID!`)
    * `request` (`CreateChaosHubRequest!`)
    '''

    sync_chaos_hub = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='syncChaosHub',
                                       args=sgqlc.types.ArgDict((
                                           ('id',
                                            sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
                                           ('project_id',
                                            sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                            default=None)),
                                       ))
                                       )
    '''Sync changes from the Git repository of a ChaosHub

    Arguments:

    * `id` (`ID!`)
    * `project_id` (`ID!`)
    '''

    generate_sshkey = sgqlc.types.Field(sgqlc.types.non_null('SSHKey'), graphql_name='generateSSHKey')
    '''Generates Private and Public key for SSH authentication'''

    update_chaos_hub = sgqlc.types.Field(sgqlc.types.non_null('ChaosHub'), graphql_name='updateChaosHub',
                                         args=sgqlc.types.ArgDict((
                                             ('project_id',
                                              sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                              default=None)),
                                             ('request', sgqlc.types.Arg(sgqlc.types.non_null(UpdateChaosHubRequest),
                                                                         graphql_name='request', default=None)),
                                         ))
                                         )
    '''Update the configuration of a ChaosHub

    Arguments:

    * `project_id` (`ID!`)
    * `request` (`UpdateChaosHubRequest!`)
    '''

    delete_chaos_hub = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteChaosHub',
                                         args=sgqlc.types.ArgDict((
                                             ('project_id',
                                              sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                              default=None)),
                                             ('hub_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='hubID',
                                                                        default=None)),
                                         ))
                                         )
    '''Delete the ChaosHub

    Arguments:

    * `project_id` (`ID!`)
    * `hub_id` (`ID!`)
    '''

    create_environment = sgqlc.types.Field('Environment', graphql_name='createEnvironment', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
        ('request', sgqlc.types.Arg(CreateEnvironmentRequest, graphql_name='request', default=None)),
    ))
                                           )
    '''Arguments:

    * `project_id` (`ID!`)
    * `request` (`CreateEnvironmentRequest`)
    '''

    update_environment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='updateEnvironment',
                                           args=sgqlc.types.ArgDict((
                                               ('project_id',
                                                sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                                default=None)),
                                               ('request',
                                                sgqlc.types.Arg(UpdateEnvironmentRequest, graphql_name='request',
                                                                default=None)),
                                           ))
                                           )
    '''Arguments:

    * `project_id` (`ID!`)
    * `request` (`UpdateEnvironmentRequest`)
    '''

    delete_environment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteEnvironment',
                                           args=sgqlc.types.ArgDict((
                                               ('project_id',
                                                sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                                default=None)),
                                               ('environment_id',
                                                sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='environmentID',
                                                                default=None)),
                                           ))
                                           )
    '''Arguments:

    * `project_id` (`ID!`)
    * `environment_id` (`ID!`)
    '''

    gitops_notifier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='gitopsNotifier',
                                        args=sgqlc.types.ArgDict((
                                            ('cluster_info', sgqlc.types.Arg(sgqlc.types.non_null(InfraIdentity),
                                                                             graphql_name='clusterInfo', default=None)),
                                            ('experiment_id',
                                             sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='experimentID',
                                                             default=None)),
                                        ))
                                        )
    '''Sends workflow run request(single run workflow only) to agent on
    gitops notification

    Arguments:

    * `cluster_info` (`InfraIdentity!`)
    * `experiment_id` (`ID!`)
    '''

    enable_git_ops = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enableGitOps',
                                       args=sgqlc.types.ArgDict((
                                           ('project_id',
                                            sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                            default=None)),
                                           ('configurations', sgqlc.types.Arg(sgqlc.types.non_null(GitConfig),
                                                                              graphql_name='configurations',
                                                                              default=None)),
                                       ))
                                       )
    '''Enables gitops settings in the project

    Arguments:

    * `project_id` (`ID!`)
    * `configurations` (`GitConfig!`)
    '''

    disable_git_ops = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='disableGitOps',
                                        args=sgqlc.types.ArgDict((
                                            ('project_id',
                                             sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                             default=None)),
                                        ))
                                        )
    '''Disables gitops settings in the project

    Arguments:

    * `project_id` (`ID!`)
    '''

    update_git_ops = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateGitOps',
                                       args=sgqlc.types.ArgDict((
                                           ('project_id',
                                            sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                            default=None)),
                                           ('configurations', sgqlc.types.Arg(sgqlc.types.non_null(GitConfig),
                                                                              graphql_name='configurations',
                                                                              default=None)),
                                       ))
                                       )
    '''Updates gitops settings in the project

    Arguments:

    * `project_id` (`ID!`)
    * `configurations` (`GitConfig!`)
    '''

    create_image_registry = sgqlc.types.Field(sgqlc.types.non_null('ImageRegistryResponse'),
                                              graphql_name='createImageRegistry', args=sgqlc.types.ArgDict((
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='projectID', default=None)),
            ('image_registry_info',
             sgqlc.types.Arg(sgqlc.types.non_null(ImageRegistryInput), graphql_name='imageRegistryInfo', default=None)),
        ))
                                              )
    '''Create an Image Registry configuration

    Arguments:

    * `project_id` (`String!`)
    * `image_registry_info` (`ImageRegistryInput!`)
    '''

    update_image_registry = sgqlc.types.Field(sgqlc.types.non_null('ImageRegistryResponse'),
                                              graphql_name='updateImageRegistry', args=sgqlc.types.ArgDict((
            ('image_registry_id',
             sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='imageRegistryID', default=None)),
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='projectID', default=None)),
            ('image_registry_info',
             sgqlc.types.Arg(sgqlc.types.non_null(ImageRegistryInput), graphql_name='imageRegistryInfo', default=None)),
        ))
                                              )
    '''Update the Image Registry configuration

    Arguments:

    * `image_registry_id` (`String!`)
    * `project_id` (`String!`)
    * `image_registry_info` (`ImageRegistryInput!`)
    '''

    delete_image_registry = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deleteImageRegistry',
                                              args=sgqlc.types.ArgDict((
                                                  ('image_registry_id', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                        graphql_name='imageRegistryID',
                                                                                        default=None)),
                                                  ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(String),
                                                                                 graphql_name='projectID',
                                                                                 default=None)),
                                              ))
                                              )
    '''Delete the Image Registry

    Arguments:

    * `image_registry_id` (`String!`)
    * `project_id` (`String!`)
    '''

    add_probe = sgqlc.types.Field(sgqlc.types.non_null('Probe'), graphql_name='addProbe', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(ProbeRequest), graphql_name='request', default=None)),
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
    ))
                                  )
    '''Creates a new Probe

    Arguments:

    * `request` (`ProbeRequest!`)
    * `project_id` (`ID!`)
    '''

    update_probe = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='updateProbe',
                                     args=sgqlc.types.ArgDict((
                                         ('request',
                                          sgqlc.types.Arg(sgqlc.types.non_null(ProbeRequest), graphql_name='request',
                                                          default=None)),
                                         ('project_id',
                                          sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                          default=None)),
                                     ))
                                     )
    '''Update the configuration of a Probe

    Arguments:

    * `request` (`ProbeRequest!`)
    * `project_id` (`ID!`)
    '''

    delete_probe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteProbe',
                                     args=sgqlc.types.ArgDict((
                                         ('probe_name',
                                          sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='probeName',
                                                          default=None)),
                                         ('project_id',
                                          sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                          default=None)),
                                     ))
                                     )
    '''Delete a Probe

    Arguments:

    * `probe_name` (`ID!`)
    * `project_id` (`ID!`)
    '''


class ObjectData(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('labels', 'name')
    labels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels')
    '''Labels present in the resource'''

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Name of the resource'''


class POST(sgqlc.types.Type):
    '''Details of POST request'''
    __schema__ = chaos
    __field_names__ = ('content_type', 'body', 'body_path', 'criteria', 'response_code')
    content_type = sgqlc.types.Field(String, graphql_name='contentType')
    '''Content Type of the request'''

    body = sgqlc.types.Field(String, graphql_name='body')
    '''Body of the request'''

    body_path = sgqlc.types.Field(String, graphql_name='bodyPath')
    '''Body Path of the HTTP body required for the http post request'''

    criteria = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='criteria')
    '''Criteria of the request'''

    response_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='responseCode')
    '''Response Code of the request'''


class PackageInformation(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('package_name', 'experiments')
    package_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='packageName')

    experiments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Experiments))),
                                    graphql_name='experiments')


class PodLogResponse(sgqlc.types.Type):
    '''Defines the response received for querying querying the pod logs'''
    __schema__ = chaos
    __field_names__ = ('experiment_run_id', 'pod_name', 'pod_type', 'log')
    experiment_run_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='experimentRunID')
    '''ID of the experiment run which is to be queried'''

    pod_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='podName')
    '''Name of the pod for which logs are queried'''

    pod_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='podType')
    '''Type of the pod: chaosengine'''

    log = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='log')
    '''Logs for the pod'''


class PredefinedExperimentList(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('experiment_name', 'experiment_csv', 'experiment_manifest')
    experiment_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentName')
    '''Name of the experiment'''

    experiment_csv = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentCSV')
    '''Experiment CSV'''

    experiment_manifest = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentManifest')
    '''Experiment Manifest'''


class ProbeRecentExecutions(sgqlc.types.Type):
    '''Defines the Recent Executions of global probe in ListProbe API
    with different fault and execution history each time
    '''
    __schema__ = chaos
    __field_names__ = ('fault_name', 'status', 'executed_by_experiment')
    fault_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='faultName')
    '''Fault name'''

    status = sgqlc.types.Field(sgqlc.types.non_null('Status'), graphql_name='status')
    '''Fault Status'''

    executed_by_experiment = sgqlc.types.Field(sgqlc.types.non_null(ExecutedByExperiment),
                                               graphql_name='executedByExperiment')
    '''Fault executed by which experiment'''


class Provider(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Query(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = (
        'get_experiment', 'list_experiment', 'get_experiment_stats', 'get_experiment_run', 'list_experiment_run',
        'get_experiment_run_stats', 'get_infra', 'list_infras', 'get_infra_details', 'get_infra_manifest',
        'get_infra_stats', 'get_version_details', 'get_server_version', 'list_chaos_faults', 'get_chaos_fault',
        'list_chaos_hub', 'get_chaos_hub', 'list_predefined_experiments', 'get_predefined_experiment',
        'get_chaos_hub_stats', 'get_environment', 'list_environments', 'get_git_ops_details', 'list_image_registry',
        'get_image_registry', 'list_probes', 'get_probe', 'get_probe_yaml', 'get_probe_reference',
        'get_probes_in_experiment_run', 'validate_unique_probe')
    get_experiment = sgqlc.types.Field(sgqlc.types.non_null(GetExperimentResponse), graphql_name='getExperiment',
                                       args=sgqlc.types.ArgDict((
                                           ('project_id',
                                            sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                            default=None)),
                                           ('experiment_id',
                                            sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='experimentID',
                                                            default=None)),
                                       ))
                                       )
    '''Returns the experiment based on experiment ID

    Arguments:

    * `project_id` (`ID!`)
    * `experiment_id` (`String!`)
    '''

    list_experiment = sgqlc.types.Field(sgqlc.types.non_null(ListExperimentResponse), graphql_name='listExperiment',
                                        args=sgqlc.types.ArgDict((
                                            ('project_id',
                                             sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                             default=None)),
                                            ('request', sgqlc.types.Arg(sgqlc.types.non_null(ListExperimentRequest),
                                                                        graphql_name='request', default=None)),
                                        ))
                                        )
    '''Returns the list of experiments based on various filter parameters

    Arguments:

    * `project_id` (`ID!`)
    * `request` (`ListExperimentRequest!`)
    '''

    get_experiment_stats = sgqlc.types.Field(sgqlc.types.non_null(GetExperimentStatsResponse),
                                             graphql_name='getExperimentStats', args=sgqlc.types.ArgDict((
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
        ))
                                             )
    '''Query to get experiment stats

    Arguments:

    * `project_id` (`ID!`)
    '''

    get_experiment_run = sgqlc.types.Field(sgqlc.types.non_null('ExperimentRun'), graphql_name='getExperimentRun',
                                           args=sgqlc.types.ArgDict((
                                               ('project_id',
                                                sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                                default=None)),
                                               ('experiment_run_id',
                                                sgqlc.types.Arg(ID, graphql_name='experimentRunID', default=None)),
                                               (
                                                   'notify_id',
                                                   sgqlc.types.Arg(ID, graphql_name='notifyID', default=None)),
                                           ))
                                           )
    '''Returns experiment run based on experiment run ID

    Arguments:

    * `project_id` (`ID!`)
    * `experiment_run_id` (`ID`)
    * `notify_id` (`ID`)
    '''

    list_experiment_run = sgqlc.types.Field(sgqlc.types.non_null(ListExperimentRunResponse),
                                            graphql_name='listExperimentRun', args=sgqlc.types.ArgDict((
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
            ('request',
             sgqlc.types.Arg(sgqlc.types.non_null(ListExperimentRunRequest), graphql_name='request', default=None)),
        ))
                                            )
    '''Returns the list of experiment run based on various filter
    parameters

    Arguments:

    * `project_id` (`ID!`)
    * `request` (`ListExperimentRunRequest!`)
    '''

    get_experiment_run_stats = sgqlc.types.Field(sgqlc.types.non_null(GetExperimentRunStatsResponse),
                                                 graphql_name='getExperimentRunStats', args=sgqlc.types.ArgDict((
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
        ))
                                                 )
    '''Query to get experiment run stats

    Arguments:

    * `project_id` (`ID!`)
    '''

    get_infra = sgqlc.types.Field(sgqlc.types.non_null('Infra'), graphql_name='getInfra', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
        ('infra_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='infraID', default=None)),
    ))
                                  )
    '''Returns infra with a particular infraID in the project

    Arguments:

    * `project_id` (`ID!`)
    * `infra_id` (`String!`)
    '''

    list_infras = sgqlc.types.Field(sgqlc.types.non_null(ListInfraResponse), graphql_name='listInfras',
                                    args=sgqlc.types.ArgDict((
                                        ('project_id',
                                         sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                         default=None)),
                                        ('request',
                                         sgqlc.types.Arg(ListInfraRequest, graphql_name='request', default=None)),
                                    ))
                                    )
    '''Returns infras with a particular infra type in the project

    Arguments:

    * `project_id` (`ID!`)
    * `request` (`ListInfraRequest`)
    '''

    get_infra_details = sgqlc.types.Field(sgqlc.types.non_null('Infra'), graphql_name='getInfraDetails',
                                          args=sgqlc.types.ArgDict((
                                              ('infra_id',
                                               sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='infraID',
                                                               default=None)),
                                              ('project_id',
                                               sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                               default=None)),
                                          ))
                                          )
    '''Returns infra details based on identifiers

    Arguments:

    * `infra_id` (`ID!`)
    * `project_id` (`ID!`)
    '''

    get_infra_manifest = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='getInfraManifest',
                                           args=sgqlc.types.ArgDict((
                                               ('infra_id',
                                                sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='infraID',
                                                                default=None)),
                                               ('upgrade',
                                                sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='upgrade',
                                                                default=None)),
                                               ('project_id',
                                                sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                                default=None)),
                                           ))
                                           )
    '''Returns the manifest for a given infraID

    Arguments:

    * `infra_id` (`ID!`)
    * `upgrade` (`Boolean!`)
    * `project_id` (`ID!`)
    '''

    get_infra_stats = sgqlc.types.Field(sgqlc.types.non_null(GetInfraStatsResponse), graphql_name='getInfraStats',
                                        args=sgqlc.types.ArgDict((
                                            ('project_id',
                                             sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                             default=None)),
                                        ))
                                        )
    '''Query to get experiment stats

    Arguments:

    * `project_id` (`ID!`)
    '''

    get_version_details = sgqlc.types.Field(sgqlc.types.non_null(InfraVersionDetails), graphql_name='getVersionDetails',
                                            args=sgqlc.types.ArgDict((
                                                ('project_id',
                                                 sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                                 default=None)),
                                            ))
                                            )
    '''Query to get the latest version of infra available

    Arguments:

    * `project_id` (`ID!`)
    '''

    get_server_version = sgqlc.types.Field(sgqlc.types.non_null('ServerVersionResponse'),
                                           graphql_name='getServerVersion')
    '''Returns version of gql server'''

    list_chaos_faults = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Chart))),
                                          graphql_name='listChaosFaults', args=sgqlc.types.ArgDict((
            ('hub_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='hubID', default=None)),
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
        ))
                                          )
    '''List the Charts details of a ChaosHub

    Arguments:

    * `hub_id` (`ID!`)
    * `project_id` (`ID!`)
    '''

    get_chaos_fault = sgqlc.types.Field(sgqlc.types.non_null(FaultDetails), graphql_name='getChaosFault',
                                        args=sgqlc.types.ArgDict((
                                            ('project_id',
                                             sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                             default=None)),
                                            ('request', sgqlc.types.Arg(sgqlc.types.non_null(ExperimentRequest),
                                                                        graphql_name='request', default=None)),
                                        ))
                                        )
    '''Get the fault list from a ChaosHub

    Arguments:

    * `project_id` (`ID!`)
    * `request` (`ExperimentRequest!`)
    '''

    list_chaos_hub = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ChaosHubStatus')),
                                       graphql_name='listChaosHub', args=sgqlc.types.ArgDict((
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
            ('request', sgqlc.types.Arg(ListChaosHubRequest, graphql_name='request', default=None)),
        ))
                                       )
    '''Lists all the connected ChaosHub

    Arguments:

    * `project_id` (`ID!`)
    * `request` (`ListChaosHubRequest`)
    '''

    get_chaos_hub = sgqlc.types.Field(sgqlc.types.non_null('ChaosHubStatus'), graphql_name='getChaosHub',
                                      args=sgqlc.types.ArgDict((
                                          ('project_id',
                                           sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                           default=None)),
                                          ('chaos_hub_id',
                                           sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='chaosHubID',
                                                           default=None)),
                                      ))
                                      )
    '''Get the details of a requested ChaosHub

    Arguments:

    * `project_id` (`ID!`)
    * `chaos_hub_id` (`ID!`)
    '''

    list_predefined_experiments = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PredefinedExperimentList))),
        graphql_name='listPredefinedExperiments', args=sgqlc.types.ArgDict((
            ('hub_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='hubID', default=None)),
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
        ))
    )
    '''List the PredefinedExperiments present in the hub

    Arguments:

    * `hub_id` (`ID!`)
    * `project_id` (`ID!`)
    '''

    get_predefined_experiment = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PredefinedExperimentList))),
        graphql_name='getPredefinedExperiment', args=sgqlc.types.ArgDict((
            ('hub_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='hubID', default=None)),
            ('experiment_name', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
                                                graphql_name='experimentName', default=None)),
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
        ))
    )
    '''Returns predefined experiment details of selected experiments

    Arguments:

    * `hub_id` (`ID!`)
    * `experiment_name` (`[String!]!`)
    * `project_id` (`ID!`)
    '''

    get_chaos_hub_stats = sgqlc.types.Field(sgqlc.types.non_null(GetChaosHubStatsResponse),
                                            graphql_name='getChaosHubStats', args=sgqlc.types.ArgDict((
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
        ))
                                            )
    '''Query to get experiment stats

    Arguments:

    * `project_id` (`ID!`)
    '''

    get_environment = sgqlc.types.Field('Environment', graphql_name='getEnvironment', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
        ('environment_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='environmentID', default=None)),
    ))
                                        )
    '''Arguments:

    * `project_id` (`ID!`)
    * `environment_id` (`ID!`)
    '''

    list_environments = sgqlc.types.Field(ListEnvironmentResponse, graphql_name='listEnvironments',
                                          args=sgqlc.types.ArgDict((
                                              ('project_id',
                                               sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                               default=None)),
                                              ('request',
                                               sgqlc.types.Arg(ListEnvironmentRequest, graphql_name='request',
                                                               default=None)),
                                          ))
                                          )
    '''Arguments:

    * `project_id` (`ID!`)
    * `request` (`ListEnvironmentRequest`)
    '''

    get_git_ops_details = sgqlc.types.Field(sgqlc.types.non_null(GitConfigResponse), graphql_name='getGitOpsDetails',
                                            args=sgqlc.types.ArgDict((
                                                ('project_id',
                                                 sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                                 default=None)),
                                            ))
                                            )
    '''Returns the git configuration for gitops

    Arguments:

    * `project_id` (`ID!`)
    '''

    list_image_registry = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ImageRegistryResponse')),
                                            graphql_name='listImageRegistry', args=sgqlc.types.ArgDict((
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='projectID', default=None)),
        ))
                                            )
    '''Arguments:

    * `project_id` (`String!`)
    '''

    get_image_registry = sgqlc.types.Field(sgqlc.types.non_null('ImageRegistryResponse'),
                                           graphql_name='getImageRegistry', args=sgqlc.types.ArgDict((
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='projectID', default=None)),
        ))
                                           )
    '''Arguments:

    * `project_id` (`String!`)
    '''

    list_probes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Probe')), graphql_name='listProbes',
                                    args=sgqlc.types.ArgDict((
                                        ('project_id',
                                         sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                         default=None)),
                                        ('infrastructure_type',
                                         sgqlc.types.Arg(InfrastructureType, graphql_name='infrastructureType',
                                                         default=None)),
                                        ('probe_names', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)),
                                                                        graphql_name='probeNames', default=None)),
                                        ('filter',
                                         sgqlc.types.Arg(ProbeFilterInput, graphql_name='filter', default=None)),
                                    ))
                                    )
    '''Returns the list of Probes based on various filter parameters

    Arguments:

    * `project_id` (`ID!`)
    * `infrastructure_type` (`InfrastructureType`)
    * `probe_names` (`[ID!]`)
    * `filter` (`ProbeFilterInput`)
    '''

    get_probe = sgqlc.types.Field(sgqlc.types.non_null('Probe'), graphql_name='getProbe', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
        ('probe_name', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='probeName', default=None)),
    ))
                                  )
    '''Returns a single Probe based on ProbeName and various filter
    parameters

    Arguments:

    * `project_id` (`ID!`)
    * `probe_name` (`ID!`)
    '''

    get_probe_yaml = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='getProbeYAML',
                                       args=sgqlc.types.ArgDict((
                                           ('project_id',
                                            sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                            default=None)),
                                           ('request', sgqlc.types.Arg(sgqlc.types.non_null(GetProbeYAMLRequest),
                                                                       graphql_name='request', default=None)),
                                       ))
                                       )
    '''Returns the Probe YAML based on ProbeName which can be used in
    ChaosEngine manifest

    Arguments:

    * `project_id` (`ID!`)
    * `request` (`GetProbeYAMLRequest!`)
    '''

    get_probe_reference = sgqlc.types.Field(sgqlc.types.non_null(GetProbeReferenceResponse),
                                            graphql_name='getProbeReference', args=sgqlc.types.ArgDict((
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
            ('probe_name', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='probeName', default=None)),
        ))
                                            )
    '''Returns all the reference of the Probe based on ProbeName

    Arguments:

    * `project_id` (`ID!`)
    * `probe_name` (`ID!`)
    '''

    get_probes_in_experiment_run = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(GetProbesInExperimentRunResponse)),
        graphql_name='getProbesInExperimentRun', args=sgqlc.types.ArgDict((
            ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID', default=None)),
            ('experiment_run_id',
             sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='experimentRunID', default=None)),
            ('fault_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='faultName', default=None)),
        ))
    )
    '''Returns all the Probes attached to the requested Experiment Run

    Arguments:

    * `project_id` (`ID!`)
    * `experiment_run_id` (`String!`)
    * `fault_name` (`String!`)
    '''

    validate_unique_probe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validateUniqueProbe',
                                              args=sgqlc.types.ArgDict((
                                                  ('project_id',
                                                   sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectID',
                                                                   default=None)),
                                                  ('probe_name',
                                                   sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='probeName',
                                                                   default=None)),
                                              ))
                                              )
    '''Validates if a probe is already present, returns true if unique

    Arguments:

    * `project_id` (`ID!`)
    * `probe_name` (`ID!`)
    '''


class RecentExecutions(sgqlc.types.Type):
    '''Defines the Recent Executions of experiment referenced by the
    Probe
    '''
    __schema__ = chaos
    __field_names__ = ('fault_name', 'mode', 'execution_history')
    fault_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='faultName')
    '''Fault name'''

    mode = sgqlc.types.Field(sgqlc.types.non_null(Mode), graphql_name='mode')
    '''Probe mode'''

    execution_history = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ExecutionHistory))),
        graphql_name='executionHistory')
    '''Execution History'''


class RegisterInfraResponse(sgqlc.types.Type):
    '''Response received for registering a new infra'''
    __schema__ = chaos
    __field_names__ = ('token', 'infra_id', 'name', 'manifest')
    token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='token')
    '''Token used to verify and retrieve the infra manifest'''

    infra_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='infraID')
    '''Unique ID for the newly registered infra'''

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Infra name as sent in request'''

    manifest = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='manifest')
    '''Infra Manifest'''


class ResilienceScoreCategory(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('id', 'count')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    '''Lower bound of the range(inclusive)'''

    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    '''total experiments with avg resilience score between lower bound
    and upper bound(exclusive)
    '''


class RunChaosExperimentResponse(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('notify_id',)
    notify_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='notifyID')


class SSHKey(sgqlc.types.Type):
    '''Defines the SSHKey details'''
    __schema__ = chaos
    __field_names__ = ('public_key', 'private_key')
    public_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='publicKey')
    '''Public SSH key authenticating into git repository'''

    private_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='privateKey')
    '''Private SSH key authenticating into git repository'''


class ServerVersionResponse(sgqlc.types.Type):
    '''Response received for fetching GQL server version'''
    __schema__ = chaos
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    '''Returns server version key'''

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    '''Returns server version value'''


class Spec(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = (
        'display_name', 'category_description', 'keywords', 'maturity', 'maintainers', 'min_kube_version', 'provider',
        'links', 'faults', 'experiments', 'chaos_exp_crdlink', 'platforms', 'chaos_type')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')

    category_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='categoryDescription')

    keywords = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
                                 graphql_name='keywords')

    maturity = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='maturity')

    maintainers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Maintainer))),
                                    graphql_name='maintainers')

    min_kube_version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='minKubeVersion')

    provider = sgqlc.types.Field(sgqlc.types.non_null(Provider), graphql_name='provider')

    links = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Link))),
                              graphql_name='links')

    faults = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FaultList))),
                               graphql_name='faults')

    experiments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='experiments')

    chaos_exp_crdlink = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='chaosExpCRDLink')

    platforms = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
                                  graphql_name='platforms')

    chaos_type = sgqlc.types.Field(String, graphql_name='chaosType')


class Status(sgqlc.types.Type):
    '''Status defines whether a probe is pass or fail'''
    __schema__ = chaos
    __field_names__ = ('verdict', 'description')
    verdict = sgqlc.types.Field(sgqlc.types.non_null(ProbeVerdict), graphql_name='verdict')
    '''Verdict defines the verdict of the probe, range: Passed, Failed,
    N/A
    '''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Description defines the description of probe status'''


class StopExperimentRunsRequest(sgqlc.types.Type):
    '''Defines the request for stopping a experiment'''
    __schema__ = chaos
    __field_names__ = ('project_id', 'experiment_id', 'experiment_run_id')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectID')

    experiment_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentID')
    '''ID of the experiment to be stopped'''

    experiment_run_id = sgqlc.types.Field(String, graphql_name='experimentRunID')
    '''ID of the experiment run to be stopped'''


class Subscription(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('get_infra_events', 'infra_connect', 'get_pod_log', 'get_kube_object')
    get_infra_events = sgqlc.types.Field(sgqlc.types.non_null(InfraEventResponse), graphql_name='getInfraEvents',
                                         args=sgqlc.types.ArgDict((
                                             ('project_id',
                                              sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='projectID',
                                                              default=None)),
                                         ))
                                         )
    '''Listens infra events from the graphql server

    Arguments:

    * `project_id` (`String!`)
    '''

    infra_connect = sgqlc.types.Field(sgqlc.types.non_null(InfraActionResponse), graphql_name='infraConnect',
                                      args=sgqlc.types.ArgDict((
                                          ('request',
                                           sgqlc.types.Arg(sgqlc.types.non_null(InfraIdentity), graphql_name='request',
                                                           default=None)),
                                      ))
                                      )
    '''Listens infra operation request from the graphql server

    Arguments:

    * `request` (`InfraIdentity!`)
    '''

    get_pod_log = sgqlc.types.Field(sgqlc.types.non_null(PodLogResponse), graphql_name='getPodLog',
                                    args=sgqlc.types.ArgDict((
                                        ('request',
                                         sgqlc.types.Arg(sgqlc.types.non_null(PodLogRequest), graphql_name='request',
                                                         default=None)),
                                    ))
                                    )
    '''Returns experiment logs from the pods

    Arguments:

    * `request` (`PodLogRequest!`)
    '''

    get_kube_object = sgqlc.types.Field(sgqlc.types.non_null(KubeObjectResponse), graphql_name='getKubeObject',
                                        args=sgqlc.types.ArgDict((
                                            ('request', sgqlc.types.Arg(sgqlc.types.non_null(KubeObjectRequest),
                                                                        graphql_name='request', default=None)),
                                        ))
                                        )
    '''Returns a kubernetes object given an input

    Arguments:

    * `request` (`KubeObjectRequest!`)
    '''


class UserDetails(sgqlc.types.Type):
    __schema__ = chaos
    __field_names__ = ('user_id', 'username', 'email')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userID')

    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')

    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')


class Weightages(sgqlc.types.Type):
    '''Defines the details of the weightages of each chaos fault in the
    experiment
    '''
    __schema__ = chaos
    __field_names__ = ('fault_name', 'weightage')
    fault_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='faultName')
    '''Name of the fault'''

    weightage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='weightage')
    '''Weightage of the experiment'''


class ChaosHub(sgqlc.types.Type, ResourceDetails, Audit):
    __schema__ = chaos
    __field_names__ = (
        'id', 'repo_url', 'repo_branch', 'project_id', 'is_default', 'hub_type', 'is_private', 'auth_type', 'token',
        'user_name', 'password', 'ssh_private_key', 'is_removed', 'last_synced_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    '''ID of the chaos hub'''

    repo_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repoURL')
    '''URL of the git repository'''

    repo_branch = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repoBranch')
    '''Branch of the git repository'''

    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectID')
    '''ID of the project in which the chaos hub is present'''

    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    '''Default Hub Identifier'''

    hub_type = sgqlc.types.Field(sgqlc.types.non_null(HubType), graphql_name='hubType')
    '''Type of ChaosHub'''

    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    '''Bool value indicating whether the hub is private or not.'''

    auth_type = sgqlc.types.Field(sgqlc.types.non_null(AuthType), graphql_name='authType')
    '''Type of authentication used:    BASIC, SSH,     TOKEN'''

    token = sgqlc.types.Field(String, graphql_name='token')
    '''Token for authentication of private chaos hub'''

    user_name = sgqlc.types.Field(String, graphql_name='userName')
    '''Git username'''

    password = sgqlc.types.Field(String, graphql_name='password')
    '''Git password'''

    ssh_private_key = sgqlc.types.Field(String, graphql_name='sshPrivateKey')
    '''Private SSH key for authenticating into private chaos hub'''

    is_removed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRemoved')
    '''Bool value indicating if the chaos hub is removed'''

    last_synced_at = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastSyncedAt')
    '''Timestamp when the chaos hub was last synced'''


class ChaosHubStatus(sgqlc.types.Type, ResourceDetails, Audit):
    __schema__ = chaos
    __field_names__ = (
        'id', 'repo_url', 'repo_branch', 'is_available', 'total_faults', 'total_experiments', 'hub_type', 'is_private',
        'auth_type', 'token', 'user_name', 'password', 'is_removed', 'ssh_private_key', 'ssh_public_key',
        'last_synced_at',
        'is_default')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    '''ID of the hub'''

    repo_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repoURL')
    '''URL of the git repository'''

    repo_branch = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repoBranch')
    '''Branch of the git repository'''

    is_available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAvailable')
    '''Bool value indicating whether the hub is available or not.'''

    total_faults = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='totalFaults')
    '''Total number of experiments in the hub'''

    total_experiments = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='totalExperiments')
    '''Total experiments'''

    hub_type = sgqlc.types.Field(sgqlc.types.non_null(HubType), graphql_name='hubType')
    '''Type of ChaosHub'''

    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    '''Bool value indicating whether the hub is private or not.'''

    auth_type = sgqlc.types.Field(sgqlc.types.non_null(AuthType), graphql_name='authType')
    '''Type of authentication used:    BASIC, SSH,     TOKEN'''

    token = sgqlc.types.Field(String, graphql_name='token')
    '''Token for authentication of private chaos hub'''

    user_name = sgqlc.types.Field(String, graphql_name='userName')
    '''Git username'''

    password = sgqlc.types.Field(String, graphql_name='password')
    '''Git password'''

    is_removed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRemoved')
    '''Bool value indicating whether the hub is private or not.'''

    ssh_private_key = sgqlc.types.Field(String, graphql_name='sshPrivateKey')
    '''Private SSH key for authenticating into private chaos hub'''

    ssh_public_key = sgqlc.types.Field(String, graphql_name='sshPublicKey')
    '''Public SSH key for authenticating into private chaos hub'''

    last_synced_at = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastSyncedAt')
    '''Timestamp when the chaos hub was last synced'''

    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    '''Default Hub Identifier'''


class Environment(sgqlc.types.Type, ResourceDetails, Audit):
    __schema__ = chaos
    __field_names__ = ('project_id', 'environment_id', 'type', 'is_removed', 'infra_ids')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectID')

    environment_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='environmentID')

    type = sgqlc.types.Field(sgqlc.types.non_null(EnvironmentType), graphql_name='type')

    is_removed = sgqlc.types.Field(Boolean, graphql_name='isRemoved')

    infra_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='infraIDs')


class Experiment(sgqlc.types.Type, ResourceDetails, Audit):
    '''Defines the details for a experiment'''
    __schema__ = chaos
    __field_names__ = (
        'project_id', 'experiment_id', 'experiment_type', 'experiment_manifest', 'cron_syntax', 'weightages',
        'is_custom_experiment', 'infra', 'is_removed', 'recent_experiment_run_details')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectID')

    experiment_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentID')
    '''ID of the experiment'''

    experiment_type = sgqlc.types.Field(String, graphql_name='experimentType')
    '''Type of the experiment'''

    experiment_manifest = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentManifest')
    '''Manifest of the experiment'''

    cron_syntax = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cronSyntax')
    '''Cron syntax of the experiment schedule'''

    weightages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Weightages))),
                                   graphql_name='weightages')
    '''Array containing weightage and name of each chaos fault in the
    experiment
    '''

    is_custom_experiment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCustomExperiment')
    '''Bool value indicating whether the experiment is a custom
    experiment or not
    '''

    infra = sgqlc.types.Field('Infra', graphql_name='infra')
    '''Target infra in which the experiment will run'''

    is_removed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRemoved')
    '''Bool value indicating if the experiment has removed'''

    recent_experiment_run_details = sgqlc.types.Field(sgqlc.types.list_of('RecentExperimentRun'),
                                                      graphql_name='recentExperimentRunDetails')
    '''Array of object containing details of recent experiment runs'''


class ExperimentRun(sgqlc.types.Type, Audit):
    '''Defines the details of a experiment run'''
    __schema__ = chaos
    __field_names__ = (
        'project_id', 'experiment_run_id', 'experiment_type', 'experiment_id', 'weightages', 'infra', 'experiment_name',
        'experiment_manifest', 'phase', 'resiliency_score', 'faults_passed', 'faults_failed', 'faults_awaited',
        'faults_stopped', 'faults_na', 'total_faults', 'execution_data', 'is_removed', 'notify_id', 'run_sequence')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectID')

    experiment_run_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='experimentRunID')
    '''ID of the experiment run which is to be queried'''

    experiment_type = sgqlc.types.Field(String, graphql_name='experimentType')
    '''Type of the experiment'''

    experiment_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='experimentID')
    '''ID of the experiment'''

    weightages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Weightages))),
                                   graphql_name='weightages')
    '''Array containing weightage and name of each chaos fault in the
    experiment
    '''

    infra = sgqlc.types.Field(sgqlc.types.non_null('Infra'), graphql_name='infra')
    '''Target infra in which the experiment will run'''

    experiment_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentName')
    '''Name of the experiment'''

    experiment_manifest = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='experimentManifest')
    '''Manifest of the experiment run'''

    phase = sgqlc.types.Field(sgqlc.types.non_null(ExperimentRunStatus), graphql_name='phase')
    '''Phase of the experiment run'''

    resiliency_score = sgqlc.types.Field(Float, graphql_name='resiliencyScore')
    '''Resiliency score of the experiment'''

    faults_passed = sgqlc.types.Field(Int, graphql_name='faultsPassed')
    '''Number of faults passed'''

    faults_failed = sgqlc.types.Field(Int, graphql_name='faultsFailed')
    '''Number of faults failed'''

    faults_awaited = sgqlc.types.Field(Int, graphql_name='faultsAwaited')
    '''Number of faults awaited'''

    faults_stopped = sgqlc.types.Field(Int, graphql_name='faultsStopped')
    '''Number of faults stopped'''

    faults_na = sgqlc.types.Field(Int, graphql_name='faultsNa')
    '''Number of faults which are not available'''

    total_faults = sgqlc.types.Field(Int, graphql_name='totalFaults')
    '''Total number of faults'''

    execution_data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='executionData')
    '''Stores all the experiment run details related to the nodes of DAG
    graph and chaos results of the faults
    '''

    is_removed = sgqlc.types.Field(Boolean, graphql_name='isRemoved')
    '''Bool value indicating if the experiment run has removed'''

    notify_id = sgqlc.types.Field(ID, graphql_name='notifyID')
    '''Notify ID of the experiment run'''

    run_sequence = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='runSequence')
    '''runSequence is the sequence number of experiment run'''


class ImageRegistryResponse(sgqlc.types.Type, Audit):
    '''Defines response data for image registry'''
    __schema__ = chaos
    __field_names__ = ('is_default', 'image_registry_info', 'image_registry_id', 'project_id', 'is_removed')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    '''Bool value indicating if the image registry is default or not; by
    default workflow uses LitmusChaos registry
    '''

    image_registry_info = sgqlc.types.Field(ImageRegistry, graphql_name='imageRegistryInfo')
    '''Information Image Registry'''

    image_registry_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='imageRegistryID')
    '''ID of the image registry'''

    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectID')
    '''ID of the project in which image registry is created'''

    is_removed = sgqlc.types.Field(Boolean, graphql_name='isRemoved')
    '''Bool value indicating if the image registry has been removed'''


class Infra(sgqlc.types.Type, ResourceDetails, Audit):
    '''Defines the details for a infra'''
    __schema__ = chaos
    __field_names__ = (
        'project_id', 'infra_id', 'environment_id', 'platform_name', 'is_active', 'is_infra_confirmed', 'is_removed',
        'no_of_experiments', 'no_of_experiment_runs', 'token', 'infra_namespace', 'service_account', 'infra_scope',
        'infra_ns_exists', 'infra_sa_exists', 'last_experiment_timestamp', 'start_time', 'version', 'infra_type',
        'update_status')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectID')

    infra_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='infraID')
    '''ID of the infra'''

    environment_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='environmentID')
    '''Environment ID for the infra'''

    platform_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='platformName')
    '''Infra Platform Name eg. GKE,AWS, Others'''

    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    '''Boolean value indicating if chaos infrastructure is active or not'''

    is_infra_confirmed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isInfraConfirmed')
    '''Boolean value indicating if chaos infrastructure is confirmed or
    not
    '''

    is_removed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRemoved')
    '''Boolean value indicating if chaos infrastructure is removed or not'''

    no_of_experiments = sgqlc.types.Field(Int, graphql_name='noOfExperiments')
    '''Number of schedules created in the infra'''

    no_of_experiment_runs = sgqlc.types.Field(Int, graphql_name='noOfExperimentRuns')
    '''Number of experiments run in the infra'''

    token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='token')
    '''Token used to verify and retrieve the infra manifest'''

    infra_namespace = sgqlc.types.Field(String, graphql_name='infraNamespace')
    '''Namespace where the infra is being installed'''

    service_account = sgqlc.types.Field(String, graphql_name='serviceAccount')
    '''Name of service account used by infra'''

    infra_scope = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='infraScope')
    '''Scope of the infra : ns or cluster'''

    infra_ns_exists = sgqlc.types.Field(Boolean, graphql_name='infraNsExists')
    '''Bool value indicating whether infra ns used already exists on
    infra or not
    '''

    infra_sa_exists = sgqlc.types.Field(Boolean, graphql_name='infraSaExists')
    '''Bool value indicating whether service account used already exists
    on infra or not
    '''

    last_experiment_timestamp = sgqlc.types.Field(String, graphql_name='lastExperimentTimestamp')
    '''Timestamp of the last experiment run in the infra'''

    start_time = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='startTime')
    '''Timestamp when the infra got connected'''

    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='version')
    '''Version of the infra'''

    infra_type = sgqlc.types.Field(InfrastructureType, graphql_name='infraType')
    '''Type of the infrastructure'''

    update_status = sgqlc.types.Field(sgqlc.types.non_null(UpdateStatus), graphql_name='updateStatus')
    '''update status of infra'''


class K8SProbe(sgqlc.types.Type, CommonProbeProperties):
    '''Defines the K8S probe properties'''
    __schema__ = chaos
    __field_names__ = (
        'group', 'version', 'resource', 'namespace', 'resource_names', 'field_selector', 'label_selector', 'operation')
    group = sgqlc.types.Field(String, graphql_name='group')
    '''Group of the Probe'''

    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='version')
    '''Version of the Probe'''

    resource = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resource')
    '''Resource of the Probe'''

    namespace = sgqlc.types.Field(String, graphql_name='namespace')
    '''Namespace of the Probe'''

    resource_names = sgqlc.types.Field(String, graphql_name='resourceNames')
    '''Resource Names of the Probe'''

    field_selector = sgqlc.types.Field(String, graphql_name='fieldSelector')
    '''Field Selector of the Probe'''

    label_selector = sgqlc.types.Field(String, graphql_name='labelSelector')
    '''Label Selector of the Probe'''

    operation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='operation')
    '''Operation of the Probe'''


class KubernetesCMDProbe(sgqlc.types.Type, CommonProbeProperties):
    '''Defines the CMD probe properties'''
    __schema__ = chaos
    __field_names__ = ('command', 'comparator', 'source')
    command = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='command')
    '''Command of the Probe'''

    comparator = sgqlc.types.Field(sgqlc.types.non_null(Comparator), graphql_name='comparator')
    '''Comparator of the Probe'''

    source = sgqlc.types.Field(String, graphql_name='source')
    '''Source of the Probe'''


class KubernetesHTTPProbe(sgqlc.types.Type, CommonProbeProperties):
    '''Defines the Kubernetes HTTP probe properties'''
    __schema__ = chaos
    __field_names__ = ('url', 'method', 'insecure_skip_verify')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    '''URL of the Probe'''

    method = sgqlc.types.Field(sgqlc.types.non_null(Method), graphql_name='method')
    '''HTTP method of the Probe'''

    insecure_skip_verify = sgqlc.types.Field(Boolean, graphql_name='insecureSkipVerify')
    '''If Insecure HTTP verification should  be skipped'''


class PROMProbe(sgqlc.types.Type, CommonProbeProperties):
    '''Defines the PROM probe properties'''
    __schema__ = chaos
    __field_names__ = ('endpoint', 'query', 'query_path', 'comparator')
    endpoint = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='endpoint')
    '''Endpoint of the Probe'''

    query = sgqlc.types.Field(String, graphql_name='query')
    '''Query of the Probe'''

    query_path = sgqlc.types.Field(String, graphql_name='queryPath')
    '''Query path of the Probe'''

    comparator = sgqlc.types.Field(sgqlc.types.non_null(Comparator), graphql_name='comparator')
    '''Comparator of the Probe'''


class Probe(sgqlc.types.Type, ResourceDetails, Audit):
    '''Defines the details of the Probe entity'''
    __schema__ = chaos
    __field_names__ = (
        'project_id', 'type', 'infrastructure_type', 'kubernetes_httpproperties', 'kubernetes_cmdproperties',
        'k8s_properties', 'prom_properties', 'recent_executions', 'referenced_by')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectID')
    '''Harness identifiers'''

    type = sgqlc.types.Field(sgqlc.types.non_null(ProbeType), graphql_name='type')
    '''Type of the Probe [From list of ProbeType enum]'''

    infrastructure_type = sgqlc.types.Field(sgqlc.types.non_null(InfrastructureType), graphql_name='infrastructureType')
    '''Infrastructure type of the Probe'''

    kubernetes_httpproperties = sgqlc.types.Field(KubernetesHTTPProbe, graphql_name='kubernetesHTTPProperties')
    '''Kubernetes HTTP Properties of the specific type of the Probe'''

    kubernetes_cmdproperties = sgqlc.types.Field(KubernetesCMDProbe, graphql_name='kubernetesCMDProperties')
    '''Kubernetes CMD Properties of the specific type of the Probe'''

    k8s_properties = sgqlc.types.Field(K8SProbe, graphql_name='k8sProperties')
    '''K8S Properties of the specific type of the Probe'''

    prom_properties = sgqlc.types.Field(PROMProbe, graphql_name='promProperties')
    '''PROM Properties of the specific type of the Probe'''

    recent_executions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProbeRecentExecutions)),
                                          graphql_name='recentExecutions')
    '''All execution histories of the probe'''

    referenced_by = sgqlc.types.Field(Int, graphql_name='referencedBy')
    '''Referenced by how many faults'''


class RecentExperimentRun(sgqlc.types.Type, Audit):
    __schema__ = chaos
    __field_names__ = ('experiment_run_id', 'phase', 'resiliency_score', 'run_sequence')
    experiment_run_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='experimentRunID')
    '''ID of the experiment run which is to be queried'''

    phase = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phase')
    '''Phase of the experiment run'''

    resiliency_score = sgqlc.types.Field(Float, graphql_name='resiliencyScore')
    '''Resiliency score of the experiment'''

    run_sequence = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='runSequence')
    '''runSequence is the sequence number of experiment run'''


########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
chaos.query_type = Query
chaos.mutation_type = Mutation
chaos.subscription_type = Subscription
