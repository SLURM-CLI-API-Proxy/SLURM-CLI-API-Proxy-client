# V0042AssocSharesObjWrap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Association ID | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**name** | **str** | Share name | [optional] 
**parent** | **str** | Parent name | [optional] 
**partition** | **str** | Partition name | [optional] 
**shares_normalized** | [**V0042Float64NoValStruct**](V0042Float64NoValStruct.md) |  | [optional] 
**shares** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**tres** | [**V0042AssocSharesObjWrapTres**](V0042AssocSharesObjWrapTres.md) |  | [optional] 
**effective_usage** | [**V0042Float64NoValStruct**](V0042Float64NoValStruct.md) |  | [optional] 
**usage_normalized** | [**V0042Float64NoValStruct**](V0042Float64NoValStruct.md) |  | [optional] 
**usage** | **int** | Measure of tresbillableunits usage | [optional] 
**fairshare** | [**V0042AssocSharesObjWrapFairshare**](V0042AssocSharesObjWrapFairshare.md) |  | [optional] 
**type** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.v0042_assoc_shares_obj_wrap import V0042AssocSharesObjWrap

# TODO update the JSON string below
json = "{}"
# create an instance of V0042AssocSharesObjWrap from a JSON string
v0042_assoc_shares_obj_wrap_instance = V0042AssocSharesObjWrap.from_json(json)
# print the JSON string representation of the object
print(V0042AssocSharesObjWrap.to_json())

# convert the object into a dict
v0042_assoc_shares_obj_wrap_dict = v0042_assoc_shares_obj_wrap_instance.to_dict()
# create an instance of V0042AssocSharesObjWrap from a dict
v0042_assoc_shares_obj_wrap_from_dict = V0042AssocSharesObjWrap.from_dict(v0042_assoc_shares_obj_wrap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


