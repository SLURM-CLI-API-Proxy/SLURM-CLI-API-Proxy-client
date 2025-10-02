# V0039RollupStatsInner

recorded rollup statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type | [optional] 
**last_run** | **int** | Last time rollup ran (UNIX timestamp) | [optional] 
**max_cycle** | **int** | longest rollup time (seconds) | [optional] 
**total_time** | **int** | total time spent doing rollups (seconds) | [optional] 
**total_cycles** | **int** | number of rollups since last_run | [optional] 
**mean_cycles** | **int** | average time for rollup (seconds) | [optional] 

## Example

```python
from openapi_client.models.v0039_rollup_stats_inner import V0039RollupStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0039RollupStatsInner from a JSON string
v0039_rollup_stats_inner_instance = V0039RollupStatsInner.from_json(json)
# print the JSON string representation of the object
print(V0039RollupStatsInner.to_json())

# convert the object into a dict
v0039_rollup_stats_inner_dict = v0039_rollup_stats_inner_instance.to_dict()
# create an instance of V0039RollupStatsInner from a dict
v0039_rollup_stats_inner_from_dict = V0039RollupStatsInner.from_dict(v0039_rollup_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


