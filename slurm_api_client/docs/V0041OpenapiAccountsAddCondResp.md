# V0041OpenapiAccountsAddCondResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_condition** | [**V0041OpenapiAccountsAddCondRespAssociationCondition**](V0041OpenapiAccountsAddCondRespAssociationCondition.md) |  | [optional] 
**account** | [**V0041OpenapiAccountsAddCondRespAccount**](V0041OpenapiAccountsAddCondRespAccount.md) |  | [optional] 
**meta** | [**V0041OpenapiSharesRespMeta**](V0041OpenapiSharesRespMeta.md) |  | [optional] 
**errors** | [**List[V0041OpenapiSharesRespErrorsInner]**](V0041OpenapiSharesRespErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[V0041OpenapiSharesRespWarningsInner]**](V0041OpenapiSharesRespWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_accounts_add_cond_resp import V0041OpenapiAccountsAddCondResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsAddCondResp from a JSON string
v0041_openapi_accounts_add_cond_resp_instance = V0041OpenapiAccountsAddCondResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsAddCondResp.to_json())

# convert the object into a dict
v0041_openapi_accounts_add_cond_resp_dict = v0041_openapi_accounts_add_cond_resp_instance.to_dict()
# create an instance of V0041OpenapiAccountsAddCondResp from a dict
v0041_openapi_accounts_add_cond_resp_from_dict = V0041OpenapiAccountsAddCondResp.from_dict(v0041_openapi_accounts_add_cond_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


