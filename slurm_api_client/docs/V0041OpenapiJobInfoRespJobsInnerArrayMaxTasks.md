# V0041OpenapiJobInfoRespJobsInnerArrayMaxTasks

Maximum number of simultaneously running array tasks, 0 if no limit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_array_max_tasks import V0041OpenapiJobInfoRespJobsInnerArrayMaxTasks

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiJobInfoRespJobsInnerArrayMaxTasks from a JSON string
v0041_openapi_job_info_resp_jobs_inner_array_max_tasks_instance = V0041OpenapiJobInfoRespJobsInnerArrayMaxTasks.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiJobInfoRespJobsInnerArrayMaxTasks.to_json())

# convert the object into a dict
v0041_openapi_job_info_resp_jobs_inner_array_max_tasks_dict = v0041_openapi_job_info_resp_jobs_inner_array_max_tasks_instance.to_dict()
# create an instance of V0041OpenapiJobInfoRespJobsInnerArrayMaxTasks from a dict
v0041_openapi_job_info_resp_jobs_inner_array_max_tasks_from_dict = V0041OpenapiJobInfoRespJobsInnerArrayMaxTasks.from_dict(v0041_openapi_job_info_resp_jobs_inner_array_max_tasks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


