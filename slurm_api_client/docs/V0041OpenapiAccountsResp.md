# V0041OpenapiAccountsResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[V0041OpenapiSlurmdbdConfigRespAccountsInner]**](V0041OpenapiSlurmdbdConfigRespAccountsInner.md) | accounts | 
**meta** | [**V0041OpenapiSharesRespMeta**](V0041OpenapiSharesRespMeta.md) |  | [optional] 
**errors** | [**List[V0041OpenapiSharesRespErrorsInner]**](V0041OpenapiSharesRespErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[V0041OpenapiSharesRespWarningsInner]**](V0041OpenapiSharesRespWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_accounts_resp import V0041OpenapiAccountsResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsResp from a JSON string
v0041_openapi_accounts_resp_instance = V0041OpenapiAccountsResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsResp.to_json())

# convert the object into a dict
v0041_openapi_accounts_resp_dict = v0041_openapi_accounts_resp_instance.to_dict()
# create an instance of V0041OpenapiAccountsResp from a dict
v0041_openapi_accounts_resp_from_dict = V0041OpenapiAccountsResp.from_dict(v0041_openapi_accounts_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


