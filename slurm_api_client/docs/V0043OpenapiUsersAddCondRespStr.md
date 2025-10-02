# V0043OpenapiUsersAddCondRespStr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_users** | **str** | added_users | 
**meta** | [**V0043OpenapiMeta**](V0043OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0043OpenapiError]**](V0043OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0043OpenapiWarning]**](V0043OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_openapi_users_add_cond_resp_str import V0043OpenapiUsersAddCondRespStr

# TODO update the JSON string below
json = "{}"
# create an instance of V0043OpenapiUsersAddCondRespStr from a JSON string
v0043_openapi_users_add_cond_resp_str_instance = V0043OpenapiUsersAddCondRespStr.from_json(json)
# print the JSON string representation of the object
print(V0043OpenapiUsersAddCondRespStr.to_json())

# convert the object into a dict
v0043_openapi_users_add_cond_resp_str_dict = v0043_openapi_users_add_cond_resp_str_instance.to_dict()
# create an instance of V0043OpenapiUsersAddCondRespStr from a dict
v0043_openapi_users_add_cond_resp_str_from_dict = V0043OpenapiUsersAddCondRespStr.from_dict(v0043_openapi_users_add_cond_resp_str_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


