# V0040OpenapiAccountsAddCondRespStr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_accounts** | **str** | added_accounts | 
**meta** | [**V0040OpenapiMeta**](V0040OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0040OpenapiError]**](V0040OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0040OpenapiWarning]**](V0040OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_openapi_accounts_add_cond_resp_str import V0040OpenapiAccountsAddCondRespStr

# TODO update the JSON string below
json = "{}"
# create an instance of V0040OpenapiAccountsAddCondRespStr from a JSON string
v0040_openapi_accounts_add_cond_resp_str_instance = V0040OpenapiAccountsAddCondRespStr.from_json(json)
# print the JSON string representation of the object
print(V0040OpenapiAccountsAddCondRespStr.to_json())

# convert the object into a dict
v0040_openapi_accounts_add_cond_resp_str_dict = v0040_openapi_accounts_add_cond_resp_str_instance.to_dict()
# create an instance of V0040OpenapiAccountsAddCondRespStr from a dict
v0040_openapi_accounts_add_cond_resp_str_from_dict = V0040OpenapiAccountsAddCondRespStr.from_dict(v0040_openapi_accounts_add_cond_resp_str_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


