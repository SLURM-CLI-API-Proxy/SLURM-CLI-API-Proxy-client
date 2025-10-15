# V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourlyDuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last** | **int** | Total time spent doing last daily rollup (seconds) | [optional] 
**max** | **int** | Longest hourly rollup time (seconds) | [optional] 
**time** | **int** | Total time spent doing hourly rollups (seconds) | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly_duration import V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourlyDuration

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourlyDuration from a JSON string
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly_duration_instance = V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourlyDuration.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourlyDuration.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly_duration_dict = v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly_duration_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourlyDuration from a dict
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly_duration_from_dict = V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourlyDuration.from_dict(v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


