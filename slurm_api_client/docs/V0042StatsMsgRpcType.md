# V0042StatsMsgRpcType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **int** | Message type as integer | 
**message_type** | **str** | Message type as string | 
**count** | **int** | Number of RPCs received | 
**queued** | **int** | Number of RPCs queued | 
**dropped** | **int** | Number of RPCs dropped | 
**cycle_last** | **int** | Number of RPCs processed within the last RPC queue cycle | 
**cycle_max** | **int** | Maximum number of RPCs processed within a RPC queue cycle since start | 
**total_time** | **int** | Total time spent processing RPC in seconds | 
**average_time** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | 

## Example

```python
from openapi_client.models.v0042_stats_msg_rpc_type import V0042StatsMsgRpcType

# TODO update the JSON string below
json = "{}"
# create an instance of V0042StatsMsgRpcType from a JSON string
v0042_stats_msg_rpc_type_instance = V0042StatsMsgRpcType.from_json(json)
# print the JSON string representation of the object
print(V0042StatsMsgRpcType.to_json())

# convert the object into a dict
v0042_stats_msg_rpc_type_dict = v0042_stats_msg_rpc_type_instance.to_dict()
# create an instance of V0042StatsMsgRpcType from a dict
v0042_stats_msg_rpc_type_from_dict = V0042StatsMsgRpcType.from_dict(v0042_stats_msg_rpc_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


