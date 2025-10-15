# V0041OpenapiAccountsAddCondRespAccount

Account organization and description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Arbitrary string describing the account | [optional] 
**organization** | **str** | Organization to which the account belongs | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_accounts_add_cond_resp_account import V0041OpenapiAccountsAddCondRespAccount

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsAddCondRespAccount from a JSON string
v0041_openapi_accounts_add_cond_resp_account_instance = V0041OpenapiAccountsAddCondRespAccount.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsAddCondRespAccount.to_json())

# convert the object into a dict
v0041_openapi_accounts_add_cond_resp_account_dict = v0041_openapi_accounts_add_cond_resp_account_instance.to_dict()
# create an instance of V0041OpenapiAccountsAddCondRespAccount from a dict
v0041_openapi_accounts_add_cond_resp_account_from_dict = V0041OpenapiAccountsAddCondRespAccount.from_dict(v0041_openapi_accounts_add_cond_resp_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


