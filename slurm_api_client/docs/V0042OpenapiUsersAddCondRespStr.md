# V0042OpenapiUsersAddCondRespStr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_users** | **str** | added_users | 
**meta** | [**V0042OpenapiMeta**](V0042OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0042OpenapiError]**](V0042OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0042OpenapiWarning]**](V0042OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_openapi_users_add_cond_resp_str import V0042OpenapiUsersAddCondRespStr

# TODO update the JSON string below
json = "{}"
# create an instance of V0042OpenapiUsersAddCondRespStr from a JSON string
v0042_openapi_users_add_cond_resp_str_instance = V0042OpenapiUsersAddCondRespStr.from_json(json)
# print the JSON string representation of the object
print(V0042OpenapiUsersAddCondRespStr.to_json())

# convert the object into a dict
v0042_openapi_users_add_cond_resp_str_dict = v0042_openapi_users_add_cond_resp_str_instance.to_dict()
# create an instance of V0042OpenapiUsersAddCondRespStr from a dict
v0042_openapi_users_add_cond_resp_str_from_dict = V0042OpenapiUsersAddCondRespStr.from_dict(v0042_openapi_users_add_cond_resp_str_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


