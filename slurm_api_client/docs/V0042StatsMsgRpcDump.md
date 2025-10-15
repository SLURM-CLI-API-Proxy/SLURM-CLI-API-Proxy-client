# V0042StatsMsgRpcDump


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **int** | Message type as integer | 
**message_type** | **str** | Message type as string | 
**count** | **List[str]** |  | 

## Example

```python
from openapi_client.models.v0042_stats_msg_rpc_dump import V0042StatsMsgRpcDump

# TODO update the JSON string below
json = "{}"
# create an instance of V0042StatsMsgRpcDump from a JSON string
v0042_stats_msg_rpc_dump_instance = V0042StatsMsgRpcDump.from_json(json)
# print the JSON string representation of the object
print(V0042StatsMsgRpcDump.to_json())

# convert the object into a dict
v0042_stats_msg_rpc_dump_dict = v0042_stats_msg_rpc_dump_instance.to_dict()
# create an instance of V0042StatsMsgRpcDump from a dict
v0042_stats_msg_rpc_dump_from_dict = V0042StatsMsgRpcDump.from_dict(v0042_stats_msg_rpc_dump_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


