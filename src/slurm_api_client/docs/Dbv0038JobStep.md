# Dbv0038JobStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | [**Dbv0038JobStepTime**](Dbv0038JobStepTime.md) |  | [optional] 
**exit_code** | [**Dbv0038JobExitCode**](Dbv0038JobExitCode.md) |  | [optional] 
**nodes** | [**Dbv0038JobStepNodes**](Dbv0038JobStepNodes.md) |  | [optional] 
**tasks** | [**Dbv0038JobStepTasks**](Dbv0038JobStepTasks.md) |  | [optional] 
**pid** | **str** | First process PID | [optional] 
**cpu** | [**Dbv0038JobStepCPU**](Dbv0038JobStepCPU.md) |  | [optional] 
**kill_request_user** | **str** | User who requested job killed | [optional] 
**state** | **str** | State of job step | [optional] 
**statistics** | [**Dbv0038JobStepStatistics**](Dbv0038JobStepStatistics.md) |  | [optional] 
**step** | [**Dbv0038JobStepStep**](Dbv0038JobStepStep.md) |  | [optional] 
**task** | **str** | Task distribution properties | [optional] 
**tres** | [**Dbv0038JobStepTres**](Dbv0038JobStepTres.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_step import Dbv0038JobStep

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobStep from a JSON string
dbv0038_job_step_instance = Dbv0038JobStep.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobStep.to_json())

# convert the object into a dict
dbv0038_job_step_dict = dbv0038_job_step_instance.to_dict()
# create an instance of Dbv0038JobStep from a dict
dbv0038_job_step_from_dict = Dbv0038JobStep.from_dict(dbv0038_job_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


