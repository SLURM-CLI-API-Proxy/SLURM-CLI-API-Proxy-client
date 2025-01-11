# V0040ClusterRec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller** | [**V0039ClusterRecController**](V0039ClusterRecController.md) |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**nodes** | **str** |  | [optional] 
**select_plugin** | **str** |  | [optional] 
**associations** | [**V0040ClusterRecAssociations**](V0040ClusterRecAssociations.md) |  | [optional] 
**rpc_version** | **int** |  | [optional] 
**tres** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_cluster_rec import V0040ClusterRec

# TODO update the JSON string below
json = "{}"
# create an instance of V0040ClusterRec from a JSON string
v0040_cluster_rec_instance = V0040ClusterRec.from_json(json)
# print the JSON string representation of the object
print(V0040ClusterRec.to_json())

# convert the object into a dict
v0040_cluster_rec_dict = v0040_cluster_rec_instance.to_dict()
# create an instance of V0040ClusterRec from a dict
v0040_cluster_rec_from_dict = V0040ClusterRec.from_dict(v0040_cluster_rec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


