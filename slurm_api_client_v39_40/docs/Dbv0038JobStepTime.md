# Dbv0038JobStepTime

Time properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** | Total time elapsed | [optional] 
**end** | **int** | Timestamp of when job ended | [optional] 
**start** | **int** | Timestamp of when job started | [optional] 
**suspended** | **int** | Timestamp of when job last suspended | [optional] 
**system** | [**Dbv0038JobTimeSystem**](Dbv0038JobTimeSystem.md) |  | [optional] 
**total** | [**Dbv0038JobTimeTotal**](Dbv0038JobTimeTotal.md) |  | [optional] 
**user** | [**Dbv0038JobTimeUser**](Dbv0038JobTimeUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_step_time import Dbv0038JobStepTime

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobStepTime from a JSON string
dbv0038_job_step_time_instance = Dbv0038JobStepTime.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobStepTime.to_json())

# convert the object into a dict
dbv0038_job_step_time_dict = dbv0038_job_step_time_instance.to_dict()
# create an instance of Dbv0038JobStepTime from a dict
dbv0038_job_step_time_from_dict = Dbv0038JobStepTime.from_dict(dbv0038_job_step_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


