# V0041OpenapiSlurmdbdConfigResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[V0041OpenapiSlurmdbdConfigRespClustersInner]**](V0041OpenapiSlurmdbdConfigRespClustersInner.md) | Clusters | [optional] 
**tres** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | TRES | [optional] 
**accounts** | [**List[V0041OpenapiSlurmdbdConfigRespAccountsInner]**](V0041OpenapiSlurmdbdConfigRespAccountsInner.md) | Accounts | [optional] 
**users** | [**List[V0041OpenapiSlurmdbdConfigRespUsersInner]**](V0041OpenapiSlurmdbdConfigRespUsersInner.md) | Users | [optional] 
**qos** | [**List[V0041OpenapiSlurmdbdConfigRespQosInner]**](V0041OpenapiSlurmdbdConfigRespQosInner.md) | QOS | [optional] 
**wckeys** | [**List[V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner]**](V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner.md) | WCKeys | [optional] 
**associations** | [**List[V0041OpenapiSlurmdbdConfigRespAssociationsInner]**](V0041OpenapiSlurmdbdConfigRespAssociationsInner.md) | Associations | [optional] 
**instances** | [**List[V0041OpenapiSlurmdbdConfigRespInstancesInner]**](V0041OpenapiSlurmdbdConfigRespInstancesInner.md) | Instances | [optional] 
**meta** | [**V0041OpenapiSharesRespMeta**](V0041OpenapiSharesRespMeta.md) |  | [optional] 
**errors** | [**List[V0041OpenapiSharesRespErrorsInner]**](V0041OpenapiSharesRespErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[V0041OpenapiSharesRespWarningsInner]**](V0041OpenapiSharesRespWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp import V0041OpenapiSlurmdbdConfigResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigResp from a JSON string
v0041_openapi_slurmdbd_config_resp_instance = V0041OpenapiSlurmdbdConfigResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigResp.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_dict = v0041_openapi_slurmdbd_config_resp_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigResp from a dict
v0041_openapi_slurmdbd_config_resp_from_dict = V0041OpenapiSlurmdbdConfigResp.from_dict(v0041_openapi_slurmdbd_config_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


