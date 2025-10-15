# V0043OpenapiAccountsRemovedResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**removed_accounts** | **List[str]** |  | 
**meta** | [**V0043OpenapiMeta**](V0043OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0043OpenapiError]**](V0043OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0043OpenapiWarning]**](V0043OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_openapi_accounts_removed_resp import V0043OpenapiAccountsRemovedResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0043OpenapiAccountsRemovedResp from a JSON string
v0043_openapi_accounts_removed_resp_instance = V0043OpenapiAccountsRemovedResp.from_json(json)
# print the JSON string representation of the object
print(V0043OpenapiAccountsRemovedResp.to_json())

# convert the object into a dict
v0043_openapi_accounts_removed_resp_dict = v0043_openapi_accounts_removed_resp_instance.to_dict()
# create an instance of V0043OpenapiAccountsRemovedResp from a dict
v0043_openapi_accounts_removed_resp_from_dict = V0043OpenapiAccountsRemovedResp.from_dict(v0043_openapi_accounts_removed_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


