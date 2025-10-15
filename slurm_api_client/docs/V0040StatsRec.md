# V0040StatsRec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_start** | **int** | When data collection started (UNIX timestamp) | [optional] 
**rollups** | [**List[V0040RollupStatsInner]**](V0040RollupStatsInner.md) | list of recorded rollup statistics | [optional] 
**rpcs** | [**List[V0040StatsRpc]**](V0040StatsRpc.md) |  | [optional] 
**users** | [**List[V0040StatsUser]**](V0040StatsUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_stats_rec import V0040StatsRec

# TODO update the JSON string below
json = "{}"
# create an instance of V0040StatsRec from a JSON string
v0040_stats_rec_instance = V0040StatsRec.from_json(json)
# print the JSON string representation of the object
print(V0040StatsRec.to_json())

# convert the object into a dict
v0040_stats_rec_dict = v0040_stats_rec_instance.to_dict()
# create an instance of V0040StatsRec from a dict
v0040_stats_rec_from_dict = V0040StatsRec.from_dict(v0040_stats_rec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


