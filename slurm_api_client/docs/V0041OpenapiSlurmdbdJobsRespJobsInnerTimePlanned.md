# V0041OpenapiSlurmdbdJobsRespJobsInnerTimePlanned

Time required to start job after becoming eligible to run in seconds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_planned import V0041OpenapiSlurmdbdJobsRespJobsInnerTimePlanned

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerTimePlanned from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_planned_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerTimePlanned.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerTimePlanned.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_planned_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_planned_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerTimePlanned from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_planned_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerTimePlanned.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_planned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


