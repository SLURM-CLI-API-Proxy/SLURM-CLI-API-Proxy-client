# V0040OpenapiSharesResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares** | [**V0040SharesRespMsg**](V0040SharesRespMsg.md) |  | 
**meta** | [**V0040OpenapiMeta**](V0040OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0040OpenapiError]**](V0040OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0040OpenapiWarning]**](V0040OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_openapi_shares_resp import V0040OpenapiSharesResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0040OpenapiSharesResp from a JSON string
v0040_openapi_shares_resp_instance = V0040OpenapiSharesResp.from_json(json)
# print the JSON string representation of the object
print(V0040OpenapiSharesResp.to_json())

# convert the object into a dict
v0040_openapi_shares_resp_dict = v0040_openapi_shares_resp_instance.to_dict()
# create an instance of V0040OpenapiSharesResp from a dict
v0040_openapi_shares_resp_from_dict = V0040OpenapiSharesResp.from_dict(v0040_openapi_shares_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


