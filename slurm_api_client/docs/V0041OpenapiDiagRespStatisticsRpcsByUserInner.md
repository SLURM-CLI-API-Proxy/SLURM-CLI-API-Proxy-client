# V0041OpenapiDiagRespStatisticsRpcsByUserInner

RPCs by user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID (numeric) | 
**user** | **str** | User name | 
**count** | **int** | Number of RPCs received | 
**total_time** | **int** | Total time spent processing RPC in seconds | 
**average_time** | [**V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime**](V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime.md) |  | 

## Example

```python
from openapi_client.models.v0041_openapi_diag_resp_statistics_rpcs_by_user_inner import V0041OpenapiDiagRespStatisticsRpcsByUserInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiDiagRespStatisticsRpcsByUserInner from a JSON string
v0041_openapi_diag_resp_statistics_rpcs_by_user_inner_instance = V0041OpenapiDiagRespStatisticsRpcsByUserInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiDiagRespStatisticsRpcsByUserInner.to_json())

# convert the object into a dict
v0041_openapi_diag_resp_statistics_rpcs_by_user_inner_dict = v0041_openapi_diag_resp_statistics_rpcs_by_user_inner_instance.to_dict()
# create an instance of V0041OpenapiDiagRespStatisticsRpcsByUserInner from a dict
v0041_openapi_diag_resp_statistics_rpcs_by_user_inner_from_dict = V0041OpenapiDiagRespStatisticsRpcsByUserInner.from_dict(v0041_openapi_diag_resp_statistics_rpcs_by_user_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


