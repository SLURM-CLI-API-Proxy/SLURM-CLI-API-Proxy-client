# V0043StatsMsgRpcQueue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **int** | Message type as integer | 
**message_type** | **str** | Message type as string (Slurm RPC message type) | 
**count** | **int** | Number of pending RPCs queued | 

## Example

```python
from openapi_client.models.v0043_stats_msg_rpc_queue import V0043StatsMsgRpcQueue

# TODO update the JSON string below
json = "{}"
# create an instance of V0043StatsMsgRpcQueue from a JSON string
v0043_stats_msg_rpc_queue_instance = V0043StatsMsgRpcQueue.from_json(json)
# print the JSON string representation of the object
print(V0043StatsMsgRpcQueue.to_json())

# convert the object into a dict
v0043_stats_msg_rpc_queue_dict = v0043_stats_msg_rpc_queue_instance.to_dict()
# create an instance of V0043StatsMsgRpcQueue from a dict
v0043_stats_msg_rpc_queue_from_dict = V0043StatsMsgRpcQueue.from_dict(v0043_stats_msg_rpc_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


