# V0042StepNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of nodes in the job step | [optional] 
**range** | **str** | Node(s) allocated to the job step | [optional] 
**list** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.v0042_step_nodes import V0042StepNodes

# TODO update the JSON string below
json = "{}"
# create an instance of V0042StepNodes from a JSON string
v0042_step_nodes_instance = V0042StepNodes.from_json(json)
# print the JSON string representation of the object
print(V0042StepNodes.to_json())

# convert the object into a dict
v0042_step_nodes_dict = v0042_step_nodes_instance.to_dict()
# create an instance of V0042StepNodes from a dict
v0042_step_nodes_from_dict = V0042StepNodes.from_dict(v0042_step_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


