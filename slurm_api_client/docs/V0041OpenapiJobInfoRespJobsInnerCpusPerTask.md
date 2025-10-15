# V0041OpenapiJobInfoRespJobsInnerCpusPerTask

Number of CPUs required by each task

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_cpus_per_task import V0041OpenapiJobInfoRespJobsInnerCpusPerTask

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiJobInfoRespJobsInnerCpusPerTask from a JSON string
v0041_openapi_job_info_resp_jobs_inner_cpus_per_task_instance = V0041OpenapiJobInfoRespJobsInnerCpusPerTask.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiJobInfoRespJobsInnerCpusPerTask.to_json())

# convert the object into a dict
v0041_openapi_job_info_resp_jobs_inner_cpus_per_task_dict = v0041_openapi_job_info_resp_jobs_inner_cpus_per_task_instance.to_dict()
# create an instance of V0041OpenapiJobInfoRespJobsInnerCpusPerTask from a dict
v0041_openapi_job_info_resp_jobs_inner_cpus_per_task_from_dict = V0041OpenapiJobInfoRespJobsInnerCpusPerTask.from_dict(v0041_openapi_job_info_resp_jobs_inner_cpus_per_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


