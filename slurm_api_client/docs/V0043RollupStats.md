# V0043RollupStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hourly** | [**V0043RollupStatsHourly**](V0043RollupStatsHourly.md) |  | [optional] 
**daily** | [**V0043RollupStatsDaily**](V0043RollupStatsDaily.md) |  | [optional] 
**monthly** | [**V0043RollupStatsMonthly**](V0043RollupStatsMonthly.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_rollup_stats import V0043RollupStats

# TODO update the JSON string below
json = "{}"
# create an instance of V0043RollupStats from a JSON string
v0043_rollup_stats_instance = V0043RollupStats.from_json(json)
# print the JSON string representation of the object
print(V0043RollupStats.to_json())

# convert the object into a dict
v0043_rollup_stats_dict = v0043_rollup_stats_instance.to_dict()
# create an instance of V0043RollupStats from a dict
v0043_rollup_stats_from_dict = V0043RollupStats.from_dict(v0043_rollup_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


