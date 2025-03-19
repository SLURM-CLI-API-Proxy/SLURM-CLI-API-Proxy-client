from slurm_api_cli_proxy.client_args_linker.slurm_api_client_wrapper import SlurmAPIClientWrapper, SbatchResponse, SqueueResponse, ApiClientException
from slurm_api_cli_proxy.client_args_linker.constants import slurm_statuses
from openapi_client.models.v0039_error import V0039Error
import openapi_client

#sbatch related
from openapi_client.models.v0039_job_submission import V0039JobSubmission
from openapi_client.models.v0039_job_submission_response import V0039JobSubmissionResponse
from openapi_client.rest import ApiException

#squeue related
from openapi_client.models.v0039_jobs_response import V0039JobsResponse
from openapi_client.models.v0039_job_info import V0039JobInfo
from openapi_client.models.v0039_job_res import V0039JobRes

import os
import json
from jsonpath import JSONPath as JP
import time
import pprint
import yaml
import re
from datetime import timedelta
import pkg_resources



class V39SlurmAPIClientWrapper(SlurmAPIClientWrapper):

    __default_squeue_format = "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R" 
    # -l, --long
    __long_squeue_format = "%.18i %.9P %.8j %.8u %.8T %.10M %.9l %.6D %R" 
    # -s, --steps
    __steps_squeue_format = "%.15i %.8j %.9P %.8u %.9M %N"
    __squeue_format_mappings = {}
    __squeue_format_re = ''
    __squeue_format_method_map = {}



    def __init__(self):
        super().__init__()
        # TODO: there is probably a better way to define the path ... ?
        squeue_format_mappings_path = pkg_resources.resource_filename(__name__, '../../mappings/squeue_format_mappings_r23.11_v0.0.39.yaml')
        # /home/cschelp2/SLURM-CLI-API-Proxy-client/src/slurm_api_cli_proxy/mappings/squeue_mappings_r23.11_v0.0.39.yaml
        V39SlurmAPIClientWrapper.__squeue_format_mappings = yaml.safe_load(open(squeue_format_mappings_path))

        all_type_keys = list(V39SlurmAPIClientWrapper.__squeue_format_mappings.keys())
        types_matcher = '|'.join(all_type_keys)
        V39SlurmAPIClientWrapper.__squeue_format_re = f"(\\.?)(\\d*)({types_matcher})(\\w*)(\\W*)"

        V39SlurmAPIClientWrapper.__squeue_format_method_map = {
            'get_D_format_value': V39SlurmAPIClientWrapper.get_D_format_value,
            'get_l_format_value': V39SlurmAPIClientWrapper.get_l_format_value,
            'get_M_format_value': V39SlurmAPIClientWrapper.get_M_format_value,
            'get_Q_format_value': V39SlurmAPIClientWrapper.get_Q_format_value,
            'get_R_format_value': V39SlurmAPIClientWrapper.get_R_format_value,
            'get_t_format_value': V39SlurmAPIClientWrapper.get_t_format_value,
        }

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
                squeue_format = cli_arguments["--format"]
            elif "--long" in cli_arguments:
                squeue_format = V39SlurmAPIClientWrapper.__long_squeue_format
            elif "--steps" in cli_arguments:
                squeue_format = V39SlurmAPIClientWrapper.__steps_squeue_format
            else:
                squeue_format = V39SlurmAPIClientWrapper.__default_squeue_format

            table_layout = V39SlurmAPIClientWrapper.parse_format_string(squeue_format)
            squeue_output = V39SlurmAPIClientWrapper.apply_table_layout(jobs, table_layout, user_filter)

            return squeue_output
        
    @staticmethod
    def parse_format_string(format):
        tokens = [token for token in format.split('%') if len(token)>0]
        table_layout = []
        for token in tokens:
            matches = re.findall(V39SlurmAPIClientWrapper.__squeue_format_re, token)
            if len(matches) != 1:
                raise ValueError(f"Invalid format token '{token}'")
            single_match = matches[0]  
            if len(single_match) != 5:
                raise ValueError(f"Invalid format token '{token}'")
            align_right, width, coltype, suffix, spacer  = single_match
            if not width and align_right:
                raise ValueError(f"No alignment ('.') without width allowed: '{token}'.")
            
            # resolve type-info from mapping
            type_info = V39SlurmAPIClientWrapper.__squeue_format_mappings[coltype]
            column = type_info.copy()

            column.pop('descr')
            column['align_right'] = (align_right == '.')
            column['width'] = int(width) if width else 0
            column['suffix'] = suffix
            column['spacer'] = spacer

            table_layout.append(column)
        
        return table_layout
    
    @staticmethod
    def apply_table_layout(jobs, table_layout, user_filter):
        output = V39SlurmAPIClientWrapper.write_header(table_layout)
        for job in jobs:
            if job.job_resources is None:
                raise ValueError(f"Unexpected 'None' value for job {job} resources")
            if user_filter and job.user_name != user_filter:
                continue

            job_row = ''
            for column in table_layout:
                if 'json_path' in column:
                    value = str(JP("$."+column['json_path']).parse(job)[0])
                else:
                    method_key = column['method']
                    method = V39SlurmAPIClientWrapper.__squeue_format_method_map[method_key]
                    value = str(method(job))

                if not column['width']:
                    job_row += value
                elif column['align_right']:
                    # align (=pad) right and/or truncate
                    job_row += value.rjust(column['width'])[:column['width']]
                else:
                    # align (=pad) left and/or truncate
                    job_row += value.ljust(column['width'])[:column['width']]

                job_row += column['suffix'] + column['spacer']

            output += job_row + "\n"

        return output

    def write_header(table_layout):
        header = ''
        for column in table_layout:
            if not column['width']:
                header += column['head']
            elif column['align_right']:
            # align (=pad) right and/or truncate
                header += column['head'].rjust(column['width'])[:column['width']]
            else:
                # align (=pad) left and/or truncate
                header += column['head'].ljust(column['width'])[:column['width']]

            header += column['suffix'] + column['spacer']

        return header + "\n"    

    @staticmethod
    def get_D_format_value(job):
        return job.job_resources.allocated_hosts

    @staticmethod
    def get_l_format_value(job):
        time_limit_info = job['time_limit']
        return V39SlurmAPIClientWrapper._get_num_value(time_limit_info)

    @staticmethod
    def get_M_format_value(job):
        start_time_info = job['start_time']
        start_time = V39SlurmAPIClientWrapper._get_num_value(start_time_info)
        end_time_info = job['end_time']
        end_time = V39SlurmAPIClientWrapper._get_num_value(end_time_info)
        # These values are always set, according to the docs.
        # So we can assume these to be numbers.
        duration = timedelta(seconds=int(end_time - start_time))
        return V39SlurmAPIClientWrapper._format_duration(duration)

    @staticmethod
    def get_Q_format_value(job):
        prio_info = job['priority']
        return V39SlurmAPIClientWrapper._get_num_value(prio_info)

    @staticmethod
    def get_R_format_value(job):
        return job.job_resources.nodes
    
    @staticmethod
    def get_t_format_value(job):
        state_description = job['job_state'][0]
        # TODO: add the actual mapping 
        return state_description[:2]
    
    @staticmethod
    def _get_num_value(num_info):
        if not num_info['set']:
            return "NOT_SET"
        if num_info['infinite']:
            return "INFINITE"
    
        return num_info['number']

    @staticmethod
    def _format_duration(timed):
        days, remainder = divmod(int(timed.total_seconds()), 24 * 3600)
        hours, remainder = divmod(remainder, 3600,)
        minutes, seconds = divmod(remainder, 60)
        
        result = ''
        hours_width = 1
        minutes_width = 1
        if days:
            result += f"{days}:"
            hours_width = 2
        if hours or days:
            result += f"{hours}".rjust(hours_width, '0') + ':'
            minutes_width = 2
        
        result += f"{minutes}".rjust(minutes_width, '0') + ':'
        result += f"{seconds:02}"

        return result

# def format_squeue_job(job:V0039JobInfo,job_resources:V0039JobRes):
#     timestamp = int(time.time())
#     if job.job_state is None:
#         job_status:str = "??"
#     else:
#         job_status = slurm_statuses[job.job_state].rjust(2, ' ')

#     if job.start_time is None:
#         elapsed_time:str = " 0:00"
#     else:        
#         elapsed_time = str(seconds_to_hhmm(timestamp-job.start_time)) if job.job_state == "RUNNING" else " 0:00"
#     return (
#         f"{str(job.job_id)[:5]:>5} "
#         f"{str(job.partition)[:9]:>9} "
#         f"{str(job.name)[:8]:>8} "
#         f"{str(job.user_name)[:8]:>8} "
#         f"{job_status[:8]:7} "
#         f"{elapsed_time[:5]:>6} "
#         f"{str(job_resources.allocated_hosts)[:5]:>5} "
#         f"{job_resources.nodes}\n"
#     )

# def seconds_to_hhmm(seconds):
#     """
#     Convert seconds to HH:MM format.
    
#     Args:
#         seconds (int): Number of seconds to convert
        
#     Returns:
#         str: Time in HH:MM format
        
#     """
#     minutes = seconds // 60
#     remaining_seconds = seconds % 60
#     return f"{minutes:2d}:{remaining_seconds:02d}"