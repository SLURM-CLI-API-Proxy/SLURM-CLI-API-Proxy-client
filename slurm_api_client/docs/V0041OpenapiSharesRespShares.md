# V0041OpenapiSharesRespShares

fairshare info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares** | [**List[V0041OpenapiSharesRespSharesSharesInner]**](V0041OpenapiSharesRespSharesSharesInner.md) | Association shares | [optional] 
**total_shares** | **int** | Total number of shares | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_shares_resp_shares import V0041OpenapiSharesRespShares

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSharesRespShares from a JSON string
v0041_openapi_shares_resp_shares_instance = V0041OpenapiSharesRespShares.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSharesRespShares.to_json())

# convert the object into a dict
v0041_openapi_shares_resp_shares_dict = v0041_openapi_shares_resp_shares_instance.to_dict()
# create an instance of V0041OpenapiSharesRespShares from a dict
v0041_openapi_shares_resp_shares_from_dict = V0041OpenapiSharesRespShares.from_dict(v0041_openapi_shares_resp_shares_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


