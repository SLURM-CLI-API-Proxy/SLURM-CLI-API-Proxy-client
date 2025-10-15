# V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresConsumed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Maximum TRES usage consumed among all tasks | [optional] 
**min** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Minimum TRES usage consumed among all tasks | [optional] 
**average** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Average TRES usage consumed among all tasks | [optional] 
**total** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Total TRES usage consumed among all tasks | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_consumed import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresConsumed

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresConsumed from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_consumed_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresConsumed.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresConsumed.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_consumed_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_consumed_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresConsumed from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_consumed_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresConsumed.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_consumed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


