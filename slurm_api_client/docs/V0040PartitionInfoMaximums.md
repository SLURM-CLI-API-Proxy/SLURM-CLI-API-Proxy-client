# V0040PartitionInfoMaximums


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus_per_node** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**cpus_per_socket** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**memory_per_cpu** | **int** | MaxMemPerCPU or MaxMemPerNode | [optional] 
**partition_memory_per_cpu** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**partition_memory_per_node** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**nodes** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**shares** | **int** | OverSubscribe | [optional] 
**oversubscribe** | [**V0040PartitionInfoMaximumsOversubscribe**](V0040PartitionInfoMaximumsOversubscribe.md) |  | [optional] 
**time** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**over_time_limit** | [**V0040Uint16NoVal**](V0040Uint16NoVal.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_partition_info_maximums import V0040PartitionInfoMaximums

# TODO update the JSON string below
json = "{}"
# create an instance of V0040PartitionInfoMaximums from a JSON string
v0040_partition_info_maximums_instance = V0040PartitionInfoMaximums.from_json(json)
# print the JSON string representation of the object
print(V0040PartitionInfoMaximums.to_json())

# convert the object into a dict
v0040_partition_info_maximums_dict = v0040_partition_info_maximums_instance.to_dict()
# create an instance of V0040PartitionInfoMaximums from a dict
v0040_partition_info_maximums_from_dict = V0040PartitionInfoMaximums.from_dict(v0040_partition_info_maximums_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


