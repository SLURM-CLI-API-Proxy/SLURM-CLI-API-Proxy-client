# V0042PartitionInfoDefaults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_per_cpu** | **int** | DefMemPerCPU or DefMemPerNode | [optional] 
**partition_memory_per_cpu** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**partition_memory_per_node** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**time** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**job** | **str** | JobDefaults | [optional] 

## Example

```python
from openapi_client.models.v0042_partition_info_defaults import V0042PartitionInfoDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of V0042PartitionInfoDefaults from a JSON string
v0042_partition_info_defaults_instance = V0042PartitionInfoDefaults.from_json(json)
# print the JSON string representation of the object
print(V0042PartitionInfoDefaults.to_json())

# convert the object into a dict
v0042_partition_info_defaults_dict = v0042_partition_info_defaults_instance.to_dict()
# create an instance of V0042PartitionInfoDefaults from a dict
v0042_partition_info_defaults_from_dict = V0042PartitionInfoDefaults.from_dict(v0042_partition_info_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


