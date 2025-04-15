import os
import openapi_client
from openapi_client.models.v0039_partitions_response import V0039PartitionsResponse
from openapi_client.models.v0039_nodes_response import V0039NodesResponse
from openapi_client.rest import ApiException
from pprint import pprint

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
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get all partition info
        partitions_response:V0039PartitionsResponse = api_instance.slurm_v0039_get_partitions()

        nodes_response:V0039NodesResponse = api_instance.slurm_v0039_get_nodes()


        print("The response of SlurmApi->slurm_v0039_get_partitions:\n")
        pprint(partitions_response)
        print("The response of SlurmApi->slurm_v0039_get_nodes:\n")
        pprint(nodes_response)

    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_partitions: %s\n" % e)