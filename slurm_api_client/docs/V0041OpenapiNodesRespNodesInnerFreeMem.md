# V0041OpenapiNodesRespNodesInnerFreeMem

Total memory in MB currently free as reported by the OS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_nodes_resp_nodes_inner_free_mem import V0041OpenapiNodesRespNodesInnerFreeMem

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiNodesRespNodesInnerFreeMem from a JSON string
v0041_openapi_nodes_resp_nodes_inner_free_mem_instance = V0041OpenapiNodesRespNodesInnerFreeMem.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiNodesRespNodesInnerFreeMem.to_json())

# convert the object into a dict
v0041_openapi_nodes_resp_nodes_inner_free_mem_dict = v0041_openapi_nodes_resp_nodes_inner_free_mem_instance.to_dict()
# create an instance of V0041OpenapiNodesRespNodesInnerFreeMem from a dict
v0041_openapi_nodes_resp_nodes_inner_free_mem_from_dict = V0041OpenapiNodesRespNodesInnerFreeMem.from_dict(v0041_openapi_nodes_resp_nodes_inner_free_mem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


