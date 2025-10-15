# V0042JobResNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Node index | 
**name** | **str** | Node name | 
**cpus** | [**V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerCpus**](V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerCpus.md) |  | [optional] 
**memory** | [**V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerMemory**](V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerMemory.md) |  | [optional] 
**sockets** | [**List[V0042JobResSocket]**](V0042JobResSocket.md) |  | 

## Example

```python
from openapi_client.models.v0042_job_res_node import V0042JobResNode

# TODO update the JSON string below
json = "{}"
# create an instance of V0042JobResNode from a JSON string
v0042_job_res_node_instance = V0042JobResNode.from_json(json)
# print the JSON string representation of the object
print(V0042JobResNode.to_json())

# convert the object into a dict
v0042_job_res_node_dict = v0042_job_res_node_instance.to_dict()
# create an instance of V0042JobResNode from a dict
v0042_job_res_node_from_dict = V0042JobResNode.from_dict(v0042_job_res_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


