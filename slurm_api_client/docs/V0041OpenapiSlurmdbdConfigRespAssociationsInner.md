# V0041OpenapiSlurmdbdConfigRespAssociationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting** | [**List[V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner]**](V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner.md) | Accounting records containing related resource usage | [optional] 
**account** | **str** | Account | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**comment** | **str** | Arbitrary comment | [optional] 
**default** | [**V0040AssocDefault**](V0040AssocDefault.md) |  | [optional] 
**flags** | **List[str]** | Flags on the association | [optional] 
**max** | [**V0041OpenapiSlurmdbdConfigRespAssociationsInnerMax**](V0041OpenapiSlurmdbdConfigRespAssociationsInnerMax.md) |  | [optional] 
**id** | **int** | Unique ID | [optional] 
**is_default** | **bool** | Is default association for user | [optional] 
**lineage** | **str** | Complete path up the hierarchy to the root association | [optional] 
**min** | [**V0041OpenapiSlurmdbdConfigRespAssociationsInnerMin**](V0041OpenapiSlurmdbdConfigRespAssociationsInnerMin.md) |  | [optional] 
**parent_account** | **str** | Name of parent account | [optional] 
**partition** | **str** | Partition name | [optional] 
**priority** | [**V0041OpenapiSlurmdbdConfigRespAssociationsInnerPriority**](V0041OpenapiSlurmdbdConfigRespAssociationsInnerPriority.md) |  | [optional] 
**qos** | **List[str]** | List of available QOS names | [optional] 
**shares_raw** | **int** | Allocated shares used for fairshare calculation | [optional] 
**user** | **str** | User name | 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_associations_inner import V0041OpenapiSlurmdbdConfigRespAssociationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInner from a JSON string
v0041_openapi_slurmdbd_config_resp_associations_inner_instance = V0041OpenapiSlurmdbdConfigRespAssociationsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespAssociationsInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_associations_inner_dict = v0041_openapi_slurmdbd_config_resp_associations_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInner from a dict
v0041_openapi_slurmdbd_config_resp_associations_inner_from_dict = V0041OpenapiSlurmdbdConfigRespAssociationsInner.from_dict(v0041_openapi_slurmdbd_config_resp_associations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


