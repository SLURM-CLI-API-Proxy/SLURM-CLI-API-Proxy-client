# V0041OpenapiSlurmdbdConfigRespClustersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller** | [**V0040ClusterRecController**](V0040ClusterRecController.md) |  | [optional] 
**flags** | **List[str]** | Flags | [optional] 
**name** | **str** | ClusterName | [optional] 
**nodes** | **str** | Node names | [optional] 
**select_plugin** | **str** |  | [optional] 
**associations** | [**V0041OpenapiSlurmdbdConfigRespClustersInnerAssociations**](V0041OpenapiSlurmdbdConfigRespClustersInnerAssociations.md) |  | [optional] 
**rpc_version** | **int** | RPC version used in the cluster | [optional] 
**tres** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Trackable resources | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_clusters_inner import V0041OpenapiSlurmdbdConfigRespClustersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespClustersInner from a JSON string
v0041_openapi_slurmdbd_config_resp_clusters_inner_instance = V0041OpenapiSlurmdbdConfigRespClustersInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespClustersInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_clusters_inner_dict = v0041_openapi_slurmdbd_config_resp_clusters_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespClustersInner from a dict
v0041_openapi_slurmdbd_config_resp_clusters_inner_from_dict = V0041OpenapiSlurmdbdConfigRespClustersInner.from_dict(v0041_openapi_slurmdbd_config_resp_clusters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


