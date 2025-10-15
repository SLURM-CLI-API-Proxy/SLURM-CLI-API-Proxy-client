# V0041OpenapiSlurmdbdConfigRespClustersInnerAssociationsRoot

Root association information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account | [optional] 
**cluster** | **str** | Cluster | [optional] 
**partition** | **str** | Partition | [optional] 
**user** | **str** | User name | 
**id** | **int** | Numeric association ID | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_clusters_inner_associations_root import V0041OpenapiSlurmdbdConfigRespClustersInnerAssociationsRoot

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespClustersInnerAssociationsRoot from a JSON string
v0041_openapi_slurmdbd_config_resp_clusters_inner_associations_root_instance = V0041OpenapiSlurmdbdConfigRespClustersInnerAssociationsRoot.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespClustersInnerAssociationsRoot.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_clusters_inner_associations_root_dict = v0041_openapi_slurmdbd_config_resp_clusters_inner_associations_root_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespClustersInnerAssociationsRoot from a dict
v0041_openapi_slurmdbd_config_resp_clusters_inner_associations_root_from_dict = V0041OpenapiSlurmdbdConfigRespClustersInnerAssociationsRoot.from_dict(v0041_openapi_slurmdbd_config_resp_clusters_inner_associations_root_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


