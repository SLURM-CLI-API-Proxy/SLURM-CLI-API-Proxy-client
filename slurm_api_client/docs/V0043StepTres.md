# V0043StepTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested** | [**V0043StepTresRequested**](V0043StepTresRequested.md) |  | [optional] 
**consumed** | [**V0043StepTresConsumed**](V0043StepTresConsumed.md) |  | [optional] 
**allocated** | [**List[V0043Tres]**](V0043Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_step_tres import V0043StepTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0043StepTres from a JSON string
v0043_step_tres_instance = V0043StepTres.from_json(json)
# print the JSON string representation of the object
print(V0043StepTres.to_json())

# convert the object into a dict
v0043_step_tres_dict = v0043_step_tres_instance.to_dict()
# create an instance of V0043StepTres from a dict
v0043_step_tres_from_dict = V0043StepTres.from_dict(v0043_step_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


