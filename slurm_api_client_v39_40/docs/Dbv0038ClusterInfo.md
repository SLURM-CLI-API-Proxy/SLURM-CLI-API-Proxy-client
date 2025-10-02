# Dbv0038ClusterInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller** | [**Dbv0038ClusterInfoController**](Dbv0038ClusterInfoController.md) |  | [optional] 
**flags** | **List[str]** | List of properties of cluster | [optional] 
**name** | **str** | Cluster name | [optional] 
**nodes** | **str** | Assigned nodes | [optional] 
**select_plugin** | **str** | Configured select plugin | [optional] 
**associations** | [**Dbv0038ClusterInfoAssociations**](Dbv0038ClusterInfoAssociations.md) |  | [optional] 
**rpc_version** | **int** | Number rpc version | [optional] 
**tres** | [**List[Dbv0038ResponseTres]**](Dbv0038ResponseTres.md) | List of TRES in cluster | [optional] 

## Example

```python
from openapi_client.models.dbv0038_cluster_info import Dbv0038ClusterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038ClusterInfo from a JSON string
dbv0038_cluster_info_instance = Dbv0038ClusterInfo.from_json(json)
# print the JSON string representation of the object
print(Dbv0038ClusterInfo.to_json())

# convert the object into a dict
dbv0038_cluster_info_dict = dbv0038_cluster_info_instance.to_dict()
# create an instance of Dbv0038ClusterInfo from a dict
dbv0038_cluster_info_from_dict = Dbv0038ClusterInfo.from_dict(dbv0038_cluster_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


