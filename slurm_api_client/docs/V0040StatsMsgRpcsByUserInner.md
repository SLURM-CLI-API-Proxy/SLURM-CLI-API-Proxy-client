# V0040StatsMsgRpcsByUserInner

user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | user name | [optional] 
**user_id** | **int** | user id (numeric) | [optional] 
**count** | **int** | Number of RPCs received | [optional] 
**average_time** | **int** | Average time spent processing RPC in seconds | [optional] 
**total_time** | **int** | Total time spent processing RPC in seconds | [optional] 

## Example

```python
from openapi_client.models.v0040_stats_msg_rpcs_by_user_inner import V0040StatsMsgRpcsByUserInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0040StatsMsgRpcsByUserInner from a JSON string
v0040_stats_msg_rpcs_by_user_inner_instance = V0040StatsMsgRpcsByUserInner.from_json(json)
# print the JSON string representation of the object
print(V0040StatsMsgRpcsByUserInner.to_json())

# convert the object into a dict
v0040_stats_msg_rpcs_by_user_inner_dict = v0040_stats_msg_rpcs_by_user_inner_instance.to_dict()
# create an instance of V0040StatsMsgRpcsByUserInner from a dict
v0040_stats_msg_rpcs_by_user_inner_from_dict = V0040StatsMsgRpcsByUserInner.from_dict(v0040_stats_msg_rpcs_by_user_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


