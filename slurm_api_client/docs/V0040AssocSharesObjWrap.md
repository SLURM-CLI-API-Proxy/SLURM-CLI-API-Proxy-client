# V0040AssocSharesObjWrap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Association ID | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**name** | **str** | Share name | [optional] 
**parent** | **str** | Parent name | [optional] 
**partition** | **str** | Partition name | [optional] 
**shares_normalized** | [**V0040Float64NoVal**](V0040Float64NoVal.md) |  | [optional] 
**shares** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**tres** | [**V0040AssocSharesObjWrapTres**](V0040AssocSharesObjWrapTres.md) |  | [optional] 
**effective_usage** | **float** | Effective, normalized usage | [optional] 
**usage_normalized** | [**V0040Float64NoVal**](V0040Float64NoVal.md) |  | [optional] 
**usage** | **int** | Measure of tresbillableunits usage | [optional] 
**fairshare** | [**V0040AssocSharesObjWrapFairshare**](V0040AssocSharesObjWrapFairshare.md) |  | [optional] 
**type** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.v0040_assoc_shares_obj_wrap import V0040AssocSharesObjWrap

# TODO update the JSON string below
json = "{}"
# create an instance of V0040AssocSharesObjWrap from a JSON string
v0040_assoc_shares_obj_wrap_instance = V0040AssocSharesObjWrap.from_json(json)
# print the JSON string representation of the object
print(V0040AssocSharesObjWrap.to_json())

# convert the object into a dict
v0040_assoc_shares_obj_wrap_dict = v0040_assoc_shares_obj_wrap_instance.to_dict()
# create an instance of V0040AssocSharesObjWrap from a dict
v0040_assoc_shares_obj_wrap_from_dict = V0040AssocSharesObjWrap.from_dict(v0040_assoc_shares_obj_wrap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


