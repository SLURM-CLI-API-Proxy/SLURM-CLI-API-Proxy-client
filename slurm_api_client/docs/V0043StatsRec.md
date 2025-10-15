# V0043StatsRec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_start** | **int** | When data collection started (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**rollups** | [**V0043RollupStats**](V0043RollupStats.md) |  | [optional] 
**rpcs** | [**List[V0043StatsRpc]**](V0043StatsRpc.md) |  | [optional] 
**users** | [**List[V0043StatsUser]**](V0043StatsUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_stats_rec import V0043StatsRec

# TODO update the JSON string below
json = "{}"
# create an instance of V0043StatsRec from a JSON string
v0043_stats_rec_instance = V0043StatsRec.from_json(json)
# print the JSON string representation of the object
print(V0043StatsRec.to_json())

# convert the object into a dict
v0043_stats_rec_dict = v0043_stats_rec_instance.to_dict()
# create an instance of V0043StatsRec from a dict
v0043_stats_rec_from_dict = V0043StatsRec.from_dict(v0043_stats_rec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


