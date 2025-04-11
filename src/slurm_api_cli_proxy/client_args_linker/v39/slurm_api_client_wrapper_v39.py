from slurm_api_cli_proxy.client_args_linker.slurm_api_client_wrapper import ScontrolResponse, SlurmAPIClientWrapper, SbatchResponse, SqueueResponse, SinfoResponse, ApiClientException
from slurm_api_cli_proxy.client_args_linker.constants import slurm_statuses
from openapi_client.models.v0039_error import V0039Error
from typing import List
import openapi_client

#sbatch related
from openapi_client.models.v0039_job_submission import V0039JobSubmission
from openapi_client.models.v0039_job_submission_response import V0039JobSubmissionResponse

#squeue related
from openapi_client.models.v0039_jobs_response import V0039JobsResponse
from openapi_client.models.v0039_job_info import V0039JobInfo
from openapi_client.models.v0039_job_res import V0039JobRes

#scontrol related
from openapi_client.models.v0039_job_desc_msg import V0039JobDescMsg
from openapi_client.models.v0039_job_update_response import V0039JobUpdateResponse

from openapi_client.rest import ApiException
from openapi_client.exceptions import ServiceException, NotFoundException

import os
import json
import time
import pprint
import slurm_api_cli_proxy.client_args_linker.v39.squeue_format as sqf

class V39SlurmAPIClientWrapper(SlurmAPIClientWrapper):

    def sbatch_post_request(self,request:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SbatchResponse:     
        #Based on the code snippet included on the documentation generated from the Slurm OpenAPI specification
        configuration = conf
        configuration.api_key['token'] = slurmrestd_token
        with openapi_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            
            api_instance = openapi_client.SlurmApi(api_client)

            # Convert the dictionary to a JSON string
            json_req_string = json.dumps(request, indent=2)

            v0039_job_submission_instance = V0039JobSubmission.from_json(json_req_string)
            if v0039_job_submission_instance is None:
                raise ValueError(f"Creation of sbatch job submission payload form json returned None when using {json_req_string}")
            
            try:
                # submit the job
                api_response = api_instance.slurm_v0039_submit_job(v0039_job_submission_instance)
                
                response = SbatchResponse(job_id=api_response.job_id,step_id=api_response.step_id)
                
                if api_response.errors is not None:
                    for err in api_response.errors:
                        #Based on V0039Error type
                        #TODO check if a template may be required
                        response.errors.append(f"Error no:{err.error_number}:{err.error}. Source:{err.source}. Description:{err.description}")
                
                return response

            except Exception as e:
                raise ApiClientException(f'Unexpected error while performing a POST request for the sbatch command:{e}') from e                



    def scontrol_update_request(self,target_job_id:str,request:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> ScontrolResponse:

        configuration = conf
        configuration.api_key['token'] = slurmrestd_token

        with openapi_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            
            api_instance = openapi_client.SlurmApi(api_client)

            # Convert the dictionary to a JSON string
            json_req_string = json.dumps(request, indent=2)

            v0039_job_update_payload = V0039JobDescMsg.from_json(json_req_string)

            if v0039_job_update_payload is None:
                raise ValueError(f"Creation of scontrol job submission payload form json returned None when using {json_req_string}")

            response = ScontrolResponse()                

            try:
                #submit the update request
                api_response = api_instance.slurm_v0039_update_job(target_job_id, v0039_job_update_payload)
                                
                #Capturing and encapsulating internal errors included as part of the request's response
                if api_response.errors is not None:
                     for err in api_response.errors:
                         #Based on V0039Error type
                         response.errors.append(f"Error no:{err.error_number}:{err.error}. Source:{err.source}. Description:{err.description}")
                
                return response

            #Capturing and encapsulating errors resported as a service exception
            except ServiceException as se:
                if (se.body):
                    exception_body = json.loads(se.body)
                    se_errors:List[dict] = exception_body['errors']
                    for ex_err in se_errors:
                        response.errors.append(f"{ex_err['description']}:{ex_err['error']}")
                    return response
                else:
                    raise ApiClientException(f'Unexpected error while performing an UPDATE request for the scontrol command:{se}') from se                
            
            #Capturing and encapsulating errors related to invalid job_ids, reported by the
            # client as exceptions
            except NotFoundException as ne:
                if (ne.body):
                    exception_body = json.loads(ne.body)
                    ne_errors:List[dict] = exception_body['errors']
                    for ex_err in ne_errors:
                        response.errors.append(f"{ex_err['description']}:{ex_err['error']}")
                    return response
                else:
                    raise ApiClientException(f'Unexpected error while performing an UPDATE request for the scontrol command:{ne}') from ne                
                

            #Any other error would be reported as an unexpected one
            except Exception as e:                
                raise ApiClientException(f'Unexpected error while performing an UPDATE request for the scontrol command:{e}') from e                



    def squeue_get_request(self,cli_arguments:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SqueueResponse:    
        #Based on the code snippet included on the documentation generated from the Slurm OpenAPI specification
        configuration = conf
        configuration.api_key['token'] = slurmrestd_token
            
        with openapi_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.SlurmApi(api_client)
            #update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

            try:
                # get list of jobs
                api_response:V0039JobsResponse = api_instance.slurm_v0039_get_jobs()

                output = V39SlurmAPIClientWrapper.process_squeue_output(cli_arguments=cli_arguments,api_response=api_response)

                if (api_response.errors is not None):
                    #Transform list of list[V0039Error] to list[str] 
                    errors:list[str] = list(map(lambda err: str(err), api_response.errors))
                else:
                    errors = []

                if (api_response.warnings is not None):
                    #Transform list of list[V0039Warning] to list[str] 
                    warnings:list[str] = list(map(lambda err: str(err), api_response.warnings))
                else:
                    warnings = []

                return SqueueResponse(output=output,errors=errors,warnings=warnings)
        
            except Exception as e:       
                raise ApiClientException(f'Unexpected error while performing a GET request for the squeue command:{e}') from e                


    def sinfo_get_request(self,cli_arguments:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SinfoResponse:
        
        configuration = conf
        configuration.api_key['token'] = slurmrestd_token

        with openapi_client.ApiClient(conf) as api_client:    
            api_instance = openapi_client.SlurmApi(api_client)

            try:
                # get all partition info
                api_response = api_instance.slurm_v0039_get_partitions()

                if (api_response.errors is not None):
                    #Transform list of list[V0039Error] to list[str] 
                    errors:list[str] = list(map(lambda err: str(err), api_response.errors))
                else:
                    errors = []

                if (api_response.warnings is not None):
                    #Transform list of list[V0039Warning] to list[str] 
                    warnings:list[str] = list(map(lambda err: str(err), api_response.warnings))
                else:
                    warnings = []

                return SinfoResponse(output=str(api_response),errors=errors,warnings=warnings)
            
            except Exception as e:
                raise ApiClientException(f'Unexpected error while performing a GET request for the squeue command:{e}') from e 



    @staticmethod
    def process_squeue_output(cli_arguments:dict,api_response:V0039JobsResponse)->str:                                                            
        """
        Processes the details returned by the GET request to /jobs so that
        they mimic the output generated by squeue command, according to the
        arguments given (cli_arguments)
        https://slurm.schedmd.com/squeue.html
        
        Args:
            cli_arguments (dict): The arguments given when running the proxy command
            api_response: the response given to a GET request to the /jobs resource            
        Returns:
            str: A formatted string representing the job queue.
        """
        if cli_arguments["--json"] is True:

            api_response_dict:dict = json.loads(api_response.to_json())
            #the "meta" property is not included in the original squeue --json
            api_response_dict.pop("meta")

            return json.dumps(api_response_dict, indent=4)            
        
        else:

            user_filter:str|None = None

            if "--user" in cli_arguments:
                user_filter = cli_arguments["--user"] 
                        
            jobs = api_response.jobs
            if (jobs is None):
                raise ValueError("A list of jobs was expected from the requests to the job resource. A None value was received instead.")

            if "--format" in cli_arguments:
                # custom format from user input
                squeue_format_string = cli_arguments["--format"]
            elif "--long" in cli_arguments:
                squeue_format_string = sqf.long
            elif "--steps" in cli_arguments:
                squeue_format_string = sqf.steps
            else:
                squeue_format_string = sqf.default

            return sqf.format_squeue_output(jobs, squeue_format_string, user_filter)
