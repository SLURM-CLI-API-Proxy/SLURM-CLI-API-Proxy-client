from slurm_api_cli_proxy.client_args_linker.slurm_api_client_wrapper import SlurmAPIClientWrapper, SbatchResponse, SqueueResponse, ScontrolResponse, ApiClientException
from slurm_api_cli_proxy.client_args_linker.constants import slurm_statuses
from openapi_client.models.v0039_error import V0039Error
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
import os
import json
import time
import pprint



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
            
            try:
                #submit the update request
                api_response = api_instance.slurm_v0039_update_job(target_job_id, v0039_job_update_payload)

                response = ScontrolResponse()                
                
                if api_response.errors is not None:
                     for err in api_response.errors:
                         #Based on V0039Error type
                         response.errors.append(f"Error no:{err.error_number}:{err.error}. Source:{err.source}. Description:{err.description}")
                
                return response

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

                return SqueueResponse(output,errors=errors,warnings=warnings)
        
            except Exception as e:       
                raise ApiClientException(f'Unexpected error while performing a GET request for the squeue command:{e}') from e                



    @staticmethod
    def process_squeue_output(cli_arguments:dict,api_response:V0039JobsResponse)->str:                                                            
        """
        Processes the details returned by the GET request to /jobs so that
        they mimic the output generated by squeue command, according to the
        arguments given (cli_arguments)
        
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

            output = "JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)\n"

            if user_filter == None:
                for job in jobs:
                    if job.job_resources is None:
                        raise ValueError(f"Unexpected 'None' value for job {job} resources")                                     
                    else:
                        job_resources:V0039JobRes = job.job_resources                          
                        output += format_squeue_job(job,job_resources)

            else:
                for job in jobs:                    
                    if job.job_resources is None:
                        raise ValueError(f"Unexpected 'None' value for job {job} resources")                                     
                    else:
                        if job.user_name == user_filter:
                            job_resources = job.job_resources                                                      
                            output += format_squeue_job(job,job_resources)


            return output
        

def format_squeue_job(job:V0039JobInfo,job_resources:V0039JobRes):
    timestamp = int(time.time())
    if job.job_state is None:
        job_status:str = "??"
    else:
        job_status = slurm_statuses[job.job_state].rjust(2, ' ')

    if job.start_time is None:
        elapsed_time:str = " 0:00"
    else:        
        elapsed_time = str(seconds_to_hhmm(timestamp-job.start_time)) if job.job_state == "RUNNING" else " 0:00"
    return (
        f"{str(job.job_id)[:5]:>5} "
        f"{str(job.partition)[:9]:>9} "
        f"{str(job.name)[:8]:>8} "
        f"{str(job.user_name)[:8]:>8} "
        f"{job_status[:8]:7} "
        f"{elapsed_time[:5]:>6} "
        f"{str(job_resources.allocated_hosts)[:5]:>5} "
        f"{job_resources.nodes}\n"
    )

def seconds_to_hhmm(seconds):
    """
    Convert seconds to HH:MM format.
    
    Args:
        seconds (int): Number of seconds to convert
        
    Returns:
        str: Time in HH:MM format
        
    """
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes:2d}:{remaining_seconds:02d}"