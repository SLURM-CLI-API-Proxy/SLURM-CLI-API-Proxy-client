from abc import ABC, abstractmethod
from slurm_api_cli_proxy.mappings.cli_to_json_map import CliToJsonPayloadMappings
import openapi_client
import importlib



class SbatchResponse():
    def __init__(self,job_id,step_id):
        self.errors = []        
        self.warnings = []
        self.job_id = job_id
        self.step_id = step_id

    def __str__(self):
        return f"Job {self.job_id} - {len(self.errors)} errors:{self.errors}"

class ScontrolResponse():
    def __init__(self):
        self.errors = []                
        self.warnings = []

class SqueueResponse():
    def __init__(self,output_text:str,errors:list[str] = [], warnings:list[str] = []):
        self.slurm_errors:list[str] = errors
        self.slurm_warnings:list[str] = warnings
        self.pre_processed_output:str  = output_text

class ApiClientException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message




class SlurmAPIClientWrapper(ABC):

    @abstractmethod
    def sbatch_post_request(self,request:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SbatchResponse: 
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
    def squeue_get_request(self,cli_arguments:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SqueueResponse:
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
    def scontrol_update_request(self,target_job_id:str,request:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> ScontrolResponse: 
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



def get_slurm_api_client_wrapper(payload_mappings:CliToJsonPayloadMappings)->SlurmAPIClientWrapper:

    wrapper_pkg:str = payload_mappings.metadata["wrapper_package"]
    wrapper_class:str = payload_mappings.metadata["wrapper_class"]

    linker_mod = importlib.import_module(wrapper_pkg)
    
    linker_class = getattr(linker_mod, wrapper_class)

    linker_inst = linker_class()

    if not isinstance(linker_inst,SlurmAPIClientWrapper):
        raise Exception(f"Dynamically load of arguments linker failed ({wrapper_pkg}.{wrapper_class}). An ArgsLinker subclass is expected)")

    return linker_inst

