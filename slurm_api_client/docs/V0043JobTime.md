# V0043JobTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** | Elapsed time in seconds | [optional] 
**eligible** | **int** | Time when the job became eligible to run (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**end** | **int** | End time (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**planned** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**start** | **int** | Time execution began (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**submission** | **int** | Time when the job was submitted (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**suspended** | **int** | Total time in suspended state in seconds | [optional] 
**system** | [**V0040JobTimeSystem**](V0040JobTimeSystem.md) |  | [optional] 
**limit** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**total** | [**V0040JobTimeTotal**](V0040JobTimeTotal.md) |  | [optional] 
**user** | [**V0040JobTimeUser**](V0040JobTimeUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_job_time import V0043JobTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0043JobTime from a JSON string
v0043_job_time_instance = V0043JobTime.from_json(json)
# print the JSON string representation of the object
print(V0043JobTime.to_json())

# convert the object into a dict
v0043_job_time_dict = v0043_job_time_instance.to_dict()
# create an instance of V0043JobTime from a dict
v0043_job_time_from_dict = V0043JobTime.from_dict(v0043_job_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


