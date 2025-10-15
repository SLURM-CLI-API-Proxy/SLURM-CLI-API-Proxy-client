# V0040JobTimeSystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** | System CPU time used by the job in seconds | [optional] 
**microseconds** | **int** | System CPU time used by the job in microseconds | [optional] 

## Example

```python
from openapi_client.models.v0040_job_time_system import V0040JobTimeSystem

# TODO update the JSON string below
json = "{}"
# create an instance of V0040JobTimeSystem from a JSON string
v0040_job_time_system_instance = V0040JobTimeSystem.from_json(json)
# print the JSON string representation of the object
print(V0040JobTimeSystem.to_json())

# convert the object into a dict
v0040_job_time_system_dict = v0040_job_time_system_instance.to_dict()
# create an instance of V0040JobTimeSystem from a dict
v0040_job_time_system_from_dict = V0040JobTimeSystem.from_dict(v0040_job_time_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


