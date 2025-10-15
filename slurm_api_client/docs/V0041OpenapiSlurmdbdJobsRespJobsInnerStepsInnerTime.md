# V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** | Elapsed time in seconds | [optional] 
**end** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeEnd**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeEnd.md) |  | [optional] 
**start** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeStart**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeStart.md) |  | [optional] 
**suspended** | **int** | Time in suspended state in seconds | [optional] 
**system** | [**V0040StepTimeSystem**](V0040StepTimeSystem.md) |  | [optional] 
**total** | [**V0040StepTimeTotal**](V0040StepTimeTotal.md) |  | [optional] 
**user** | [**V0040StepTimeUser**](V0040StepTimeUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


