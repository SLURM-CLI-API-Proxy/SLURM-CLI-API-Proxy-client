# V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting** | [**List[V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner]**](V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInnerAccountingInner.md) | Accounting records containing related resource usage | [optional] 
**cluster** | **str** | Cluster name | 
**id** | **int** | Unique ID for this user-cluster-wckey combination | [optional] 
**name** | **str** | WCKey name | 
**user** | **str** | User name | 
**flags** | **List[str]** | Flags associated with the WCKey | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner import V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner from a JSON string
v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_instance = V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_dict = v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner from a dict
v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_from_dict = V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner.from_dict(v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


