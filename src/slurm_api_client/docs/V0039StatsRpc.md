# V0039StatsRpc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rpc** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**time** | [**V0039StatsRpcTime**](V0039StatsRpcTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_stats_rpc import V0039StatsRpc

# TODO update the JSON string below
json = "{}"
# create an instance of V0039StatsRpc from a JSON string
v0039_stats_rpc_instance = V0039StatsRpc.from_json(json)
# print the JSON string representation of the object
print(V0039StatsRpc.to_json())

# convert the object into a dict
v0039_stats_rpc_dict = v0039_stats_rpc_instance.to_dict()
# create an instance of V0039StatsRpc from a dict
v0039_stats_rpc_from_dict = V0039StatsRpc.from_dict(v0039_stats_rpc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


