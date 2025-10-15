# V0041OpenapiSlurmdbdJobsRespJobsInnerState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **List[str]** | Current state | [optional] 
**reason** | **str** | Reason for previous Pending or Failed state | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_state import V0041OpenapiSlurmdbdJobsRespJobsInnerState

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerState from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_state_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerState.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerState.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_state_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_state_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerState from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_state_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerState.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


