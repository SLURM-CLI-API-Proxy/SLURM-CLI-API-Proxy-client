# V0040StepStatisticsCPU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_frequency** | **int** | Average weighted CPU frequency of all tasks in kHz | [optional] 

## Example

```python
from openapi_client.models.v0040_step_statistics_cpu import V0040StepStatisticsCPU

# TODO update the JSON string below
json = "{}"
# create an instance of V0040StepStatisticsCPU from a JSON string
v0040_step_statistics_cpu_instance = V0040StepStatisticsCPU.from_json(json)
# print the JSON string representation of the object
print(V0040StepStatisticsCPU.to_json())

# convert the object into a dict
v0040_step_statistics_cpu_dict = v0040_step_statistics_cpu_instance.to_dict()
# create an instance of V0040StepStatisticsCPU from a dict
v0040_step_statistics_cpu_from_dict = V0040StepStatisticsCPU.from_dict(v0040_step_statistics_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


