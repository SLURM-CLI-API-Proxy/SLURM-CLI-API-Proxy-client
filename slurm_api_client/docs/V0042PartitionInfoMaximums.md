# V0042PartitionInfoMaximums


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus_per_node** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**cpus_per_socket** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**memory_per_cpu** | **int** | MaxMemPerCPU or MaxMemPerNode | [optional] 
**partition_memory_per_cpu** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**partition_memory_per_node** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**nodes** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**shares** | **int** | OverSubscribe | [optional] 
**oversubscribe** | [**V0042PartitionInfoMaximumsOversubscribe**](V0042PartitionInfoMaximumsOversubscribe.md) |  | [optional] 
**time** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**over_time_limit** | [**V0042Uint16NoValStruct**](V0042Uint16NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_partition_info_maximums import V0042PartitionInfoMaximums

# TODO update the JSON string below
json = "{}"
# create an instance of V0042PartitionInfoMaximums from a JSON string
v0042_partition_info_maximums_instance = V0042PartitionInfoMaximums.from_json(json)
# print the JSON string representation of the object
print(V0042PartitionInfoMaximums.to_json())

# convert the object into a dict
v0042_partition_info_maximums_dict = v0042_partition_info_maximums_instance.to_dict()
# create an instance of V0042PartitionInfoMaximums from a dict
v0042_partition_info_maximums_from_dict = V0042PartitionInfoMaximums.from_dict(v0042_partition_info_maximums_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


