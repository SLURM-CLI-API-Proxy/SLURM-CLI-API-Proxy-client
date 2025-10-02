# V0042ClusterRec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller** | [**V0040ClusterRecController**](V0040ClusterRecController.md) |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**name** | **str** | ClusterName | [optional] 
**nodes** | **str** | Node names | [optional] 
**select_plugin** | **str** |  | [optional] 
**associations** | [**V0042ClusterRecAssociations**](V0042ClusterRecAssociations.md) |  | [optional] 
**rpc_version** | **int** | RPC version used in the cluster | [optional] 
**tres** | [**List[V0042Tres]**](V0042Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_cluster_rec import V0042ClusterRec

# TODO update the JSON string below
json = "{}"
# create an instance of V0042ClusterRec from a JSON string
v0042_cluster_rec_instance = V0042ClusterRec.from_json(json)
# print the JSON string representation of the object
print(V0042ClusterRec.to_json())

# convert the object into a dict
v0042_cluster_rec_dict = v0042_cluster_rec_instance.to_dict()
# create an instance of V0042ClusterRec from a dict
v0042_cluster_rec_from_dict = V0042ClusterRec.from_dict(v0042_cluster_rec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


