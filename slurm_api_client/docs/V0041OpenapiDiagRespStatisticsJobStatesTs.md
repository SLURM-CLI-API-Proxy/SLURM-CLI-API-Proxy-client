# V0041OpenapiDiagRespStatisticsJobStatesTs

When the job state counts were gathered (UNIX timestamp)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_diag_resp_statistics_job_states_ts import V0041OpenapiDiagRespStatisticsJobStatesTs

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiDiagRespStatisticsJobStatesTs from a JSON string
v0041_openapi_diag_resp_statistics_job_states_ts_instance = V0041OpenapiDiagRespStatisticsJobStatesTs.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiDiagRespStatisticsJobStatesTs.to_json())

# convert the object into a dict
v0041_openapi_diag_resp_statistics_job_states_ts_dict = v0041_openapi_diag_resp_statistics_job_states_ts_instance.to_dict()
# create an instance of V0041OpenapiDiagRespStatisticsJobStatesTs from a dict
v0041_openapi_diag_resp_statistics_job_states_ts_from_dict = V0041OpenapiDiagRespStatisticsJobStatesTs.from_dict(v0041_openapi_diag_resp_statistics_job_states_ts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


