
# Adding new commands

The current version of the tool provides proxies for the `sbatch`, `squeue` and `scontrol`, commands, with a selection of their respective arguments. In the process of inclusing these, there were further design considerations for simplyfing as much as possible the inclusion of additional SLURM commands. These design considerations, along with the suggested steps for adding a new command, are below described, with `sinfo` as a reference example.

1. As the first step, identify wich resources of the SLURM API can be used to replicate the new command. Using the examples included in the documentation, make experiments with the API client to understand what is required by the payload, the structure of the API response, etc. The `sinfo` requires performing GET requests to `/slurm/v0.0.39/partitions` and
`/slurm/v0.0.39/nodes` resources, hence you can refer to the [slurm_v0039_get_nodes](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/SlurmApi.md#slurm_v0039_get_nodes) and [slurm_v0039_get_partitions](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/SlurmApi.md#slurm_v0039_get_partitions) functions documentation. As you will see, the [V0039NodesResponse](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0039NodesResponse.md) provides details of every node, including the list of the partitions each one belongs to, whereas the[V0039PartitionsResponse](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0039PartitionsResponse.md) gives the detais of such partitions. Use these code examples to create a minimum python script that performs a request to these two resources and print the 'raw' output.

2. To run the script, update the *host* and *api_key* properties so that they match your target test SLURM server:

    ```python

    configuration = openapi_client.Configuration(
        host = "http://<slurm-controllers-name>:6820"
    )

    configuration.api_key['token'] = os.environ["SLURM_JWT"]

    ```

3. Create a new YAML file for the command on `src/mappings` (all the YAML files here are copied to the Python package data, as seen on the `setup.py` file). By convention, to ensure that a cli parser is properly created for the new command, each argument must include the *name*, *abbreviation*, *is_mandatory*, and *type* elements:

    ```yaml
    mapping_meta:
    command: sinfo
    api_version: 0.0.39
    wlm_release: 23.11
    wrapper_package: slurm_api_cli_proxy.client_args_linker.v39.slurm_api_client_wrapper_v39
    wrapper_class: V39SlurmAPIClientWrapper

    parameters:

    - name: 
        abbreviation: 
        is_mandatory: 
        type:
        
    ```

4. Now you need to create a new method on the *client wrapper* that performs the API request, for a given API version, required by the new proxy command. This method must return an `SlurmCommandResponse` object, which contains the command's output to be printed on STDOUT, along with the errors and warnings reported by SLURM in the process. As it will use the API client required for that particular API version, its implementation can be based on the python example you created on step 1. 
    
    Add an abstract method for the new command on the *client wrapper* interface (`SlurmAPIClientWrapper`), and add its implementation on the `V39SlurmAPIClientWrapper` (a class that implements the `SlurmAPIClientWrapper` interface). This method should include as parameters, at least, an `openapi_client.Configuration` and the slurm API token. The method created for the `sinfo` command also includes a dictionary with the CLI arguments, so its output can be properly formatted before including it on the returned `SlurmCommandResponse` object (other POST-based commands like `squeue` would also require a dictionary for creating the request's JSON payload).
    
    It is also important to consider that, by convention, any exception catched within the method should be scaled as an `ApiClientException` so that they are properly handled by the application:

    ```python
    def sinfo_get_request(self,cli_arguments:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SlurmCommandResponse:
        configuration = conf
        configuration.api_key['token'] = slurmrestd_token

        with openapi_client.ApiClient(conf) as api_client:    
            api_instance = openapi_client.SlurmApi(api_client)

            try:

                api_response:V0039PartitionsResponse = api_instance.slurm_v0039_get_partitions()

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

                ################################
                # Transform the request's response (api_response) into a string (output)
                # that resembles the format used by the real SLURM commands, based on the
                # arguments given in cli_arguments:
                output = ...
                #
                #################################
                
                return SlurmCommandResponse(output=output,errors=errors,warnings=warnings)
            
            except Exception as e:
                raise ApiClientException(f'Unexpected error while performing a GET request for the squeue command:{e}') from e 

    ```

5. Now that you have a *client wrapper* method for the command, it's time to implement what put everything together: a command evaluator which parses the arguments given through the CLI, prepares the request payload (if needed) based on such arguments and the settings given on the YAML configuration file, and uses this *client wrapper* to perform the request. Most of this is already implemented on the `slurm_api_cli_proxy.command_handler.CommandEvaluator` class, so for a new command only a subclass implementing the `process_command_args` method is required. 

    ```mermaid
    ---
    title: asds
    ---
    classDiagram

        class CommandEvaluator {
            + (abstract) process_command_args(...) SlurmCommandResponse
            + eval_command(self, config_file_path, include_input_file_arg)
            - __get_env_vars(self) Tuple[str, str]
        }

        class SbatchEvaluator {
            + process_command_args(...) SlurmCommandResponse
        }

        class SqueueEvaluator {
            + process_command_args(...) SlurmCommandResponse
        }

        class ScontrolEvaluator {
            + process_command_args(...) SlurmCommandResponse
        }

        CommandEvaluator <|-- SbatchEvaluator
        CommandEvaluator <|-- SqueueEvaluator
        CommandEvaluator <|-- ScontrolEvaluator


    ```
   
    The following example, for the `sinfo` command, describe the method's arguments, and how these can be used to perform the request base on the given arguments:
   
    ```python

    class SinfoEvaluator(CommandEvaluator):

        def process_command_args(self,
        #the wrapper defined on the YAML file will be set here
        slurm_cli_wrapper:SlurmAPIClientWrapper,
        #the dictionary with the CLI arguments given by argparse
        cli_args,
        #an object representation of the YAML configuration file
        command_mappings_config:CliToJsonPayloadMappings,
        #the configuration required to create an instance of the client
        configuration:openapi_client.Configuration,
        #the SLURM API web token
        slurm_jwt:str)->SlurmCommandResponse:    

            #dictionary with the arguments/values given to the squeue command
            request_args = args_to_parameters_dict(command_args_dict=vars(cli_args))

            response = slurm_cli_wrapper.sinfo_get_request(request_args, 
            configuration,slurm_jwt)

            return response


    ```


6. On the `command_handler` add the function that make use of the *Command Evaluator*, which can be used for linking it with the proxy command's entry point. As seen in the example, here you refer to the YAML configuration file originally created:

    ```python
    def sinfo():

        eval = SinfoEvaluator()
        eval.eval_command(config_file_path='mappings/sinfo_mappings_r23.11_v0.0.39.yaml')    

    ```

7. Link the method above to an entry point that corresponds to the original command name:
    ```python
        #setup.py
        ...
        entry_points={
            "console_scripts": [
                "sbatch=slurm_api_cli_proxy.command_handler:sbatch",
                "squeue=slurm_api_cli_proxy.command_handler:squeue",
                "scontrol=slurm_api_cli_proxy.command_handler:scontrol",
                "sinfo=slurm_api_cli_proxy.command_handler:sinfo",
            ],
        },

    ```

8. After rebuilding the package (`pip install .`), the new command should now be available.