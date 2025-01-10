# V0039StepTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** |  | [optional] 
**end** | **int** |  | [optional] 
**start** | **int** |  | [optional] 
**suspended** | **int** |  | [optional] 
**system** | [**V0039StepTimeSystem**](V0039StepTimeSystem.md) |  | [optional] 
**total** | [**V0039StepTimeSystem**](V0039StepTimeSystem.md) |  | [optional] 
**user** | [**V0039StepTimeSystem**](V0039StepTimeSystem.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_step_time import V0039StepTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0039StepTime from a JSON string
v0039_step_time_instance = V0039StepTime.from_json(json)
# print the JSON string representation of the object
print(V0039StepTime.to_json())

# convert the object into a dict
v0039_step_time_dict = v0039_step_time_instance.to_dict()
# create an instance of V0039StepTime from a dict
v0039_step_time_from_dict = V0039StepTime.from_dict(v0039_step_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


