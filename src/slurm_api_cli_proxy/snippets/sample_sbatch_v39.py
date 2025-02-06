import openapi_client
from openapi_client.models.v0039_job_submission import V0039JobSubmission
from openapi_client.models.v0039_job_submission_response import V0039JobSubmissionResponse
from openapi_client.rest import ApiException
import os
import json
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

    #https://slurm.schedmd.com/rest_api.html#v0.0.42_job_submit_req

    job_request = {
        "script": """#!/bin/bash
            ls > /home/hcadavid/temp_file.txt
            sleep 10
            """,  # Modified to include sleep command
        "job": {
            "environment": ["PATH=/bin/:/usr/bin/:/sbin/",
                            "MY_VAR=value1",
                            "ANOTHER_VAR=value2",                            
                            ],
            "current_working_directory": "/home/hcadavid",
            "name": "test slurmrestd job",
            "output": "slurm-%j.out"
        }
    }

    # Convert the dictionary to a JSON string
    json_req_string = json.dumps(job_request, indent=2)

 
    #Empty job submission (from the documenation)
    #v0039_job_submission = openapi_client.V0039JobSubmission() # V0039JobSubmission | submit new job

    v0039_job_submission_instance = V0039JobSubmission.from_json(json_req_string)


    try:
        # submit new job
        api_response = api_instance.slurm_v0039_submit_job(v0039_job_submission_instance)
        print("The response of SlurmApi->slurm_v0039_submit_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0039_submit_job: %s\n" % e)


