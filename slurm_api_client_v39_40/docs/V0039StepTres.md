# V0039StepTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested** | [**V0039StepTresRequested**](V0039StepTresRequested.md) |  | [optional] 
**consumed** | [**V0039StepTresConsumed**](V0039StepTresConsumed.md) |  | [optional] 
**allocated** | [**List[V0039Tres]**](V0039Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_step_tres import V0039StepTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0039StepTres from a JSON string
v0039_step_tres_instance = V0039StepTres.from_json(json)
# print the JSON string representation of the object
print(V0039StepTres.to_json())

# convert the object into a dict
v0039_step_tres_dict = v0039_step_tres_instance.to_dict()
# create an instance of V0039StepTres from a dict
v0039_step_tres_from_dict = V0039StepTres.from_dict(v0039_step_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


