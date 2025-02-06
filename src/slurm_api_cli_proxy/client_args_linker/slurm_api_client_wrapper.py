from abc import ABC, abstractmethod
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


class SlurmAPIClientWrapper(ABC):

    @abstractmethod
    def sbatch_post_request(self,request:dict,conf:openapi_client.Configuration)-> SbatchResponse: 
        """
        Sends a POST request to the sbatch endpoint.

        Args:
            request (dict): The request payload to be sent to the sbatch endpoint. It must
                match the expected JSON structure if the request.
            conf (openapi_client.Configuration): The configuration object for the API client.

        Returns:
            str: The response from the sbatch endpoint (to be processed and sent to STDOUT).
        """
        pass

    @abstractmethod
    def squeue_post_request(self,request:dict,conf:openapi_client.Configuration)-> str:
        pass


def get_slurm_api_client_wrapper(app_config:dict)->SlurmAPIClientWrapper:

    #TODO to be parametrizable on a real configuration file
    dummy_conf = {"module":"slurm_api_cli_proxy.client_args_linker.v39.slurm_api_client_wrapper_v39",
                  "class_name":"V39SlurmAPIClientWrapper"}

    linker_mod = importlib.import_module(dummy_conf["module"])
    
    linker_class = getattr(linker_mod, dummy_conf["class_name"])

    linker_inst = linker_class()

    if not isinstance(linker_inst,SlurmAPIClientWrapper):
        raise Exception(f"Dynamically load of arguments linker failed (${dummy_conf["module"]}.${dummy_conf["class_name"]}). An ArgsLinker subclass is expected)")

    return linker_inst

