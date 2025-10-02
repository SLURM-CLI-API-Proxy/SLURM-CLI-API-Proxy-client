# V0040StepTimeTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** | Total CPU time used by the step in seconds | [optional] 
**microseconds** | **int** | Total CPU time used by the step in microseconds | [optional] 

## Example

```python
from openapi_client.models.v0040_step_time_total import V0040StepTimeTotal

# TODO update the JSON string below
json = "{}"
# create an instance of V0040StepTimeTotal from a JSON string
v0040_step_time_total_instance = V0040StepTimeTotal.from_json(json)
# print the JSON string representation of the object
print(V0040StepTimeTotal.to_json())

# convert the object into a dict
v0040_step_time_total_dict = v0040_step_time_total_instance.to_dict()
# create an instance of V0040StepTimeTotal from a dict
v0040_step_time_total_from_dict = V0040StepTimeTotal.from_dict(v0040_step_time_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


