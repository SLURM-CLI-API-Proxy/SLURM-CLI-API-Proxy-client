# Dbv0038JobTime

Time properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** | Total time elapsed | [optional] 
**eligible** | **int** | Total time eligible to run | [optional] 
**end** | **int** | Timestamp of when job ended | [optional] 
**start** | **int** | Timestamp of when job started | [optional] 
**submission** | **int** | Timestamp of when job submitted | [optional] 
**suspended** | **int** | Timestamp of when job last suspended | [optional] 
**system** | [**Dbv0038JobTimeSystem**](Dbv0038JobTimeSystem.md) |  | [optional] 
**total** | [**Dbv0038JobTimeTotal**](Dbv0038JobTimeTotal.md) |  | [optional] 
**user** | [**Dbv0038JobTimeUser**](Dbv0038JobTimeUser.md) |  | [optional] 
**limit** | **int** | Job wall clock time limit | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_time import Dbv0038JobTime

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobTime from a JSON string
dbv0038_job_time_instance = Dbv0038JobTime.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobTime.to_json())

# convert the object into a dict
dbv0038_job_time_dict = dbv0038_job_time_instance.to_dict()
# create an instance of Dbv0038JobTime from a dict
dbv0038_job_time_from_dict = Dbv0038JobTime.from_dict(dbv0038_job_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


