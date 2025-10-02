# V0042OpenapiAccountsAddCondResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_condition** | [**V0042AccountsAddCond**](V0042AccountsAddCond.md) |  | [optional] 
**account** | [**V0042AccountShort**](V0042AccountShort.md) |  | [optional] 
**meta** | [**V0042OpenapiMeta**](V0042OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0042OpenapiError]**](V0042OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0042OpenapiWarning]**](V0042OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_openapi_accounts_add_cond_resp import V0042OpenapiAccountsAddCondResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0042OpenapiAccountsAddCondResp from a JSON string
v0042_openapi_accounts_add_cond_resp_instance = V0042OpenapiAccountsAddCondResp.from_json(json)
# print the JSON string representation of the object
print(V0042OpenapiAccountsAddCondResp.to_json())

# convert the object into a dict
v0042_openapi_accounts_add_cond_resp_dict = v0042_openapi_accounts_add_cond_resp_instance.to_dict()
# create an instance of V0042OpenapiAccountsAddCondResp from a dict
v0042_openapi_accounts_add_cond_resp_from_dict = V0042OpenapiAccountsAddCondResp.from_dict(v0042_openapi_accounts_add_cond_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


