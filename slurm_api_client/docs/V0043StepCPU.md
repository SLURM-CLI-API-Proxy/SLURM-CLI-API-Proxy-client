# V0043StepCPU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_frequency** | [**V0043StepCPURequestedFrequency**](V0043StepCPURequestedFrequency.md) |  | [optional] 
**governor** | **str** | Requested CPU frequency governor in kHz | [optional] 

## Example

```python
from openapi_client.models.v0043_step_cpu import V0043StepCPU

# TODO update the JSON string below
json = "{}"
# create an instance of V0043StepCPU from a JSON string
v0043_step_cpu_instance = V0043StepCPU.from_json(json)
# print the JSON string representation of the object
print(V0043StepCPU.to_json())

# convert the object into a dict
v0043_step_cpu_dict = v0043_step_cpu_instance.to_dict()
# create an instance of V0043StepCPU from a dict
v0043_step_cpu_from_dict = V0043StepCPU.from_dict(v0043_step_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


