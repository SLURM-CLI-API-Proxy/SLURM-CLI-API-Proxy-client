import openapi_client
from openapi_client.models.dbv0039_job_info import Dbv0039JobInfo
from openapi_client.rest import ApiException
from pprint import pprint
import os

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://slurm-controller:6820"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['token'] = os.environ["SLURM_JWT"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    users = 'users_example' # str | Filter by comma delimited list of user names (optional)
    submit_time = 'submit_time_example' # str | Filter by submission time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    start_time = 'start_time_example' # str | Filter by start time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    end_time = 'end_time_example' # str | Filter by end time  Accepted formats:  HH:MM[:SS] [AM|PM]  MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]  MM/DD[/YY]-HH:MM[:SS]  YYYY-MM-DD[THH:MM[:SS]] (optional)
    account = 'account_example' # str | Comma delimited list of accounts to match (optional)
    association = 'association_example' # str | Comma delimited list of associations to match (optional)
    cluster = 'cluster_example' # str | Comma delimited list of cluster to match (optional)
    constraints = 'constraints_example' # str | Comma delimited list of constraints to match (optional)
    cpus_max = 'cpus_max_example' # str | Number of CPUs high range (optional)
    cpus_min = 'cpus_min_example' # str | Number of CPUs low range (optional)
    skip_steps = 'false' # str | Report job step information (optional) (default to false)
    disable_wait_for_result = 'false' # str | Disable waiting for result from slurmdbd (optional) (default to false)
    exit_code = 'exit_code_example' # str | Exit code of job (optional)
    format = 'format_example' # str | Comma delimited list of formats to match (optional)
    group = 'group_example' # str | Comma delimited list of groups to match (optional)
    job_name = 'job_name_example' # str | Comma delimited list of job names to match (optional)
    nodes_max = 'nodes_max_example' # str | Number of nodes high range (optional)
    nodes_min = 'nodes_min_example' # str | Number of nodes low range (optional)
    partition = 'partition_example' # str | Comma delimited list of partitions to match (optional)
    qos = 'qos_example' # str | Comma delimited list of QOS to match (optional)
    reason = 'reason_example' # str | Comma delimited list of job reasons to match (optional)
    reservation = 'reservation_example' # str | Comma delimited list of reservations to match (optional)
    state = 'state_example' # str | Comma delimited list of states to match (optional)
    step = 'step_example' # str | Comma delimited list of job steps to match (optional)
    node = 'node_example' # str | Comma delimited list of used nodes to match (optional)
    wckey = 'wckey_example' # str | Comma delimited list of wckeys to match (optional)

    try:
        # Get job list
        api_response = api_instance.slurmdb_v0039_get_jobs()
        print("The response of SlurmApi->slurmdb_v0039_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_jobs: %s\n" % e)