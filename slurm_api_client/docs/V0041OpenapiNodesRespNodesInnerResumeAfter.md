# V0041OpenapiNodesRespNodesInnerResumeAfter

Number of seconds after the node's state is updated to \"DOWN\" or \"DRAIN\" before scheduling a node state resume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_nodes_resp_nodes_inner_resume_after import V0041OpenapiNodesRespNodesInnerResumeAfter

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiNodesRespNodesInnerResumeAfter from a JSON string
v0041_openapi_nodes_resp_nodes_inner_resume_after_instance = V0041OpenapiNodesRespNodesInnerResumeAfter.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiNodesRespNodesInnerResumeAfter.to_json())

# convert the object into a dict
v0041_openapi_nodes_resp_nodes_inner_resume_after_dict = v0041_openapi_nodes_resp_nodes_inner_resume_after_instance.to_dict()
# create an instance of V0041OpenapiNodesRespNodesInnerResumeAfter from a dict
v0041_openapi_nodes_resp_nodes_inner_resume_after_from_dict = V0041OpenapiNodesRespNodesInnerResumeAfter.from_dict(v0041_openapi_nodes_resp_nodes_inner_resume_after_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


