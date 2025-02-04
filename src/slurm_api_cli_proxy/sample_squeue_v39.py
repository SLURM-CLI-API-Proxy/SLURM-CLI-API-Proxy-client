import openapi_client
from openapi_client.models.v0039_jobs_response import V0039JobsResponse
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
#configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["SLURM_JWT"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get list of jobs
        api_response = api_instance.slurm_v0039_get_jobs(update_time=update_time)
        print("The response of SlurmApi->slurm_v0039_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_jobs: %s\n" % e)