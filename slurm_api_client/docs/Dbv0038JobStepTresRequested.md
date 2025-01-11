# Dbv0038JobStepTresRequested

TRES requested for job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 
**max** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 
**min** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 
**total** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_step_tres_requested import Dbv0038JobStepTresRequested

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobStepTresRequested from a JSON string
dbv0038_job_step_tres_requested_instance = Dbv0038JobStepTresRequested.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobStepTresRequested.to_json())

# convert the object into a dict
dbv0038_job_step_tres_requested_dict = dbv0038_job_step_tres_requested_instance.to_dict()
# create an instance of Dbv0038JobStepTresRequested from a dict
dbv0038_job_step_tres_requested_from_dict = Dbv0038JobStepTresRequested.from_dict(dbv0038_job_step_tres_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


