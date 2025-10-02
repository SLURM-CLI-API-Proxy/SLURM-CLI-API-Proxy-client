# V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner

RPCs by type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **int** | Message type as integer | 
**message_type** | **str** | Message type as string | 
**count** | **int** | Number of RPCs received | 
**queued** | **int** | Number of RPCs queued | 
**dropped** | **int** | Number of RPCs dropped | 
**cycle_last** | **int** | Number of RPCs processed within the last RPC queue cycle | 
**cycle_max** | **int** | Maximum number of RPCs processed within a RPC queue cycle since start | 
**total_time** | **int** | Total time spent processing RPC in seconds | 
**average_time** | [**V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime**](V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime.md) |  | 

## Example

```python
from openapi_client.models.v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner import V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner from a JSON string
v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner_instance = V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner.to_json())

# convert the object into a dict
v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner_dict = v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner_instance.to_dict()
# create an instance of V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner from a dict
v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner_from_dict = V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner.from_dict(v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


