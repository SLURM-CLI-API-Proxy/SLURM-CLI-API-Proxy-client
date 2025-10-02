# V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of allocated nodes | [optional] 
**select_type** | **List[str]** | Node scheduling selection method | [optional] 
**list** | **str** | Node(s) allocated to the job | [optional] 
**whole** | **bool** | Whether whole nodes were allocated | [optional] 
**allocation** | [**List[V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner]**](V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner.md) | Allocated node resources | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes import V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes from a JSON string
v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_instance = V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes.to_json())

# convert the object into a dict
v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_dict = v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_instance.to_dict()
# create an instance of V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes from a dict
v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_from_dict = V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes.from_dict(v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


