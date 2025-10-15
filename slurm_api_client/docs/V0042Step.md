# V0042Step


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | [**V0042StepTime**](V0042StepTime.md) |  | [optional] 
**exit_code** | [**V0042ProcessExitCodeVerbose**](V0042ProcessExitCodeVerbose.md) |  | [optional] 
**nodes** | [**V0042StepNodes**](V0042StepNodes.md) |  | [optional] 
**tasks** | [**V0040StepTasks**](V0040StepTasks.md) |  | [optional] 
**pid** | **str** | Deprecated; Process ID | [optional] 
**cpu** | [**V0042StepCPU**](V0042StepCPU.md) |  | [optional] 
**kill_request_user** | **str** | User ID that requested termination of the step | [optional] 
**state** | **List[str]** |  | [optional] 
**statistics** | [**V0042StepStatistics**](V0042StepStatistics.md) |  | [optional] 
**step** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep.md) |  | [optional] 
**task** | [**V0040StepTask**](V0040StepTask.md) |  | [optional] 
**tres** | [**V0042StepTres**](V0042StepTres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_step import V0042Step

# TODO update the JSON string below
json = "{}"
# create an instance of V0042Step from a JSON string
v0042_step_instance = V0042Step.from_json(json)
# print the JSON string representation of the object
print(V0042Step.to_json())

# convert the object into a dict
v0042_step_dict = v0042_step_instance.to_dict()
# create an instance of V0042Step from a dict
v0042_step_from_dict = V0042Step.from_dict(v0042_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


