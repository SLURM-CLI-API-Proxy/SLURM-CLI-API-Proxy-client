# V0041OpenapiDiagRespStatisticsScheduleExit

Reasons for which the scheduling cycle exited since last reset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_job_queue** | **int** | Reached end of queue | [optional] 
**default_queue_depth** | **int** | Reached number of jobs allowed to be tested | [optional] 
**max_job_start** | **int** | Reached number of jobs allowed to start | [optional] 
**max_rpc_cnt** | **int** | Reached RPC limit | [optional] 
**max_sched_time** | **int** | Reached maximum allowed scheduler time | [optional] 
**licenses** | **int** | Blocked on licenses | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_diag_resp_statistics_schedule_exit import V0041OpenapiDiagRespStatisticsScheduleExit

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiDiagRespStatisticsScheduleExit from a JSON string
v0041_openapi_diag_resp_statistics_schedule_exit_instance = V0041OpenapiDiagRespStatisticsScheduleExit.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiDiagRespStatisticsScheduleExit.to_json())

# convert the object into a dict
v0041_openapi_diag_resp_statistics_schedule_exit_dict = v0041_openapi_diag_resp_statistics_schedule_exit_instance.to_dict()
# create an instance of V0041OpenapiDiagRespStatisticsScheduleExit from a dict
v0041_openapi_diag_resp_statistics_schedule_exit_from_dict = V0041OpenapiDiagRespStatisticsScheduleExit.from_dict(v0041_openapi_diag_resp_statistics_schedule_exit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


