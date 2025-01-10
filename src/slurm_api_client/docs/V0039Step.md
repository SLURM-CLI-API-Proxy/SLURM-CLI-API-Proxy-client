# V0039Step


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | [**V0039StepTime**](V0039StepTime.md) |  | [optional] 
**exit_code** | [**V0039JobExitCode**](V0039JobExitCode.md) |  | [optional] 
**nodes** | [**V0039StepNodes**](V0039StepNodes.md) |  | [optional] 
**tasks** | [**V0039StepTasks**](V0039StepTasks.md) |  | [optional] 
**pid** | **str** |  | [optional] 
**cpu** | [**V0039StepCPU**](V0039StepCPU.md) |  | [optional] 
**kill_request_user** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**statistics** | [**V0039StepStatistics**](V0039StepStatistics.md) |  | [optional] 
**step** | [**V0039StepStep**](V0039StepStep.md) |  | [optional] 
**task** | [**V0039StepTask**](V0039StepTask.md) |  | [optional] 
**tres** | [**V0039StepTres**](V0039StepTres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_step import V0039Step

# TODO update the JSON string below
json = "{}"
# create an instance of V0039Step from a JSON string
v0039_step_instance = V0039Step.from_json(json)
# print the JSON string representation of the object
print(V0039Step.to_json())

# convert the object into a dict
v0039_step_dict = v0039_step_instance.to_dict()
# create an instance of V0039Step from a dict
v0039_step_from_dict = V0039Step.from_dict(v0039_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


