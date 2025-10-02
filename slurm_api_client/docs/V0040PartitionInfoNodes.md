# V0040PartitionInfoNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_allocation** | **str** | AllocNodes | [optional] 
**configured** | **str** | Nodes | [optional] 
**total** | **int** | TotalNodes | [optional] 

## Example

```python
from openapi_client.models.v0040_partition_info_nodes import V0040PartitionInfoNodes

# TODO update the JSON string below
json = "{}"
# create an instance of V0040PartitionInfoNodes from a JSON string
v0040_partition_info_nodes_instance = V0040PartitionInfoNodes.from_json(json)
# print the JSON string representation of the object
print(V0040PartitionInfoNodes.to_json())

# convert the object into a dict
v0040_partition_info_nodes_dict = v0040_partition_info_nodes_instance.to_dict()
# create an instance of V0040PartitionInfoNodes from a dict
v0040_partition_info_nodes_from_dict = V0040PartitionInfoNodes.from_dict(v0040_partition_info_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


