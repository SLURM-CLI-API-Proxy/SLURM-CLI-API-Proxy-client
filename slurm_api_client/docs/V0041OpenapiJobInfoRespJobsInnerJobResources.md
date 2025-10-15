# V0041OpenapiJobInfoRespJobsInnerJobResources

Resources used by the job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select_type** | **List[str]** | Scheduler consumable resource selection type | 
**nodes** | [**V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes**](V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes.md) |  | [optional] 
**cpus** | **int** | Number of allocated CPUs | 
**threads_per_core** | [**V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore**](V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore.md) |  | 

## Example

```python
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_job_resources import V0041OpenapiJobInfoRespJobsInnerJobResources

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiJobInfoRespJobsInnerJobResources from a JSON string
v0041_openapi_job_info_resp_jobs_inner_job_resources_instance = V0041OpenapiJobInfoRespJobsInnerJobResources.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiJobInfoRespJobsInnerJobResources.to_json())

# convert the object into a dict
v0041_openapi_job_info_resp_jobs_inner_job_resources_dict = v0041_openapi_job_info_resp_jobs_inner_job_resources_instance.to_dict()
# create an instance of V0041OpenapiJobInfoRespJobsInnerJobResources from a dict
v0041_openapi_job_info_resp_jobs_inner_job_resources_from_dict = V0041OpenapiJobInfoRespJobsInnerJobResources.from_dict(v0041_openapi_job_info_resp_jobs_inner_job_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


