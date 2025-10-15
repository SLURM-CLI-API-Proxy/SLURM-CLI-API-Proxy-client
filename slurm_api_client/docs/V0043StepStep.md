# V0043StepStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Step ID (Slurm job step ID) | [optional] 
**name** | **str** | Step name | [optional] 
**stderr** | **str** | Path to stderr file | [optional] 
**stdin** | **str** | Path to stdin file | [optional] 
**stdout** | **str** | Path to stdout file | [optional] 
**stderr_expanded** | **str** | Step stderr with expanded fields | [optional] 
**stdin_expanded** | **str** | Step stdin with expanded fields | [optional] 
**stdout_expanded** | **str** | Step stdout with expanded fields | [optional] 

## Example

```python
from openapi_client.models.v0043_step_step import V0043StepStep

# TODO update the JSON string below
json = "{}"
# create an instance of V0043StepStep from a JSON string
v0043_step_step_instance = V0043StepStep.from_json(json)
# print the JSON string representation of the object
print(V0043StepStep.to_json())

# convert the object into a dict
v0043_step_step_dict = v0043_step_step_instance.to_dict()
# create an instance of V0043StepStep from a dict
v0043_step_step_from_dict = V0043StepStep.from_dict(v0043_step_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


