from abc import ABC, abstractmethod
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings
import openapi_client
import importlib


class SlurmCommandResponse():
    def __init__(self, errors: list[str] | None = None, warnings: list[str] | None = None, output: str = ""):
        # New lists per instance: mutable default arguments would be shared between
        # responses, so errors from one request would leak into the next.
        self.errors: list[str] = list(errors) if errors else []
        self.warnings: list[str] = list(warnings) if warnings else []
        self.output = output
        # Set by sbatch requests
        self.job_id: int | None = None
        # Exit code to use when there are errors (default 1)
        self.exit_code: int | None = None


class ApiClientException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message



class SlurmAPIClientWrapper(ABC):

    @abstractmethod
    def sbatch_post_request(self,request:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SlurmCommandResponse: 
        """
        Sends a POST request to the job endpoint.

        Args:
            request (dict): The request payload to be sent to the sbatch endpoint. It must
                match the expected JSON structure if the request.
            conf (openapi_client.Configuration): The configuration object for the API client.

        Returns:
            str: The response from the sbatch endpoint (to be processed and sent to STDOUT).

        Raises:
            ApiClientException: If there is an error on the proxy, different from the errors returned
            by the SLURM API            
        """
        pass


    @abstractmethod
    def squeue_get_request(self,cli_arguments:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SlurmCommandResponse:
        """
        Sends a GET request to the job endpoint.

        Args:
            cli_arguments (dict): a dictionary with the arguments (and values) given to the squee command
            conf (openapi_client.Configuration): The configuration object for the API client.
            slurmrestd_token (str): The authentication token for the SLURM REST API.

        Returns:
            str: The processed response (ready to be sent to STDOUT)

        Raises:
            ApiClientException: If there is an error on the proxy, different from the errors returned
            by the SLURM API            

        """
        pass


    @abstractmethod
    def sinfo_get_request(self,cli_arguments:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SlurmCommandResponse:
        """
        Sends a GET request to the job endpoint.

        Args:
            cli_arguments (dict): a dictionary with the arguments (and values) given to the squee command
            conf (openapi_client.Configuration): The configuration object for the API client.
            slurmrestd_token (str): The authentication token for the SLURM REST API.

        Returns:
            str: The processed response (ready to be sent to STDOUT)

        Raises:
            ApiClientException: If there is an error on the proxy, different from the errors returned
            by the SLURM API            

        """
        pass


    @abstractmethod
    def scontrol_update_request(self,target_job_id:str,request:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SlurmCommandResponse: 
        """
        Sends a UPDATE request to the job endpoint.

        Args:
            request (dict): The request payload to be sent to the sbatch endpoint. It must
                match the expected JSON structure if the request.
            conf (openapi_client.Configuration): The configuration object for the API client.

        Returns:
            

        Raises:
            ApiClientException: If there is an error on the proxy, different from the errors returned
            by the SLURM API            
        """
        pass



    def scancel_delete_request(self,request:dict,conf:openapi_client.Configuration,slurmrestd_token:str,quiet:bool=False)-> SlurmCommandResponse:
        """
        Sends a DELETE request to the jobs endpoint (cancel or signal jobs).

        Args:
            request (dict): kill_jobs_msg payload (jobs, signal, filters)
            conf (openapi_client.Configuration): The configuration object for the API client.
            slurmrestd_token (str): The authentication token for the SLURM REST API.
            quiet (bool): don't report jobs that no longer exist (scancel -Q)

        Raises:
            ApiClientException: If there is an error on the proxy, different from the errors returned
            by the SLURM API
        """
        raise NotImplementedError("scancel is not supported for this API version")



def get_slurm_api_client_wrapper(payload_mappings:CliToJsonPayloadMappings)->SlurmAPIClientWrapper:

    wrapper_pkg:str = payload_mappings.metadata["wrapper_package"]
    wrapper_class:str = payload_mappings.metadata["wrapper_class"]

    linker_mod = importlib.import_module(wrapper_pkg)
    
    linker_class = getattr(linker_mod, wrapper_class)

    linker_inst = linker_class()

    if not isinstance(linker_inst,SlurmAPIClientWrapper):
        raise Exception(f"Dynamically load of arguments linker failed ({wrapper_pkg}.{wrapper_class}). An ArgsLinker subclass is expected)")

    return linker_inst

