# V0043JobResNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of allocated nodes | [optional] 
**select_type** | **List[str]** | Node scheduling selection method | [optional] 
**list** | **str** | Node(s) allocated to the job | [optional] 
**whole** | **bool** | Whether whole nodes were allocated | [optional] 
**allocation** | [**List[V0043JobResNode]**](V0043JobResNode.md) | Job resources for a node | [optional] 

## Example

```python
from openapi_client.models.v0043_job_res_nodes import V0043JobResNodes

# TODO update the JSON string below
json = "{}"
# create an instance of V0043JobResNodes from a JSON string
v0043_job_res_nodes_instance = V0043JobResNodes.from_json(json)
# print the JSON string representation of the object
print(V0043JobResNodes.to_json())

# convert the object into a dict
v0043_job_res_nodes_dict = v0043_job_res_nodes_instance.to_dict()
# create an instance of V0043JobResNodes from a dict
v0043_job_res_nodes_from_dict = V0043JobResNodes.from_dict(v0043_job_res_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


