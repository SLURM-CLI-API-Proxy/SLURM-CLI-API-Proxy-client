# V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | User ID | [optional] 
**count** | **int** | Number of RPCs processed | [optional] 
**time** | [**V0040StatsRpcTime**](V0040StatsRpcTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_stats_resp_statistics_users_inner import V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner from a JSON string
v0041_openapi_slurmdbd_stats_resp_statistics_users_inner_instance = V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_stats_resp_statistics_users_inner_dict = v0041_openapi_slurmdbd_stats_resp_statistics_users_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner from a dict
v0041_openapi_slurmdbd_stats_resp_statistics_users_inner_from_dict = V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner.from_dict(v0041_openapi_slurmdbd_stats_resp_statistics_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


