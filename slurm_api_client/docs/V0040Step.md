# V0040Step


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | [**V0040StepTime**](V0040StepTime.md) |  | [optional] 
**exit_code** | [**V0040ProcessExitCodeVerbose**](V0040ProcessExitCodeVerbose.md) |  | [optional] 
**nodes** | [**V0040StepNodes**](V0040StepNodes.md) |  | [optional] 
**tasks** | [**V0040StepTasks**](V0040StepTasks.md) |  | [optional] 
**pid** | **str** | Process ID | [optional] 
**cpu** | [**V0040StepCPU**](V0040StepCPU.md) |  | [optional] 
**kill_request_user** | **str** | User ID that requested termination of the step | [optional] 
**state** | **List[str]** |  | [optional] 
**statistics** | [**V0040StepStatistics**](V0040StepStatistics.md) |  | [optional] 
**step** | [**V0040StepStep**](V0040StepStep.md) |  | [optional] 
**task** | [**V0040StepTask**](V0040StepTask.md) |  | [optional] 
**tres** | [**V0040StepTres**](V0040StepTres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_step import V0040Step

# TODO update the JSON string below
json = "{}"
# create an instance of V0040Step from a JSON string
v0040_step_instance = V0040Step.from_json(json)
# print the JSON string representation of the object
print(V0040Step.to_json())

# convert the object into a dict
v0040_step_dict = v0040_step_instance.to_dict()
# create an instance of V0040Step from a dict
v0040_step_from_dict = V0040Step.from_dict(v0040_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


