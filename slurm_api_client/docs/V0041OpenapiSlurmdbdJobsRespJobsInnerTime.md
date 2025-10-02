# V0041OpenapiSlurmdbdJobsRespJobsInnerTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** | Elapsed time in seconds | [optional] 
**eligible** | **int** | Time when the job became eligible to run (UNIX timestamp) | [optional] 
**end** | **int** | End time (UNIX timestamp) | [optional] 
**planned** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerTimePlanned**](V0041OpenapiSlurmdbdJobsRespJobsInnerTimePlanned.md) |  | [optional] 
**start** | **int** | Time execution began (UNIX timestamp) | [optional] 
**submission** | **int** | Time when the job was submitted (UNIX timestamp) | [optional] 
**suspended** | **int** | Total time in suspended state in seconds | [optional] 
**system** | [**V0040JobTimeSystem**](V0040JobTimeSystem.md) |  | [optional] 
**limit** | [**V0041JobDescMsgTimeLimit**](V0041JobDescMsgTimeLimit.md) |  | [optional] 
**total** | [**V0040JobTimeTotal**](V0040JobTimeTotal.md) |  | [optional] 
**user** | [**V0040JobTimeUser**](V0040JobTimeUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time import V0041OpenapiSlurmdbdJobsRespJobsInnerTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerTime from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerTime.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerTime.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerTime from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerTime.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


