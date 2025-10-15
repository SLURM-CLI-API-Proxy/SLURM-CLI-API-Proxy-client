# V0043StatsMsgRpcDump


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **int** | Message type as integer | 
**message_type** | **str** | Message type as string (Slurm RPC message type) | 
**count** | **List[str]** |  | 

## Example

```python
from openapi_client.models.v0043_stats_msg_rpc_dump import V0043StatsMsgRpcDump

# TODO update the JSON string below
json = "{}"
# create an instance of V0043StatsMsgRpcDump from a JSON string
v0043_stats_msg_rpc_dump_instance = V0043StatsMsgRpcDump.from_json(json)
# print the JSON string representation of the object
print(V0043StatsMsgRpcDump.to_json())

# convert the object into a dict
v0043_stats_msg_rpc_dump_dict = v0043_stats_msg_rpc_dump_instance.to_dict()
# create an instance of V0043StatsMsgRpcDump from a dict
v0043_stats_msg_rpc_dump_from_dict = V0043StatsMsgRpcDump.from_dict(v0043_stats_msg_rpc_dump_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


