# V0043RollupStatsMonthly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of monthly rollups since last_run | [optional] 
**last_run** | **int** | Last time monthly rollup ran (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**duration** | [**V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthlyDuration**](V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthlyDuration.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_rollup_stats_monthly import V0043RollupStatsMonthly

# TODO update the JSON string below
json = "{}"
# create an instance of V0043RollupStatsMonthly from a JSON string
v0043_rollup_stats_monthly_instance = V0043RollupStatsMonthly.from_json(json)
# print the JSON string representation of the object
print(V0043RollupStatsMonthly.to_json())

# convert the object into a dict
v0043_rollup_stats_monthly_dict = v0043_rollup_stats_monthly_instance.to_dict()
# create an instance of V0043RollupStatsMonthly from a dict
v0043_rollup_stats_monthly_from_dict = V0043RollupStatsMonthly.from_dict(v0043_rollup_stats_monthly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


