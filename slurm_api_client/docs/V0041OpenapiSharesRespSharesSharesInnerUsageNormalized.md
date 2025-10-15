# V0041OpenapiSharesRespSharesSharesInnerUsageNormalized

Normalized usage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **float** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_shares_resp_shares_shares_inner_usage_normalized import V0041OpenapiSharesRespSharesSharesInnerUsageNormalized

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSharesRespSharesSharesInnerUsageNormalized from a JSON string
v0041_openapi_shares_resp_shares_shares_inner_usage_normalized_instance = V0041OpenapiSharesRespSharesSharesInnerUsageNormalized.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSharesRespSharesSharesInnerUsageNormalized.to_json())

# convert the object into a dict
v0041_openapi_shares_resp_shares_shares_inner_usage_normalized_dict = v0041_openapi_shares_resp_shares_shares_inner_usage_normalized_instance.to_dict()
# create an instance of V0041OpenapiSharesRespSharesSharesInnerUsageNormalized from a dict
v0041_openapi_shares_resp_shares_shares_inner_usage_normalized_from_dict = V0041OpenapiSharesRespSharesSharesInnerUsageNormalized.from_dict(v0041_openapi_shares_resp_shares_shares_inner_usage_normalized_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


