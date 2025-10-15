# V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of nodes in the job step | [optional] 
**range** | **str** | Node(s) allocated to the job step | [optional] 
**list** | **List[str]** | List of nodes used by the step | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_nodes import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_nodes_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_nodes_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_nodes_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_nodes_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


