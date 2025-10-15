# V0043PartitionInfoMaximums


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus_per_node** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**cpus_per_socket** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**memory_per_cpu** | **int** | Raw value for MaxMemPerCPU or MaxMemPerNode | [optional] 
**partition_memory_per_cpu** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**partition_memory_per_node** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**nodes** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**shares** | **int** | OverSubscribe - Controls the ability of the partition to execute more than one job at a time on each resource | [optional] 
**oversubscribe** | [**V0041OpenapiPartitionRespPartitionsInnerMaximumsOversubscribe**](V0041OpenapiPartitionRespPartitionsInnerMaximumsOversubscribe.md) |  | [optional] 
**time** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**over_time_limit** | [**V0043Uint16NoValStruct**](V0043Uint16NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_partition_info_maximums import V0043PartitionInfoMaximums

# TODO update the JSON string below
json = "{}"
# create an instance of V0043PartitionInfoMaximums from a JSON string
v0043_partition_info_maximums_instance = V0043PartitionInfoMaximums.from_json(json)
# print the JSON string representation of the object
print(V0043PartitionInfoMaximums.to_json())

# convert the object into a dict
v0043_partition_info_maximums_dict = v0043_partition_info_maximums_instance.to_dict()
# create an instance of V0043PartitionInfoMaximums from a dict
v0043_partition_info_maximums_from_dict = V0043PartitionInfoMaximums.from_dict(v0043_partition_info_maximums_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


