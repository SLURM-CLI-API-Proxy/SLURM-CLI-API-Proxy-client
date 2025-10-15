# V0043Step


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | [**V0043StepTime**](V0043StepTime.md) |  | [optional] 
**exit_code** | [**V0043ProcessExitCodeVerbose**](V0043ProcessExitCodeVerbose.md) |  | [optional] 
**nodes** | [**V0043StepNodes**](V0043StepNodes.md) |  | [optional] 
**tasks** | [**V0040StepTasks**](V0040StepTasks.md) |  | [optional] 
**pid** | **str** | Deprecated; Process ID | [optional] 
**cpu** | [**V0043StepCPU**](V0043StepCPU.md) |  | [optional] 
**kill_request_user** | **str** | User ID that requested termination of the step | [optional] 
**state** | **List[str]** | Current state | [optional] 
**statistics** | [**V0043StepStatistics**](V0043StepStatistics.md) |  | [optional] 
**step** | [**V0043StepStep**](V0043StepStep.md) |  | [optional] 
**task** | [**V0040StepTask**](V0040StepTask.md) |  | [optional] 
**tres** | [**V0043StepTres**](V0043StepTres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_step import V0043Step

# TODO update the JSON string below
json = "{}"
# create an instance of V0043Step from a JSON string
v0043_step_instance = V0043Step.from_json(json)
# print the JSON string representation of the object
print(V0043Step.to_json())

# convert the object into a dict
v0043_step_dict = v0043_step_instance.to_dict()
# create an instance of V0043Step from a dict
v0043_step_from_dict = V0043Step.from_dict(v0043_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


