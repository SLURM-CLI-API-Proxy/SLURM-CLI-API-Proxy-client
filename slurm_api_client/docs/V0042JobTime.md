# V0042JobTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** | Elapsed time in seconds | [optional] 
**eligible** | **int** | Time when the job became eligible to run (UNIX timestamp) | [optional] 
**end** | **int** | End time (UNIX timestamp) | [optional] 
**planned** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**start** | **int** | Time execution began (UNIX timestamp) | [optional] 
**submission** | **int** | Time when the job was submitted (UNIX timestamp) | [optional] 
**suspended** | **int** | Total time in suspended state in seconds | [optional] 
**system** | [**V0040JobTimeSystem**](V0040JobTimeSystem.md) |  | [optional] 
**limit** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**total** | [**V0040JobTimeTotal**](V0040JobTimeTotal.md) |  | [optional] 
**user** | [**V0040JobTimeUser**](V0040JobTimeUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_job_time import V0042JobTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0042JobTime from a JSON string
v0042_job_time_instance = V0042JobTime.from_json(json)
# print the JSON string representation of the object
print(V0042JobTime.to_json())

# convert the object into a dict
v0042_job_time_dict = v0042_job_time_instance.to_dict()
# create an instance of V0042JobTime from a dict
v0042_job_time_from_dict = V0042JobTime.from_dict(v0042_job_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


