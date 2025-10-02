# V0040AssocMaxTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**group** | [**V0040AssocMaxTresGroup**](V0040AssocMaxTresGroup.md) |  | [optional] 
**minutes** | [**V0040AssocMaxTresMinutes**](V0040AssocMaxTresMinutes.md) |  | [optional] 
**per** | [**V0040AssocMaxTresPer**](V0040AssocMaxTresPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_assoc_max_tres import V0040AssocMaxTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0040AssocMaxTres from a JSON string
v0040_assoc_max_tres_instance = V0040AssocMaxTres.from_json(json)
# print the JSON string representation of the object
print(V0040AssocMaxTres.to_json())

# convert the object into a dict
v0040_assoc_max_tres_dict = v0040_assoc_max_tres_instance.to_dict()
# create an instance of V0040AssocMaxTres from a dict
v0040_assoc_max_tres_from_dict = V0040AssocMaxTres.from_dict(v0040_assoc_max_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


