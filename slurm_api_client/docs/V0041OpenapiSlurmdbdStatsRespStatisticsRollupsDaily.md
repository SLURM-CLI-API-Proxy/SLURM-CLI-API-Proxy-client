# V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of daily rollups since last_run | [optional] 
**last_run** | **int** | Last time daily rollup ran (UNIX timestamp) | [optional] 
**duration** | [**V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDailyDuration**](V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDailyDuration.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_stats_resp_statistics_rollups_daily import V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily from a JSON string
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_daily_instance = V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_daily_dict = v0041_openapi_slurmdbd_stats_resp_statistics_rollups_daily_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily from a dict
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_daily_from_dict = V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily.from_dict(v0041_openapi_slurmdbd_stats_resp_statistics_rollups_daily_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


