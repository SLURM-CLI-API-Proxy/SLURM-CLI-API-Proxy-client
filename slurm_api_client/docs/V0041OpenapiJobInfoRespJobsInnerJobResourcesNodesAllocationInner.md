# V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner

Job resources for a node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Node index | 
**name** | **str** | Node name | 
**cpus** | [**V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerCpus**](V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerCpus.md) |  | [optional] 
**memory** | [**V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerMemory**](V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerMemory.md) |  | [optional] 
**sockets** | [**List[V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerSocketsInner]**](V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerSocketsInner.md) | Socket allocations in node | 

## Example

```python
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner import V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner from a JSON string
v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_instance = V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner.to_json())

# convert the object into a dict
v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_dict = v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_instance.to_dict()
# create an instance of V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner from a dict
v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_from_dict = V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner.from_dict(v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


