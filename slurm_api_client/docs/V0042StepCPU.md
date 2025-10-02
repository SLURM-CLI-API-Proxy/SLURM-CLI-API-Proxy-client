# V0042StepCPU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_frequency** | [**V0042StepCPURequestedFrequency**](V0042StepCPURequestedFrequency.md) |  | [optional] 
**governor** | **str** | Requested CPU frequency governor in kHz | [optional] 

## Example

```python
from openapi_client.models.v0042_step_cpu import V0042StepCPU

# TODO update the JSON string below
json = "{}"
# create an instance of V0042StepCPU from a JSON string
v0042_step_cpu_instance = V0042StepCPU.from_json(json)
# print the JSON string representation of the object
print(V0042StepCPU.to_json())

# convert the object into a dict
v0042_step_cpu_dict = v0042_step_cpu_instance.to_dict()
# create an instance of V0042StepCPU from a dict
v0042_step_cpu_from_dict = V0042StepCPU.from_dict(v0042_step_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


