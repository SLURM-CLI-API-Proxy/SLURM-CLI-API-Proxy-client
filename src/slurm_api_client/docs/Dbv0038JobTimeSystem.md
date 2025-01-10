# Dbv0038JobTimeSystem

System time values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** | Total number of CPU-seconds used by the system on behalf of the process (in kernel mode), in seconds | [optional] 
**microseconds** | **int** | Total number of CPU-seconds used by the system on behalf of the process (in kernel mode), in microseconds | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_time_system import Dbv0038JobTimeSystem

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobTimeSystem from a JSON string
dbv0038_job_time_system_instance = Dbv0038JobTimeSystem.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobTimeSystem.to_json())

# convert the object into a dict
dbv0038_job_time_system_dict = dbv0038_job_time_system_instance.to_dict()
# create an instance of Dbv0038JobTimeSystem from a dict
dbv0038_job_time_system_from_dict = Dbv0038JobTimeSystem.from_dict(dbv0038_job_time_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


