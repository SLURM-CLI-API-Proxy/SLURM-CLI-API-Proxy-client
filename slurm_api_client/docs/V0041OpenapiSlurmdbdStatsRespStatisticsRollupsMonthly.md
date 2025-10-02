# V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of monthly rollups since last_run | [optional] 
**last_run** | **int** | Last time monthly rollup ran (UNIX timestamp) | [optional] 
**duration** | [**V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthlyDuration**](V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthlyDuration.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_stats_resp_statistics_rollups_monthly import V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly from a JSON string
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_monthly_instance = V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_monthly_dict = v0041_openapi_slurmdbd_stats_resp_statistics_rollups_monthly_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly from a dict
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_monthly_from_dict = V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly.from_dict(v0041_openapi_slurmdbd_stats_resp_statistics_rollups_monthly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


