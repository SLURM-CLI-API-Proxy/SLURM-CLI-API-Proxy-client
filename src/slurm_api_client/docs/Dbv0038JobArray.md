# Dbv0038JobArray

Array properties (optional)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | Job id of array | [optional] 
**limits** | [**Dbv0038JobArrayLimits**](Dbv0038JobArrayLimits.md) |  | [optional] 
**task** | **str** | Array task | [optional] 
**task_id** | **int** | Array task id | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_array import Dbv0038JobArray

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobArray from a JSON string
dbv0038_job_array_instance = Dbv0038JobArray.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobArray.to_json())

# convert the object into a dict
dbv0038_job_array_dict = dbv0038_job_array_instance.to_dict()
# create an instance of Dbv0038JobArray from a dict
dbv0038_job_array_from_dict = Dbv0038JobArray.from_dict(dbv0038_job_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


