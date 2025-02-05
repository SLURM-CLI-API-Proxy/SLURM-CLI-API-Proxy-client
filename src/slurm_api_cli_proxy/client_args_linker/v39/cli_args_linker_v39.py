from slurm_api_cli_proxy.client_args_linker.cli_args_linker import ArgsLinker
import openapi_client
from openapi_client.models.v0039_job_submission import V0039JobSubmission
from openapi_client.models.v0039_job_submission_response import V0039JobSubmissionResponse
from openapi_client.rest import ApiException
import os
import json


class V39ArgsLinker(ArgsLinker):

    def sbatch_post_request(request:dict,conf:openapi_client.Configuration)-> str:        
        configuration = conf
        configuration.api_key['token'] = os.environ["SLURM_JWT"]
        with openapi_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            
            api_instance = openapi_client.SlurmApi(api_client)

            # Convert the dictionary to a JSON string
            json_req_string = json.dumps(request, indent=2)

            v0039_job_submission_instance = V0039JobSubmission.from_json(json_req_string)
            try:
                # submit the job
                api_response = api_instance.slurm_v0039_submit_job(v0039_job_submission_instance)
                
                return api_response
            except Exception as e:
                #TODO raise custom exception
                print("Exception when calling SlurmApi->slurm_v0039_submit_job: %s\n" % e)


    def squeue_post_request(json_request:str)-> str:
        raise Exception("Not implemented")
    

