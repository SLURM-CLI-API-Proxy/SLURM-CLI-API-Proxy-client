# Dbv0038JobStepTres

TRES usage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested** | [**Dbv0038JobStepTresRequested**](Dbv0038JobStepTresRequested.md) |  | [optional] 
**consumed** | [**Dbv0038JobStepTresRequested**](Dbv0038JobStepTresRequested.md) |  | [optional] 
**allocated** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_step_tres import Dbv0038JobStepTres

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobStepTres from a JSON string
dbv0038_job_step_tres_instance = Dbv0038JobStepTres.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobStepTres.to_json())

# convert the object into a dict
dbv0038_job_step_tres_dict = dbv0038_job_step_tres_instance.to_dict()
# create an instance of Dbv0038JobStepTres from a dict
dbv0038_job_step_tres_from_dict = Dbv0038JobStepTres.from_dict(dbv0038_job_step_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


