# V0041OpenapiPartitionRespPartitionsInnerMaximums


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus_per_node** | [**V0041OpenapiPartitionRespPartitionsInnerMaximumsCpusPerNode**](V0041OpenapiPartitionRespPartitionsInnerMaximumsCpusPerNode.md) |  | [optional] 
**cpus_per_socket** | [**V0041OpenapiPartitionRespPartitionsInnerMaximumsCpusPerSocket**](V0041OpenapiPartitionRespPartitionsInnerMaximumsCpusPerSocket.md) |  | [optional] 
**memory_per_cpu** | **int** | MaxMemPerCPU or MaxMemPerNode | [optional] 
**partition_memory_per_cpu** | [**V0041OpenapiPartitionRespPartitionsInnerMaximumsPartitionMemoryPerCpu**](V0041OpenapiPartitionRespPartitionsInnerMaximumsPartitionMemoryPerCpu.md) |  | [optional] 
**partition_memory_per_node** | [**V0041OpenapiPartitionRespPartitionsInnerMaximumsPartitionMemoryPerNode**](V0041OpenapiPartitionRespPartitionsInnerMaximumsPartitionMemoryPerNode.md) |  | [optional] 
**nodes** | [**V0041OpenapiPartitionRespPartitionsInnerMaximumsNodes**](V0041OpenapiPartitionRespPartitionsInnerMaximumsNodes.md) |  | [optional] 
**shares** | **int** | OverSubscribe | [optional] 
**oversubscribe** | [**V0041OpenapiPartitionRespPartitionsInnerMaximumsOversubscribe**](V0041OpenapiPartitionRespPartitionsInnerMaximumsOversubscribe.md) |  | [optional] 
**time** | [**V0041OpenapiPartitionRespPartitionsInnerMaximumsTime**](V0041OpenapiPartitionRespPartitionsInnerMaximumsTime.md) |  | [optional] 
**over_time_limit** | [**V0041OpenapiPartitionRespPartitionsInnerMaximumsOverTimeLimit**](V0041OpenapiPartitionRespPartitionsInnerMaximumsOverTimeLimit.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_maximums import V0041OpenapiPartitionRespPartitionsInnerMaximums

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiPartitionRespPartitionsInnerMaximums from a JSON string
v0041_openapi_partition_resp_partitions_inner_maximums_instance = V0041OpenapiPartitionRespPartitionsInnerMaximums.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiPartitionRespPartitionsInnerMaximums.to_json())

# convert the object into a dict
v0041_openapi_partition_resp_partitions_inner_maximums_dict = v0041_openapi_partition_resp_partitions_inner_maximums_instance.to_dict()
# create an instance of V0041OpenapiPartitionRespPartitionsInnerMaximums from a dict
v0041_openapi_partition_resp_partitions_inner_maximums_from_dict = V0041OpenapiPartitionRespPartitionsInnerMaximums.from_dict(v0041_openapi_partition_resp_partitions_inner_maximums_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


