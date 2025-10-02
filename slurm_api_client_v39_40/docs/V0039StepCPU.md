# V0039StepCPU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_frequency** | [**V0039StepCPURequestedFrequency**](V0039StepCPURequestedFrequency.md) |  | [optional] 
**governor** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v0039_step_cpu import V0039StepCPU

# TODO update the JSON string below
json = "{}"
# create an instance of V0039StepCPU from a JSON string
v0039_step_cpu_instance = V0039StepCPU.from_json(json)
# print the JSON string representation of the object
print(V0039StepCPU.to_json())

# convert the object into a dict
v0039_step_cpu_dict = v0039_step_cpu_instance.to_dict()
# create an instance of V0039StepCPU from a dict
v0039_step_cpu_from_dict = V0039StepCPU.from_dict(v0039_step_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


