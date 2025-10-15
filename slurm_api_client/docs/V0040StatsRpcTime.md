# V0040StatsRpcTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average** | **int** | Average RPC processing time in microseconds | [optional] 
**total** | **int** | Total RPC processing time in microseconds | [optional] 

## Example

```python
from openapi_client.models.v0040_stats_rpc_time import V0040StatsRpcTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0040StatsRpcTime from a JSON string
v0040_stats_rpc_time_instance = V0040StatsRpcTime.from_json(json)
# print the JSON string representation of the object
print(V0040StatsRpcTime.to_json())

# convert the object into a dict
v0040_stats_rpc_time_dict = v0040_stats_rpc_time_instance.to_dict()
# create an instance of V0040StatsRpcTime from a dict
v0040_stats_rpc_time_from_dict = V0040StatsRpcTime.from_dict(v0040_stats_rpc_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


