import logging
from slurm_api_cli_proxy.client_args_linker.slurm_api_client_wrapper import SlurmAPIClientWrapper, ApiClientException, SlurmCommandResponse
from slurm_api_cli_proxy.client_args_linker.constants import slurm_statuses
from openapi_client.models.v0043_openapi_error import V0043OpenapiError
from typing import List
import openapi_client

#sbatch related
from openapi_client.models.v0043_job_submit_req import V0043JobSubmitReq
from openapi_client.models.v0043_openapi_job_submit_response import V0043OpenapiJobSubmitResponse

#squeue related
from openapi_client.models.v0043_openapi_job_info_resp import V0043OpenapiJobInfoResp
from openapi_client.models.v0043_job_info import V0043JobInfo
from openapi_client.models.v0043_job_res import V0043JobRes, V0043JobResNodes
from openapi_client.models.v0043_uint64_no_val_struct import V0043Uint64NoValStruct
from openapi_client.models.v0043_uint16_no_val_struct import V0043Uint16NoValStruct

#scancel related
from openapi_client.models.v0043_kill_jobs_msg import V0043KillJobsMsg
from openapi_client.models.v0043_openapi_kill_jobs_resp import V0043OpenapiKillJobsResp

#scontrol related
from openapi_client.models.v0043_job_desc_msg import V0043JobDescMsg
from openapi_client.models.v0043_openapi_job_post_response import V0043OpenapiJobPostResponse

from openapi_client.rest import ApiException
from urllib3.exceptions import HTTPError as Urllib3HTTPError

import os
import json
import time
import pprint
import slurm_api_cli_proxy.client_args_linker.v43.squeue_format as sqf
from openapi_client.models.v0043_openapi_partition_resp import V0043OpenapiPartitionResp
from openapi_client.models.v0043_partition_info import V0043PartitionInfo
from openapi_client.models.v0043_partition_info_nodes import V0043PartitionInfoNodes
from openapi_client.models.v0043_openapi_partition_resp import V0043OpenapiPartitionResp

class V43SlurmAPIClientWrapper(SlurmAPIClientWrapper):

    # ESLURM_INVALID_JOB_ID, ESLURM_ALREADY_DONE: scancel doesn't report these
    SCANCEL_SILENT_ERRORS = {2017, 2021}

    def sbatch_post_request(self,request:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SlurmCommandResponse:     
        #Based on the code snippet included on the documentation generated from the Slurm OpenAPI specification
        configuration = conf
        configuration.api_key['token'] = slurmrestd_token
        with openapi_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            
            api_instance = openapi_client.SlurmApi(api_client)

            # Convert the dictionary to a JSON string
            json_req_string = json.dumps(request, indent=2)

            v0043_job_submission_instance = V0043JobSubmitReq.from_json(json_req_string)
            if v0043_job_submission_instance is None:
                raise ValueError(f"Creation of sbatch job submission payload form json returned None when using {json_req_string}")
            
            response = SlurmCommandResponse()

            try:
                # submit the job
                api_response = api_instance.slurm_v0043_post_job_submit(v0043_job_submission_instance)
            except ApiException as ae:
                # Slurm reports rejected submissions (bad partition, account, ...) as HTTP errors
                # with an 'errors' list in the body: show those like sbatch would.
                response.errors.extend(V43SlurmAPIClientWrapper.errors_from_api_exception(ae, "sbatch"))
                return response
            except Urllib3HTTPError as ce:
                response.errors.extend(V43SlurmAPIClientWrapper.connection_error(ce, "sbatch", configuration))
                return response
            except Exception as e:
                raise ApiClientException(f'Unexpected error while performing a POST request for the sbatch command:{e}') from e

            if api_response.errors:
                for err in api_response.errors:
                    #Based on V0043Error type
                    response.errors.append(f"Error no:{err.error_number}:{err.error}. Source:{err.source}. Description:{err.description}")

            if api_response.job_submit_user_msg:
                # sbatch prints the job_submit plugin's message to stderr
                response.warnings.append(api_response.job_submit_user_msg)

            if not response.errors:
                if api_response.job_id is None:
                    response.errors.append("sbatch: error: the SLURM API did not return a job id")
                else:
                    # Same output as sbatch; tools such as dask-jobqueue parse the job id from it
                    response.output = f"Submitted batch job {api_response.job_id}"
                    response.job_id = api_response.job_id

            return response


    # HTTP statuses slurmrestd uses when the token is missing, invalid or expired
    AUTH_FAILURE_STATUSES = {401, 511}

    @staticmethod
    def errors_from_api_exception(ae: ApiException, command: str) -> List[str]:
        """Turn a failed API response into short CLI error lines (no raw HTTP dump)."""
        messages: List[str] = []
        if ae.body:
            try:
                body = json.loads(ae.body)
                for err in body.get("errors") or []:
                    description = err.get("description") or ""
                    error = err.get("error") or ""
                    messages.append(f"{command}: error: {description}{': ' if description and error else ''}{error}")
            except (ValueError, AttributeError):
                pass
        if not messages:
            if not ae.status:
                # raised by the client itself, e.g. for TLS errors: no HTTP response at all
                messages.append(f"{command}: error: cannot reach the SLURM API: {ae.reason}")
            else:
                messages.append(f"{command}: error: SLURM API request failed (HTTP {ae.status}): {ae.reason}")
        if ae.status in V43SlurmAPIClientWrapper.AUTH_FAILURE_STATUSES:
            messages.append(f"{command}: error: the SLURM API did not accept the token in SLURM_JWT (missing, invalid or expired?)")
        return messages

    @staticmethod
    def format_response_errors(errors, command: str) -> List[str]:
        """Errors listed in a (successful) API response, as CLI error lines."""
        lines: List[str] = []
        for err in errors or []:
            description = getattr(err, "description", None) or ""
            error = getattr(err, "error", None) or ""
            lines.append(f"{command}: error: {description}{': ' if description and error else ''}{error}" if (description or error) else f"{command}: error: {err}")
        return lines

    @staticmethod
    def log_response_warnings(warnings, command: str) -> None:
        """slurmrestd adds informational warnings (e.g. 'Zero jobs to dump') that the real
        commands don't print; they are only logged at debug level."""
        for w in warnings or []:
            logging.getLogger(__name__).debug("%s: SLURM API warning: %s", command, getattr(w, "description", None) or w)

    @staticmethod
    def connection_error(e: Exception, command: str, conf: openapi_client.Configuration) -> List[str]:
        """The SLURM API could not be reached (wrong URL, DNS, network, TLS)."""
        reason = getattr(e, "reason", None) or e
        return [f"{command}: error: cannot reach the SLURM API at {conf.host}: {reason}"]


    def scancel_delete_request(self,request:dict,conf:openapi_client.Configuration,slurmrestd_token:str,quiet:bool=False)-> SlurmCommandResponse:
        # quiet (-Q) is accepted for compatibility: the errors it suppresses in scancel
        # (jobs already gone) are never reported, as in Slurm 25.05.
        configuration = conf
        configuration.api_key['token'] = slurmrestd_token

        with openapi_client.ApiClient(configuration) as api_client:
            api_instance = openapi_client.SlurmApi(api_client)

            kill_jobs_msg = V0043KillJobsMsg.from_dict(request)
            response = SlurmCommandResponse()

            try:
                api_response:V0043OpenapiKillJobsResp = api_instance.slurm_v0043_delete_jobs(kill_jobs_msg)
            except ApiException as ae:
                # A failed request can still list per-job results; use them when present
                try:
                    api_response = V0043OpenapiKillJobsResp.from_json(ae.body) if ae.body else None  # type: ignore[assignment]
                except Exception:
                    api_response = None  # type: ignore[assignment]
                if api_response is None or not api_response.status:
                    response.errors.extend(V43SlurmAPIClientWrapper.errors_from_api_exception(ae, "scancel"))
                    return response
            except Urllib3HTTPError as ce:
                response.errors.extend(V43SlurmAPIClientWrapper.connection_error(ce, "scancel", configuration))
                return response
            except Exception as e:
                raise ApiClientException(f'Unexpected error while performing a DELETE request for the scancel command:{e}') from e

            # Only jobs that could not be signalled are listed in 'status'; an empty list means
            # success. Like scancel (Slurm 25.05), jobs that don't exist (anymore) or are
            # already completing are not reported; other failures (e.g. permission denied)
            # are, and the exit code is Slurm's error number modulo 256 (as scancel's).
            for job_status in api_response.status or []:
                err = job_status.error
                if err is None or not (err.code or err.message or err.string):
                    continue
                if err.code in V43SlurmAPIClientWrapper.SCANCEL_SILENT_ERRORS:
                    continue
                job_label = job_status.step_id or (job_status.job_id.number if job_status.job_id else "?")
                message = err.message or err.string or f"error code {err.code}"
                response.errors.append(f"scancel: error: Kill job error on job id {job_label}: {message}")
                if err.code:
                    response.exit_code = err.code % 256 or 1

            for api_err in api_response.errors or []:
                if api_err.description or api_err.error:
                    response.errors.append(f"scancel: error: {api_err.description or api_err.error}")

            return response



    def scontrol_update_request(self,target_job_id:str,request:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SlurmCommandResponse:

        configuration = conf
        configuration.api_key['token'] = slurmrestd_token

        with openapi_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            
            api_instance = openapi_client.SlurmApi(api_client)

            # Convert the dictionary to a JSON string
            json_req_string = json.dumps(request, indent=2)

            v0043_job_update_payload = V0043JobDescMsg.from_json(json_req_string)

            if v0043_job_update_payload is None:
                raise ValueError(f"Creation of scontrol job submission payload form json returned None when using {json_req_string}")

            response = SlurmCommandResponse()                

            try:
                #submit the update request
                api_response = api_instance.slurm_v0043_post_job(target_job_id, v0043_job_update_payload)
                                
                #Capturing and encapsulating internal errors included as part of the request's response
                if api_response.errors is not None:
                     for err in api_response.errors:
                         #Based on V0043Error type
                         response.errors.append(f"Error no:{err.error_number}:{err.error}. Source:{err.source}. Description:{err.description}")
                
                return response

            # API errors (job not found, authentication, permissions, ...): Slurm's message
            except ApiException as ae:
                response.errors.extend(V43SlurmAPIClientWrapper.errors_from_api_exception(ae, "scontrol"))
                return response
            except Urllib3HTTPError as ce:
                response.errors.extend(V43SlurmAPIClientWrapper.connection_error(ce, "scontrol", configuration))
                return response

            #Any other error would be reported as an unexpected one
            except Exception as e:                
                raise ApiClientException(f'Unexpected error while performing an UPDATE request for the scontrol command:{e}') from e                



    def squeue_get_request(self,cli_arguments:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SlurmCommandResponse:    
        #Based on the code snippet included on the documentation generated from the Slurm OpenAPI specification
        configuration = conf
        configuration.api_key['token'] = slurmrestd_token
            
        with openapi_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.SlurmApi(api_client)
            #update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

            try:
                # get list of jobs
                api_response:V0043OpenapiJobInfoResp = api_instance.slurm_v0043_get_jobs()
            except ApiException as ae:
                return SlurmCommandResponse(errors=V43SlurmAPIClientWrapper.errors_from_api_exception(ae, "squeue"))
            except Urllib3HTTPError as ce:
                return SlurmCommandResponse(errors=V43SlurmAPIClientWrapper.connection_error(ce, "squeue", configuration))
            except Exception as e:
                raise ApiClientException(f'Unexpected error while performing a GET request for the squeue command:{e}') from e

            errors = V43SlurmAPIClientWrapper.format_response_errors(api_response.errors, "squeue")
            V43SlurmAPIClientWrapper.log_response_warnings(api_response.warnings, "squeue")
            if errors:
                return SlurmCommandResponse(errors=errors)

            output = V43SlurmAPIClientWrapper.process_squeue_output(cli_arguments=cli_arguments,api_response=api_response)
            return SlurmCommandResponse(output=output)


    def sinfo_get_request(self,cli_arguments:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SlurmCommandResponse:
        
        configuration = conf
        configuration.api_key['token'] = slurmrestd_token

        with openapi_client.ApiClient(conf) as api_client:    
            api_instance = openapi_client.SlurmApi(api_client)

            try:
                # get all partition info
                api_response:V0043OpenapiPartitionResp = api_instance.slurm_v0043_get_partitions()
            except ApiException as ae:
                return SlurmCommandResponse(errors=V43SlurmAPIClientWrapper.errors_from_api_exception(ae, "sinfo"))
            except Urllib3HTTPError as ce:
                return SlurmCommandResponse(errors=V43SlurmAPIClientWrapper.connection_error(ce, "sinfo", configuration))
            except Exception as e:
                raise ApiClientException(f'Unexpected error while performing a GET request for the sinfo command:{e}') from e

            errors = V43SlurmAPIClientWrapper.format_response_errors(api_response.errors, "sinfo")
            V43SlurmAPIClientWrapper.log_response_warnings(api_response.warnings, "sinfo")
            if errors:
                return SlurmCommandResponse(errors=errors)

            output = V43SlurmAPIClientWrapper.process_sinfo_output(cli_arguments=cli_arguments,api_response=api_response)
            return SlurmCommandResponse(output=output)


    @staticmethod
    def process_sinfo_output(cli_arguments:dict, api_response:V0043OpenapiPartitionResp)->str:
        #ref: https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0043PartitionInfo.md
        partitions:List[V0043PartitionInfo] | None = api_response.partitions

        if partitions != None:
            table = "Partition Name\tTotal Nodes\n"
            table += "-" * 30 + "\n"
            for partition in partitions:
                name = partition.name
                nodes_info: V0043PartitionInfoNodes | None = partition.nodes
                if nodes_info != None:
                    total = nodes_info.total
                else:
                    total = -1
                table += f"{name}\t{total}\n"
            return table
        else:
            return ""



    @staticmethod
    def process_squeue_output(cli_arguments:dict,api_response:V0043OpenapiJobInfoResp)->str:                                                            
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
