# V0043AssocSharesObjWrapTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_seconds** | [**List[V0043SharesUint64Tres]**](V0043SharesUint64Tres.md) |  | [optional] 
**group_minutes** | [**List[V0043SharesUint64Tres]**](V0043SharesUint64Tres.md) |  | [optional] 
**usage** | [**List[V0043SharesFloat128Tres]**](V0043SharesFloat128Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_assoc_shares_obj_wrap_tres import V0043AssocSharesObjWrapTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0043AssocSharesObjWrapTres from a JSON string
v0043_assoc_shares_obj_wrap_tres_instance = V0043AssocSharesObjWrapTres.from_json(json)
# print the JSON string representation of the object
print(V0043AssocSharesObjWrapTres.to_json())

# convert the object into a dict
v0043_assoc_shares_obj_wrap_tres_dict = v0043_assoc_shares_obj_wrap_tres_instance.to_dict()
# create an instance of V0043AssocSharesObjWrapTres from a dict
v0043_assoc_shares_obj_wrap_tres_from_dict = V0043AssocSharesObjWrapTres.from_dict(v0043_assoc_shares_obj_wrap_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


