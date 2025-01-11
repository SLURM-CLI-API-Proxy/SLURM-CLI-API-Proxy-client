# V0038DiagRpcm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | **str** | message type | [optional] 
**type_id** | **int** | message type id | [optional] 
**count** | **int** | rpc count | [optional] 
**average_time** | **int** | average time | [optional] 
**total_time** | **int** | total time | [optional] 

## Example

```python
from openapi_client.models.v0038_diag_rpcm import V0038DiagRpcm

# TODO update the JSON string below
json = "{}"
# create an instance of V0038DiagRpcm from a JSON string
v0038_diag_rpcm_instance = V0038DiagRpcm.from_json(json)
# print the JSON string representation of the object
print(V0038DiagRpcm.to_json())

# convert the object into a dict
v0038_diag_rpcm_dict = v0038_diag_rpcm_instance.to_dict()
# create an instance of V0038DiagRpcm from a dict
v0038_diag_rpcm_from_dict = V0038DiagRpcm.from_dict(v0038_diag_rpcm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


