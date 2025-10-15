# V0040KillJobsRespJobError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string** | **str** | String error encountered signaling job | [optional] 
**code** | **int** | Numeric error encountered signaling job | [optional] 
**message** | **str** | Error message why signaling job failed | [optional] 

## Example

```python
from openapi_client.models.v0040_kill_jobs_resp_job_error import V0040KillJobsRespJobError

# TODO update the JSON string below
json = "{}"
# create an instance of V0040KillJobsRespJobError from a JSON string
v0040_kill_jobs_resp_job_error_instance = V0040KillJobsRespJobError.from_json(json)
# print the JSON string representation of the object
print(V0040KillJobsRespJobError.to_json())

# convert the object into a dict
v0040_kill_jobs_resp_job_error_dict = v0040_kill_jobs_resp_job_error_instance.to_dict()
# create an instance of V0040KillJobsRespJobError from a dict
v0040_kill_jobs_resp_job_error_from_dict = V0040KillJobsRespJobError.from_dict(v0040_kill_jobs_resp_job_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


