from slurm_api_cli_proxy.client_args_linker.slurm_api_client_wrapper import SlurmAPIClientWrapper, SbatchResponse
import openapi_client
from openapi_client.models.v0039_job_submission import V0039JobSubmission
from openapi_client.models.v0039_job_submission_response import V0039JobSubmissionResponse
from openapi_client.rest import ApiException
import os
import json


class V39SlurmAPIClientWrapper(SlurmAPIClientWrapper):

    def sbatch_post_request(self,request:dict,conf:openapi_client.Configuration)-> SbatchResponse:        
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
                
                response = SbatchResponse(job_id=api_response.job_id,step_id=api_response.step_id)
                
                for err in api_response.errors:
                    #Based on V0039Error type
                    #TODO check if a template may be required
                    response.errors.append(f"Error no:{err.error_number}:{err.error}. Source:{err.source}. Description:{err.description}")
                
                return response

            except Exception as e:                
                response = SbatchResponse(job_id=None,step_id=None)
                response.errors.append(f"SLURM_PROXY_ERROR: {e}")
                return response

    def squeue_post_request(self,json_request:str)-> str:
        raise Exception("Not implemented")
    

