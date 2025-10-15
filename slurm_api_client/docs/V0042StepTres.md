# V0042StepTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested** | [**V0042StepTresRequested**](V0042StepTresRequested.md) |  | [optional] 
**consumed** | [**V0042StepTresConsumed**](V0042StepTresConsumed.md) |  | [optional] 
**allocated** | [**List[V0042Tres]**](V0042Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_step_tres import V0042StepTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0042StepTres from a JSON string
v0042_step_tres_instance = V0042StepTres.from_json(json)
# print the JSON string representation of the object
print(V0042StepTres.to_json())

# convert the object into a dict
v0042_step_tres_dict = v0042_step_tres_instance.to_dict()
# create an instance of V0042StepTres from a dict
v0042_step_tres_from_dict = V0042StepTres.from_dict(v0042_step_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


