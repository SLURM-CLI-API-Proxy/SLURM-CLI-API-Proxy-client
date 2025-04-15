# Extending already supported commands with new arguments

## Commands that require using the argument values as part of the request payload (sbatch, scontrol)

Given the design principles previously described, adding argument to a command, already configured for a given API version (in this case, v0.0.39) involves the following steps:

1. Check the target API resource used by the command's proxy, its corresponding API client method, and the related data objects. For example, the `sbatch` proxy command currently implemented performs a POST request to `/slurm/v0.0.39/job/submit`.

    | Command  | VERB + Target SLURM API resource    | OpenAPI Client method    | Related data classes | 
    |----------|-------------------------------------|--------------------------|----------------------|
    | sbatch   | POST /slurm/v0.0.39/job/submit     | [slurm_v0039_submit_job](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/SlurmApi.md#slurm_v0039_submit_job) | [V0039JobSubmission](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0039JobSubmission.md), [V0039JobDescMsg](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0039JobDescMsg.md) (request payload) |
    | squeue   | GET /slurm/v0.0.39/jobs            | [slurm_v0039_get_jobs](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/SlurmApi.md#slurm_v0039_get_jobs) | [V0039JobsResponse](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0039JobsResponse.md) (request response) |
    | scontrol | UPDATE /slurm/v0.0.39/job/{job_id} | [slurm_v0039_update_job](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/SlurmApi.md#slurm_v0039_update_job) | [V0039JobDescMsg](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0039JobDescMsg.md) (request payload) |
    | sinfo    | GET /slurm/v0.0.39/partitions, GET /slurm/v0.0.39/nodes      | [slurm_v0039_get_partitions](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/SlurmApi.md#slurm_v0039_get_partitions) | [V0039PartitionsResponse](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0039PartitionsResponse.md) (request response) |


2. Check which property of the corresponding POST payload should be set to the value given to the argument. To this end, look at the documentation of the class used for creating the request's payload. For example, the POST payload structure required by the `/slurm/v0.0.39/job/submit` resource is defined by the [V0039JobDescMsg](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0039JobDescMsg.md) class. 

3. Based on the above, add an entry on the existing YAML configuration file of the `sbatch` command (`mappings/sbatch_mappings_r23.11_v0.0.39.yaml`). For example, to add support to the `--chdir` argument (which defines in which directory within the SLURM worker the script will be executed), you can verify that the its equivalent on the[V0039JobDescMsg](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0039JobDescMsg.md) class is the `current_working_directory` property. Based on this, the argument should be included as follows: 

    ```yaml
    - name: --chdir
      abbreviation: -D
      is_mandatory: false
      data_type: str
      api_mapping:
          request_property: job.current_working_directory
    ```

    Keep in mind that the accepted values for *data_type* are *int*, *str* and *bool*. When using the latter, argparse uses it as a flag, so no value is captured for it. 


4. And that's it! However, if the captured argument value needs to be pre-processed, you can include a lambda expression to do it if needed. For example, the `--export` argument (the environment variables to be exported), in the `sbatch` command receives a string with comma-separated values, but the [V0039JobDescMsg](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0039JobDescMsg.md) class requires a list of strings (that is, each exported environment variable).

    By including the following definition on the `sbatch` YAML configuration file:

    ```yaml
    - name: --export
      abbreviation: --export
      is_mandatory: false
      data_type: str
      api_mapping:
          request_property: job.environment
          lambda_expression: "lambda p: p.split(',')"
    ```

    The following request payload would be generated:

    ```json

    //Payload generated for the command: sbatch script1.sh --export PATH=/bin/,ENV2=123 --job-name job123

    {
        "script": "<the content of script1.sh>",  
        "job": {
            "environment": ["PATH=/bin/","ENV2=123"],
            "name": "job123"
        }
    }
    ```



## Commands that require using the argument values for output formatting only (squeue, sinfo)

The proxies of commands like `squeue` or `sinfo` use the arguments only for formatting purposes. For example, a `GET` request to the `/slurm/v0.0.39/jobs` (as it doesn't support any arguments), simply return all the jobs as a [V0039JobsResponse](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0039JobsResponse.md) object. Hence, to mimic the behaviour of arguments like `--user`, this [V0039JobsResponse](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0039JobsResponse.md) must be pre-processed to produce a string -the one that will be sent to STDOUT- that is consistent with such command. 

This can be done on the corresponding *client wrapper* method, which, as described on the [design principles section](designprinciples.md), is where the request is performed using the API client, and response processed. You can check which wrapper is being used by looking at the `wrapper_package` and `wrapper_class` on the command's YAML configuration file. 

For example, the `squeue_get_request` method of the `V39SlurmAPIClientWrapper` class, listed below, transforms the given V0039JobsResponse, into a string that mimics the `squeue` output. For this it considers the details included on the list of [V0039JobInfo](https://github.com/SLURM-CLI-API-Proxy/SLURM-CLI-API-Proxy-client/blob/main/slurm_api_client/docs/V0039JobInfo.md) objects given on its *jobs* property. Hence, to do the output pre-processing considering the `--user` argument, this method should check if this argument was included on the `cli_arguments` dictionary, which value (the user) was given to it, and filter the jobs whose `user_id` is equal to such value:


```python

def squeue_get_request(self,cli_arguments:dict,conf:openapi_client.Configuration,slurmrestd_token:str)-> SqueueResponse:    
    configuration = conf
    configuration.api_key['token'] = slurmrestd_token
        
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.SlurmApi(api_client)
        #update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

        try:
            # get list of jobs
            api_response:V0039JobsResponse = api_instance.slurm_v0039_get_jobs()                

            ######################################
            ######## TRANSFORM api_response_dict into a string, based on:
            ########  * the api response
            ########  * the cli_arguments            
            output:str = ...
            ######################################

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



```