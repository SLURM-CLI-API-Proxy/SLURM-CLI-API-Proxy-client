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


class SqueueResponse():
    def __init__(self,job_id,step_id):
        self.errors = []
        self.warnings = []
        self.job_id = job_id
        self.step_id = step_id

    def __str__(self):
        return f"Job {self.job_id} - {len(self.errors)} errors:{self.errors}"




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
        """
        pass

    @abstractmethod
    def squeue_get_request(self,request:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> str:
        """
        Sends a GET request to the job endpoint.

        Args:
            request (dict): The arguments required by the API client. 
            conf (openapi_client.Configuration): The configuration object for the API client.

        Returns:
            str: The response from the sbatch endpoint (to be processed and sent to STDOUT).
        """

        pass


def get_slurm_api_client_wrapper(payload_mappings:CliToJsonPayloadMappings)->SlurmAPIClientWrapper:

    wrapper_pkg:str = payload_mappings.metadata["wrapper_package"]
    wrapper_class:str = payload_mappings.metadata["wrapper_class"]


    dummy_conf = {"module":"slurm_api_cli_proxy.client_args_linker.v39.slurm_api_client_wrapper_v39",
                  "class_name":"V39SlurmAPIClientWrapper"}

    linker_mod = importlib.import_module(wrapper_pkg)
    
    linker_class = getattr(linker_mod, wrapper_class)

    linker_inst = linker_class()

    if not isinstance(linker_inst,SlurmAPIClientWrapper):
        raise Exception(f"Dynamically load of arguments linker failed (${dummy_conf["module"]}.${dummy_conf["class_name"]}). An ArgsLinker subclass is expected)")

    return linker_inst

