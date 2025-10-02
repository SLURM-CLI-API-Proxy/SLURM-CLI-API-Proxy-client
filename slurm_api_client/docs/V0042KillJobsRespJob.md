# V0042KillJobsRespJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**V0040KillJobsRespJobError**](V0040KillJobsRespJobError.md) |  | [optional] 
**step_id** | **str** | Job or Step ID that signaling failed | 
**job_id** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | 
**federation** | [**V0040KillJobsRespJobFederation**](V0040KillJobsRespJobFederation.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_kill_jobs_resp_job import V0042KillJobsRespJob

# TODO update the JSON string below
json = "{}"
# create an instance of V0042KillJobsRespJob from a JSON string
v0042_kill_jobs_resp_job_instance = V0042KillJobsRespJob.from_json(json)
# print the JSON string representation of the object
print(V0042KillJobsRespJob.to_json())

# convert the object into a dict
v0042_kill_jobs_resp_job_dict = v0042_kill_jobs_resp_job_instance.to_dict()
# create an instance of V0042KillJobsRespJob from a dict
v0042_kill_jobs_resp_job_from_dict = V0042KillJobsRespJob.from_dict(v0042_kill_jobs_resp_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


