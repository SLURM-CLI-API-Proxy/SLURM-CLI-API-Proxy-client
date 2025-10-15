# V0043AssocMaxTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0043Tres]**](V0043Tres.md) |  | [optional] 
**group** | [**V0043AssocMaxTresGroup**](V0043AssocMaxTresGroup.md) |  | [optional] 
**minutes** | [**V0043AssocMaxTresMinutes**](V0043AssocMaxTresMinutes.md) |  | [optional] 
**per** | [**V0043AssocMaxTresPer**](V0043AssocMaxTresPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_assoc_max_tres import V0043AssocMaxTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0043AssocMaxTres from a JSON string
v0043_assoc_max_tres_instance = V0043AssocMaxTres.from_json(json)
# print the JSON string representation of the object
print(V0043AssocMaxTres.to_json())

# convert the object into a dict
v0043_assoc_max_tres_dict = v0043_assoc_max_tres_instance.to_dict()
# create an instance of V0043AssocMaxTres from a dict
v0043_assoc_max_tres_from_dict = V0043AssocMaxTres.from_dict(v0043_assoc_max_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


