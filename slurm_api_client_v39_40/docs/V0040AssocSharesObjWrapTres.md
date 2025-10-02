# V0040AssocSharesObjWrapTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_seconds** | [**List[V0040SharesUint64Tres]**](V0040SharesUint64Tres.md) |  | [optional] 
**group_minutes** | [**List[V0040SharesUint64Tres]**](V0040SharesUint64Tres.md) |  | [optional] 
**usage** | [**List[V0040SharesFloat128Tres]**](V0040SharesFloat128Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_assoc_shares_obj_wrap_tres import V0040AssocSharesObjWrapTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0040AssocSharesObjWrapTres from a JSON string
v0040_assoc_shares_obj_wrap_tres_instance = V0040AssocSharesObjWrapTres.from_json(json)
# print the JSON string representation of the object
print(V0040AssocSharesObjWrapTres.to_json())

# convert the object into a dict
v0040_assoc_shares_obj_wrap_tres_dict = v0040_assoc_shares_obj_wrap_tres_instance.to_dict()
# create an instance of V0040AssocSharesObjWrapTres from a dict
v0040_assoc_shares_obj_wrap_tres_from_dict = V0040AssocSharesObjWrapTres.from_dict(v0040_assoc_shares_obj_wrap_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


