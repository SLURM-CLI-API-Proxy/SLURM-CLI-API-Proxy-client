import openapi_client
import os
import json
from openapi_client.models.v0039_job_desc_msg import V0039JobDescMsg
from openapi_client.models.v0039_job_update_response import V0039JobUpdateResponse
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
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
#configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = '203' # str | Slurm Job ID

    # scontrol hold/release 
    # hold: Optional[StrictBool] = Field(default=None, description="Hold (True) or release (False) job")

    """"
        scontrol update JobId=<jobid> Priority=<value>
    scontrol update JobId=<jobid> Nice=<adjustment>
    scontrol update JobId=<jobid> Dependency=<dependency-spec>

    # Resource allocation
    scontrol update JobId=<jobid> MinMemoryNode=<MB>
    scontrol update JobId=<jobid> MinCPUsNode=<count>
    

    """

    #Based on:
    #https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0039JobDescMsg.md
    


    job_m = {"environment": ['']}

    job_desc = {
        "environment": ["PATH=/bin/:/usr/bin/:/sbin/"],
        #"nice":1, <- crashes slurmrestd
        "dependency":"singleton",
        "minimum_cpus_per_node":1,
        "hold": True,
    }


    job_obj = V0039JobDescMsg.from_json(json.dumps(job_desc))
    
    print(job_obj)

    try:
        # update job (scontrol update)

        #api_response = api_instance.slurm_v0039_update_job(job_id, v0039_job_desc_msg)

        api_response = api_instance.slurm_v0039_update_job(job_id, job_obj)

        print("The response of SlurmApi->slurm_v0039_update_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_update_job: %s\n" % e)