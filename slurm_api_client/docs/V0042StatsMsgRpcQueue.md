# V0042StatsMsgRpcQueue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **int** | Message type as integer | 
**message_type** | **str** | Message type as string | 
**count** | **int** | Number of pending RPCs queued | 

## Example

```python
from openapi_client.models.v0042_stats_msg_rpc_queue import V0042StatsMsgRpcQueue

# TODO update the JSON string below
json = "{}"
# create an instance of V0042StatsMsgRpcQueue from a JSON string
v0042_stats_msg_rpc_queue_instance = V0042StatsMsgRpcQueue.from_json(json)
# print the JSON string representation of the object
print(V0042StatsMsgRpcQueue.to_json())

# convert the object into a dict
v0042_stats_msg_rpc_queue_dict = v0042_stats_msg_rpc_queue_instance.to_dict()
# create an instance of V0042StatsMsgRpcQueue from a dict
v0042_stats_msg_rpc_queue_from_dict = V0042StatsMsgRpcQueue.from_dict(v0042_stats_msg_rpc_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


