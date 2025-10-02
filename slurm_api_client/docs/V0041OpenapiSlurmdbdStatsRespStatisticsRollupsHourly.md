# V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of hourly rollups since last_run | [optional] 
**last_run** | **int** | Last time hourly rollup ran (UNIX timestamp) | [optional] 
**duration** | [**V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourlyDuration**](V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourlyDuration.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly import V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly from a JSON string
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly_instance = V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly_dict = v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly from a dict
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly_from_dict = V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly.from_dict(v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


