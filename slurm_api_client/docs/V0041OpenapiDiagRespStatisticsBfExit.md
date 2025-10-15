# V0041OpenapiDiagRespStatisticsBfExit

Reasons for which the backfill scheduling cycle exited since last reset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_job_queue** | **int** | Reached end of queue | [optional] 
**bf_max_job_start** | **int** | Reached number of jobs allowed to start | [optional] 
**bf_max_job_test** | **int** | Reached number of jobs allowed to be tested | [optional] 
**bf_max_time** | **int** | Reached maximum allowed scheduler time | [optional] 
**bf_node_space_size** | **int** | Reached table size limit | [optional] 
**state_changed** | **int** | System state changed | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_diag_resp_statistics_bf_exit import V0041OpenapiDiagRespStatisticsBfExit

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiDiagRespStatisticsBfExit from a JSON string
v0041_openapi_diag_resp_statistics_bf_exit_instance = V0041OpenapiDiagRespStatisticsBfExit.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiDiagRespStatisticsBfExit.to_json())

# convert the object into a dict
v0041_openapi_diag_resp_statistics_bf_exit_dict = v0041_openapi_diag_resp_statistics_bf_exit_instance.to_dict()
# create an instance of V0041OpenapiDiagRespStatisticsBfExit from a dict
v0041_openapi_diag_resp_statistics_bf_exit_from_dict = V0041OpenapiDiagRespStatisticsBfExit.from_dict(v0041_openapi_diag_resp_statistics_bf_exit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


