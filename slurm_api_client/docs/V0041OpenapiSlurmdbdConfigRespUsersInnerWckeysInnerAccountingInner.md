# V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**V0040AccountingAllocated**](V0040AccountingAllocated.md) |  | [optional] 
**id** | **int** | Association ID or Workload characterization key ID | [optional] 
**start** | **int** | When the record was started | [optional] 
**tres** | [**V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInnerTRES**](V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInnerTRES.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner import V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner from a JSON string
v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner_instance = V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner_dict = v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner from a dict
v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner_from_dict = V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner.from_dict(v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


