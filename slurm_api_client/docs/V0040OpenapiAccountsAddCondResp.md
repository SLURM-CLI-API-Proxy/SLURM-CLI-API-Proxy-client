# V0040OpenapiAccountsAddCondResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_condition** | [**V0040AccountsAddCond**](V0040AccountsAddCond.md) |  | [optional] 
**account** | [**V0040AccountShort**](V0040AccountShort.md) |  | [optional] 
**meta** | [**V0040OpenapiMeta**](V0040OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0040OpenapiError]**](V0040OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0040OpenapiWarning]**](V0040OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_openapi_accounts_add_cond_resp import V0040OpenapiAccountsAddCondResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0040OpenapiAccountsAddCondResp from a JSON string
v0040_openapi_accounts_add_cond_resp_instance = V0040OpenapiAccountsAddCondResp.from_json(json)
# print the JSON string representation of the object
print(V0040OpenapiAccountsAddCondResp.to_json())

# convert the object into a dict
v0040_openapi_accounts_add_cond_resp_dict = v0040_openapi_accounts_add_cond_resp_instance.to_dict()
# create an instance of V0040OpenapiAccountsAddCondResp from a dict
v0040_openapi_accounts_add_cond_resp_from_dict = V0040OpenapiAccountsAddCondResp.from_dict(v0040_openapi_accounts_add_cond_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


