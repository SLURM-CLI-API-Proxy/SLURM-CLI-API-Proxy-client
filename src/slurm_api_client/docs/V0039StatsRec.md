# V0039StatsRec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_start** | **int** |  | [optional] 
**rollups** | [**List[V0039RollupStatsInner]**](V0039RollupStatsInner.md) | list of recorded rollup statistics | [optional] 
**rpcs** | [**List[V0039StatsRpc]**](V0039StatsRpc.md) |  | [optional] 
**users** | [**List[V0039StatsUser]**](V0039StatsUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_stats_rec import V0039StatsRec

# TODO update the JSON string below
json = "{}"
# create an instance of V0039StatsRec from a JSON string
v0039_stats_rec_instance = V0039StatsRec.from_json(json)
# print the JSON string representation of the object
print(V0039StatsRec.to_json())

# convert the object into a dict
v0039_stats_rec_dict = v0039_stats_rec_instance.to_dict()
# create an instance of V0039StatsRec from a dict
v0039_stats_rec_from_dict = V0039StatsRec.from_dict(v0039_stats_rec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


