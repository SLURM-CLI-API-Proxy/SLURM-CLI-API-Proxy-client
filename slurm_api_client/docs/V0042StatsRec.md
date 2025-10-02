# V0042StatsRec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_start** | **int** | When data collection started (UNIX timestamp) | [optional] 
**rollups** | [**V0042RollupStats**](V0042RollupStats.md) |  | [optional] 
**rpcs** | [**List[V0042StatsRpc]**](V0042StatsRpc.md) |  | [optional] 
**users** | [**List[V0042StatsUser]**](V0042StatsUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_stats_rec import V0042StatsRec

# TODO update the JSON string below
json = "{}"
# create an instance of V0042StatsRec from a JSON string
v0042_stats_rec_instance = V0042StatsRec.from_json(json)
# print the JSON string representation of the object
print(V0042StatsRec.to_json())

# convert the object into a dict
v0042_stats_rec_dict = v0042_stats_rec_instance.to_dict()
# create an instance of V0042StatsRec from a dict
v0042_stats_rec_from_dict = V0042StatsRec.from_dict(v0042_stats_rec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


