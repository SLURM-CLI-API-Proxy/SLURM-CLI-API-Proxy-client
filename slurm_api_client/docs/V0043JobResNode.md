# V0043JobResNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Node index | 
**name** | **str** | Node name | 
**cpus** | [**V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerCpus**](V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerCpus.md) |  | [optional] 
**memory** | [**V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerMemory**](V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerMemory.md) |  | [optional] 
**sockets** | [**List[V0043JobResSocket]**](V0043JobResSocket.md) |  | 

## Example

```python
from openapi_client.models.v0043_job_res_node import V0043JobResNode

# TODO update the JSON string below
json = "{}"
# create an instance of V0043JobResNode from a JSON string
v0043_job_res_node_instance = V0043JobResNode.from_json(json)
# print the JSON string representation of the object
print(V0043JobResNode.to_json())

# convert the object into a dict
v0043_job_res_node_dict = v0043_job_res_node_instance.to_dict()
# create an instance of V0043JobResNode from a dict
v0043_job_res_node_from_dict = V0043JobResNode.from_dict(v0043_job_res_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


