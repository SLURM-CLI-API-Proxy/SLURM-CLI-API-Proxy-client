# V0040OpenapiSlurmdbdConfigResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[V0040ClusterRec]**](V0040ClusterRec.md) |  | [optional] 
**tres** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**accounts** | [**List[V0040Account]**](V0040Account.md) |  | [optional] 
**users** | [**List[V0040User]**](V0040User.md) |  | [optional] 
**qos** | [**List[V0040Qos]**](V0040Qos.md) |  | [optional] 
**wckeys** | [**List[V0040Wckey]**](V0040Wckey.md) |  | [optional] 
**associations** | [**List[V0040Assoc]**](V0040Assoc.md) |  | [optional] 
**instances** | [**List[V0040Instance]**](V0040Instance.md) |  | [optional] 
**meta** | [**V0040OpenapiMeta**](V0040OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0040OpenapiError]**](V0040OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0040OpenapiWarning]**](V0040OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_openapi_slurmdbd_config_resp import V0040OpenapiSlurmdbdConfigResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0040OpenapiSlurmdbdConfigResp from a JSON string
v0040_openapi_slurmdbd_config_resp_instance = V0040OpenapiSlurmdbdConfigResp.from_json(json)
# print the JSON string representation of the object
print(V0040OpenapiSlurmdbdConfigResp.to_json())

# convert the object into a dict
v0040_openapi_slurmdbd_config_resp_dict = v0040_openapi_slurmdbd_config_resp_instance.to_dict()
# create an instance of V0040OpenapiSlurmdbdConfigResp from a dict
v0040_openapi_slurmdbd_config_resp_from_dict = V0040OpenapiSlurmdbdConfigResp.from_dict(v0040_openapi_slurmdbd_config_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


