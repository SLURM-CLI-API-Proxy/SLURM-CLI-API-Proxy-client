# V0042AssocSharesObjWrapTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_seconds** | [**List[V0042SharesUint64Tres]**](V0042SharesUint64Tres.md) |  | [optional] 
**group_minutes** | [**List[V0042SharesUint64Tres]**](V0042SharesUint64Tres.md) |  | [optional] 
**usage** | [**List[V0042SharesFloat128Tres]**](V0042SharesFloat128Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_assoc_shares_obj_wrap_tres import V0042AssocSharesObjWrapTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0042AssocSharesObjWrapTres from a JSON string
v0042_assoc_shares_obj_wrap_tres_instance = V0042AssocSharesObjWrapTres.from_json(json)
# print the JSON string representation of the object
print(V0042AssocSharesObjWrapTres.to_json())

# convert the object into a dict
v0042_assoc_shares_obj_wrap_tres_dict = v0042_assoc_shares_obj_wrap_tres_instance.to_dict()
# create an instance of V0042AssocSharesObjWrapTres from a dict
v0042_assoc_shares_obj_wrap_tres_from_dict = V0042AssocSharesObjWrapTres.from_dict(v0042_assoc_shares_obj_wrap_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


