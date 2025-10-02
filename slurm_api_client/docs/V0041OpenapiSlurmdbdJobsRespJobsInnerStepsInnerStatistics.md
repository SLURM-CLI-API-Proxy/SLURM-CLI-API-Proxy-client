# V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**V0040StepStatisticsCPU**](V0040StepStatisticsCPU.md) |  | [optional] 
**energy** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsEnergy**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsEnergy.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


