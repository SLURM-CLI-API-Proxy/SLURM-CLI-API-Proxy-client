# V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime.md) |  | [optional] 
**exit_code** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerExitCode**](V0041OpenapiSlurmdbdJobsRespJobsInnerExitCode.md) |  | [optional] 
**nodes** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes.md) |  | [optional] 
**tasks** | [**V0040StepTasks**](V0040StepTasks.md) |  | [optional] 
**pid** | **str** | Process ID | [optional] 
**cpu** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU.md) |  | [optional] 
**kill_request_user** | **str** | User ID that requested termination of the step | [optional] 
**state** | **List[str]** | Current state | [optional] 
**statistics** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics.md) |  | [optional] 
**step** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStep.md) |  | [optional] 
**task** | [**V0040StepTask**](V0040StepTask.md) |  | [optional] 
**tres** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTres**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInner from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInner from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInner.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


