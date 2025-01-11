# V0040StepTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested** | [**V0040StepTresRequested**](V0040StepTresRequested.md) |  | [optional] 
**consumed** | [**V0040StepTresConsumed**](V0040StepTresConsumed.md) |  | [optional] 
**allocated** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_step_tres import V0040StepTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0040StepTres from a JSON string
v0040_step_tres_instance = V0040StepTres.from_json(json)
# print the JSON string representation of the object
print(V0040StepTres.to_json())

# convert the object into a dict
v0040_step_tres_dict = v0040_step_tres_instance.to_dict()
# create an instance of V0040StepTres from a dict
v0040_step_tres_from_dict = V0040StepTres.from_dict(v0040_step_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


