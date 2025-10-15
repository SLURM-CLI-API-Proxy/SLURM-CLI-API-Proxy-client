# V0041OpenapiSlurmdbdJobsRespJobsInnerTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Trackable resources allocated to the job | [optional] 
**requested** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Trackable resources requested by job | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_tres import V0041OpenapiSlurmdbdJobsRespJobsInnerTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerTres from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_tres_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerTres.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerTres.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_tres_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_tres_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerTres from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_tres_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerTres.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


