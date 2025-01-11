# Dbv0038JobStepStep

Step details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | Parent job id | [optional] 
**het** | [**Dbv0038JobStepStepHet**](Dbv0038JobStepStepHet.md) |  | [optional] 
**id** | **str** | Step id | [optional] 
**name** | **str** | Step name | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_step_step import Dbv0038JobStepStep

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobStepStep from a JSON string
dbv0038_job_step_step_instance = Dbv0038JobStepStep.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobStepStep.to_json())

# convert the object into a dict
dbv0038_job_step_step_dict = dbv0038_job_step_step_instance.to_dict()
# create an instance of Dbv0038JobStepStep from a dict
dbv0038_job_step_step_from_dict = Dbv0038JobStepStep.from_dict(dbv0038_job_step_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


