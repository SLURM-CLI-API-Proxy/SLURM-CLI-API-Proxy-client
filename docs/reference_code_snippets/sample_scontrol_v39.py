import openapi_client
from openapi_client.models.v0039_job_desc_msg import V0039JobDescMsg
from openapi_client.models.v0039_job_update_response import V0039JobUpdateResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Slurm Job ID

    # scontrol hold/release 
    # hold: Optional[StrictBool] = Field(default=None, description="Hold (true) or release (false) job")


    v0039_job_desc_msg = openapi_client.V0039JobDescMsg() # V0039JobDescMsg | update job

    try:
        # update job (scontrol update)



        api_response = api_instance.slurm_v0039_update_job(job_id, v0039_job_desc_msg)
        print("The response of SlurmApi->slurm_v0039_update_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_update_job: %s\n" % e)