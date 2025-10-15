# V0043OpenapiUsersAddCondResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_condition** | [**V0043UsersAddCond**](V0043UsersAddCond.md) |  | 
**user** | [**V0043UserShort**](V0043UserShort.md) |  | 
**meta** | [**V0043OpenapiMeta**](V0043OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0043OpenapiError]**](V0043OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0043OpenapiWarning]**](V0043OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_openapi_users_add_cond_resp import V0043OpenapiUsersAddCondResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0043OpenapiUsersAddCondResp from a JSON string
v0043_openapi_users_add_cond_resp_instance = V0043OpenapiUsersAddCondResp.from_json(json)
# print the JSON string representation of the object
print(V0043OpenapiUsersAddCondResp.to_json())

# convert the object into a dict
v0043_openapi_users_add_cond_resp_dict = v0043_openapi_users_add_cond_resp_instance.to_dict()
# create an instance of V0043OpenapiUsersAddCondResp from a dict
v0043_openapi_users_add_cond_resp_from_dict = V0043OpenapiUsersAddCondResp.from_dict(v0043_openapi_users_add_cond_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


