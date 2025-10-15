# V0043OpenapiSlurmdbdConfigResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[V0043ClusterRec]**](V0043ClusterRec.md) |  | [optional] 
**tres** | [**List[V0043Tres]**](V0043Tres.md) |  | [optional] 
**accounts** | [**List[V0043Account]**](V0043Account.md) |  | [optional] 
**users** | [**List[V0043User]**](V0043User.md) |  | [optional] 
**qos** | [**List[V0043Qos]**](V0043Qos.md) |  | [optional] 
**wckeys** | [**List[V0043Wckey]**](V0043Wckey.md) |  | [optional] 
**associations** | [**List[V0043Assoc]**](V0043Assoc.md) |  | [optional] 
**instances** | [**List[V0043Instance]**](V0043Instance.md) |  | [optional] 
**meta** | [**V0043OpenapiMeta**](V0043OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0043OpenapiError]**](V0043OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0043OpenapiWarning]**](V0043OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_openapi_slurmdbd_config_resp import V0043OpenapiSlurmdbdConfigResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0043OpenapiSlurmdbdConfigResp from a JSON string
v0043_openapi_slurmdbd_config_resp_instance = V0043OpenapiSlurmdbdConfigResp.from_json(json)
# print the JSON string representation of the object
print(V0043OpenapiSlurmdbdConfigResp.to_json())

# convert the object into a dict
v0043_openapi_slurmdbd_config_resp_dict = v0043_openapi_slurmdbd_config_resp_instance.to_dict()
# create an instance of V0043OpenapiSlurmdbdConfigResp from a dict
v0043_openapi_slurmdbd_config_resp_from_dict = V0043OpenapiSlurmdbdConfigResp.from_dict(v0043_openapi_slurmdbd_config_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


