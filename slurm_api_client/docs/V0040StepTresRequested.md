# V0040StepTresRequested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**min** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**average** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**total** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_step_tres_requested import V0040StepTresRequested

# TODO update the JSON string below
json = "{}"
# create an instance of V0040StepTresRequested from a JSON string
v0040_step_tres_requested_instance = V0040StepTresRequested.from_json(json)
# print the JSON string representation of the object
print(V0040StepTresRequested.to_json())

# convert the object into a dict
v0040_step_tres_requested_dict = v0040_step_tres_requested_instance.to_dict()
# create an instance of V0040StepTresRequested from a dict
v0040_step_tres_requested_from_dict = V0040StepTresRequested.from_dict(v0040_step_tres_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


