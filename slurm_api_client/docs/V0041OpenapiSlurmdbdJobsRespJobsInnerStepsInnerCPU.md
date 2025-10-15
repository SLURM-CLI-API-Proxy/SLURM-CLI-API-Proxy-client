# V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_frequency** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequency**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequency.md) |  | [optional] 
**governor** | **str** | Requested CPU frequency governor in kHz | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


