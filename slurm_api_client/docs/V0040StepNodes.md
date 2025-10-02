# V0040StepNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of nodes in the job step | [optional] 
**range** | **str** | Node(s) allocated to the job step | [optional] 
**list** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.v0040_step_nodes import V0040StepNodes

# TODO update the JSON string below
json = "{}"
# create an instance of V0040StepNodes from a JSON string
v0040_step_nodes_instance = V0040StepNodes.from_json(json)
# print the JSON string representation of the object
print(V0040StepNodes.to_json())

# convert the object into a dict
v0040_step_nodes_dict = v0040_step_nodes_instance.to_dict()
# create an instance of V0040StepNodes from a dict
v0040_step_nodes_from_dict = V0040StepNodes.from_dict(v0040_step_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


