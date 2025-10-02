# V0040StatsMsgRpcsByTypeInner

RPC

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | **str** | Message type as string | [optional] 
**type_id** | **int** | Message type as integer | [optional] 
**count** | **int** | Number of RPCs received | [optional] 
**average_time** | **int** | Average time spent processing RPC in seconds | [optional] 
**total_time** | **int** | Total time spent processing RPC in seconds | [optional] 

## Example

```python
from openapi_client.models.v0040_stats_msg_rpcs_by_type_inner import V0040StatsMsgRpcsByTypeInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0040StatsMsgRpcsByTypeInner from a JSON string
v0040_stats_msg_rpcs_by_type_inner_instance = V0040StatsMsgRpcsByTypeInner.from_json(json)
# print the JSON string representation of the object
print(V0040StatsMsgRpcsByTypeInner.to_json())

# convert the object into a dict
v0040_stats_msg_rpcs_by_type_inner_dict = v0040_stats_msg_rpcs_by_type_inner_instance.to_dict()
# create an instance of V0040StatsMsgRpcsByTypeInner from a dict
v0040_stats_msg_rpcs_by_type_inner_from_dict = V0040StatsMsgRpcsByTypeInner.from_dict(v0040_stats_msg_rpcs_by_type_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


