# V0041OpenapiSlurmdbdJobsRespJobsInnerRequired


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus** | **int** | Minimum number of CPUs required | [optional] 
**memory_per_cpu** | [**V0041JobDescMsgMemoryPerCpu**](V0041JobDescMsgMemoryPerCpu.md) |  | [optional] 
**memory_per_node** | [**V0041OpenapiJobInfoRespJobsInnerMemoryPerNode**](V0041OpenapiJobInfoRespJobsInnerMemoryPerNode.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_required import V0041OpenapiSlurmdbdJobsRespJobsInnerRequired

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerRequired from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_required_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerRequired.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerRequired.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_required_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_required_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerRequired from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_required_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerRequired.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


