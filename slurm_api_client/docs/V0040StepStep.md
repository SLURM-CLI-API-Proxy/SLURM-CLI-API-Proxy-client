# V0040StepStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Slurm Job Step ID | [optional] 
**name** | **str** | Step name | [optional] 

## Example

```python
from openapi_client.models.v0040_step_step import V0040StepStep

# TODO update the JSON string below
json = "{}"
# create an instance of V0040StepStep from a JSON string
v0040_step_step_instance = V0040StepStep.from_json(json)
# print the JSON string representation of the object
print(V0040StepStep.to_json())

# convert the object into a dict
v0040_step_step_dict = v0040_step_step_instance.to_dict()
# create an instance of V0040StepStep from a dict
v0040_step_step_from_dict = V0040StepStep.from_dict(v0040_step_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


