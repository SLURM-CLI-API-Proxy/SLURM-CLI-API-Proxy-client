# V0039AssocMaxTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0039Tres]**](V0039Tres.md) |  | [optional] 
**minutes** | [**V0039AssocMaxTresMinutes**](V0039AssocMaxTresMinutes.md) |  | [optional] 
**group** | [**V0039AssocMaxTresGroup**](V0039AssocMaxTresGroup.md) |  | [optional] 
**per** | [**V0039AssocMaxTresPer**](V0039AssocMaxTresPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_assoc_max_tres import V0039AssocMaxTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0039AssocMaxTres from a JSON string
v0039_assoc_max_tres_instance = V0039AssocMaxTres.from_json(json)
# print the JSON string representation of the object
print(V0039AssocMaxTres.to_json())

# convert the object into a dict
v0039_assoc_max_tres_dict = v0039_assoc_max_tres_instance.to_dict()
# create an instance of V0039AssocMaxTres from a dict
v0039_assoc_max_tres_from_dict = V0039AssocMaxTres.from_dict(v0039_assoc_max_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


