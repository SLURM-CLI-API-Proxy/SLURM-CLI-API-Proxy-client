# V0040PartitionInfoDefaults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_per_cpu** | **int** | DefMemPerCPU or DefMemPerNode | [optional] 
**partition_memory_per_cpu** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**partition_memory_per_node** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**time** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**job** | **str** | JobDefaults | [optional] 

## Example

```python
from openapi_client.models.v0040_partition_info_defaults import V0040PartitionInfoDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of V0040PartitionInfoDefaults from a JSON string
v0040_partition_info_defaults_instance = V0040PartitionInfoDefaults.from_json(json)
# print the JSON string representation of the object
print(V0040PartitionInfoDefaults.to_json())

# convert the object into a dict
v0040_partition_info_defaults_dict = v0040_partition_info_defaults_instance.to_dict()
# create an instance of V0040PartitionInfoDefaults from a dict
v0040_partition_info_defaults_from_dict = V0040PartitionInfoDefaults.from_dict(v0040_partition_info_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


