# V0043AssocSharesObjWrap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Association ID | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**name** | **str** | Share name | [optional] 
**parent** | **str** | Parent name | [optional] 
**partition** | **str** | Partition name | [optional] 
**shares_normalized** | [**V0043Float64NoValStruct**](V0043Float64NoValStruct.md) |  | [optional] 
**shares** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**tres** | [**V0043AssocSharesObjWrapTres**](V0043AssocSharesObjWrapTres.md) |  | [optional] 
**effective_usage** | [**V0043Float64NoValStruct**](V0043Float64NoValStruct.md) |  | [optional] 
**usage_normalized** | [**V0043Float64NoValStruct**](V0043Float64NoValStruct.md) |  | [optional] 
**usage** | **int** | Measure of tresbillableunits usage | [optional] 
**fairshare** | [**V0043AssocSharesObjWrapFairshare**](V0043AssocSharesObjWrapFairshare.md) |  | [optional] 
**type** | **List[str]** | User or account association | [optional] 

## Example

```python
from openapi_client.models.v0043_assoc_shares_obj_wrap import V0043AssocSharesObjWrap

# TODO update the JSON string below
json = "{}"
# create an instance of V0043AssocSharesObjWrap from a JSON string
v0043_assoc_shares_obj_wrap_instance = V0043AssocSharesObjWrap.from_json(json)
# print the JSON string representation of the object
print(V0043AssocSharesObjWrap.to_json())

# convert the object into a dict
v0043_assoc_shares_obj_wrap_dict = v0043_assoc_shares_obj_wrap_instance.to_dict()
# create an instance of V0043AssocSharesObjWrap from a dict
v0043_assoc_shares_obj_wrap_from_dict = V0043AssocSharesObjWrap.from_dict(v0043_assoc_shares_obj_wrap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


