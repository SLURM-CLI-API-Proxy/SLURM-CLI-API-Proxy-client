# V0040AssocSharesObjWrapFairshare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor** | **float** | Fairshare factor | [optional] 
**level** | **float** | Fairshare factor at this level; stored on an assoc as a long double, but that is not needed for display in sshare | [optional] 

## Example

```python
from openapi_client.models.v0040_assoc_shares_obj_wrap_fairshare import V0040AssocSharesObjWrapFairshare

# TODO update the JSON string below
json = "{}"
# create an instance of V0040AssocSharesObjWrapFairshare from a JSON string
v0040_assoc_shares_obj_wrap_fairshare_instance = V0040AssocSharesObjWrapFairshare.from_json(json)
# print the JSON string representation of the object
print(V0040AssocSharesObjWrapFairshare.to_json())

# convert the object into a dict
v0040_assoc_shares_obj_wrap_fairshare_dict = v0040_assoc_shares_obj_wrap_fairshare_instance.to_dict()
# create an instance of V0040AssocSharesObjWrapFairshare from a dict
v0040_assoc_shares_obj_wrap_fairshare_from_dict = V0040AssocSharesObjWrapFairshare.from_dict(v0040_assoc_shares_obj_wrap_fairshare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


