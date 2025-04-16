import openapi_client
from openapi_client.models.v0040_job_submit_req import V0040JobSubmitReq
from openapi_client.models.v0040_openapi_job_submit_response import V0040OpenapiJobSubmitResponse
from openapi_client.rest import ApiException
from pprint import pprint
import os
import json

#docker run -p 10022:22 -p 6820:6820 ghcr.io/xenon-middleware/slurm:23
#https://github.com/xenon-middleware/xenon-docker-images/tree/master/slurm-23


# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:6820"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.


# Configure API key authorization: user
#configuration.api_key['user'] = os.environ["SLURM_JWT"]

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


    #https://slurm.schedmd.com/rest_api.html#v0.0.42_job_submit_req

    job_request = {
        "script": "#!/bin/bash\nsrun uptime",
        #https://slurm.schedmd.com/rest_api.html#v0.0.42_job_desc_msg
        "job": {
            "environment": ["PATH=/bin/:/usr/bin/:/sbin/"],
            "current_working_directory": "/a/b/c",
            "name": "test slurmrestd job",            
            "output": "slurm-%j.out",
        }
    }
    

    # Convert the dictionary to a JSON string
    json_req_string = json.dumps(job_request, indent=2)

    # create an instance of V0040JobSubmitReq from a JSON string
    v0040_job_submit_req = V0040JobSubmitReq.from_json(json_req_string)

    try:
        # submit new job
        api_response = api_instance.slurm_v0040_post_job_submit(v0040_job_submit_req)
        print("The response of SlurmApi->slurm_v0040_post_job_submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0040_post_job_submit: %s\n" % e)