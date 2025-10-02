# V0042StepTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** | Elapsed time in seconds | [optional] 
**end** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**start** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**suspended** | **int** | Total time in suspended state in seconds | [optional] 
**system** | [**V0040StepTimeSystem**](V0040StepTimeSystem.md) |  | [optional] 
**total** | [**V0040StepTimeTotal**](V0040StepTimeTotal.md) |  | [optional] 
**user** | [**V0040StepTimeUser**](V0040StepTimeUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_step_time import V0042StepTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0042StepTime from a JSON string
v0042_step_time_instance = V0042StepTime.from_json(json)
# print the JSON string representation of the object
print(V0042StepTime.to_json())

# convert the object into a dict
v0042_step_time_dict = v0042_step_time_instance.to_dict()
# create an instance of V0042StepTime from a dict
v0042_step_time_from_dict = V0042StepTime.from_dict(v0042_step_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


