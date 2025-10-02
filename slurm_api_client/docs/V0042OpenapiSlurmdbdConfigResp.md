# V0042OpenapiSlurmdbdConfigResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[V0042ClusterRec]**](V0042ClusterRec.md) |  | [optional] 
**tres** | [**List[V0042Tres]**](V0042Tres.md) |  | [optional] 
**accounts** | [**List[V0042Account]**](V0042Account.md) |  | [optional] 
**users** | [**List[V0042User]**](V0042User.md) |  | [optional] 
**qos** | [**List[V0042Qos]**](V0042Qos.md) |  | [optional] 
**wckeys** | [**List[V0042Wckey]**](V0042Wckey.md) |  | [optional] 
**associations** | [**List[V0042Assoc]**](V0042Assoc.md) |  | [optional] 
**instances** | [**List[V0042Instance]**](V0042Instance.md) |  | [optional] 
**meta** | [**V0042OpenapiMeta**](V0042OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0042OpenapiError]**](V0042OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0042OpenapiWarning]**](V0042OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_openapi_slurmdbd_config_resp import V0042OpenapiSlurmdbdConfigResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0042OpenapiSlurmdbdConfigResp from a JSON string
v0042_openapi_slurmdbd_config_resp_instance = V0042OpenapiSlurmdbdConfigResp.from_json(json)
# print the JSON string representation of the object
print(V0042OpenapiSlurmdbdConfigResp.to_json())

# convert the object into a dict
v0042_openapi_slurmdbd_config_resp_dict = v0042_openapi_slurmdbd_config_resp_instance.to_dict()
# create an instance of V0042OpenapiSlurmdbdConfigResp from a dict
v0042_openapi_slurmdbd_config_resp_from_dict = V0042OpenapiSlurmdbdConfigResp.from_dict(v0042_openapi_slurmdbd_config_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


