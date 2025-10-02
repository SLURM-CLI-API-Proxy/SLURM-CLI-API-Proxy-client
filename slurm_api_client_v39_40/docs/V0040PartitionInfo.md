# V0040PartitionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**V0039PartitionInfoNodes**](V0039PartitionInfoNodes.md) |  | [optional] 
**accounts** | [**V0039PartitionInfoAccounts**](V0039PartitionInfoAccounts.md) |  | [optional] 
**groups** | [**V0039PartitionInfoGroups**](V0039PartitionInfoGroups.md) |  | [optional] 
**qos** | [**V0039PartitionInfoQos**](V0039PartitionInfoQos.md) |  | [optional] 
**alternate** | **str** |  | [optional] 
**tres** | [**V0039PartitionInfoTres**](V0039PartitionInfoTres.md) |  | [optional] 
**cluster** | **str** |  | [optional] 
**cpus** | [**V0039PartitionInfoCpus**](V0039PartitionInfoCpus.md) |  | [optional] 
**defaults** | [**V0040PartitionInfoDefaults**](V0040PartitionInfoDefaults.md) |  | [optional] 
**grace_time** | **int** |  | [optional] 
**maximums** | [**V0040PartitionInfoMaximums**](V0040PartitionInfoMaximums.md) |  | [optional] 
**minimums** | [**V0039PartitionInfoMinimums**](V0039PartitionInfoMinimums.md) |  | [optional] 
**name** | **str** |  | [optional] 
**node_sets** | **str** |  | [optional] 
**priority** | [**V0039PartitionInfoPriority**](V0039PartitionInfoPriority.md) |  | [optional] 
**timeouts** | [**V0040PartitionInfoTimeouts**](V0040PartitionInfoTimeouts.md) |  | [optional] 
**partition** | [**V0040PartitionInfoPartition**](V0040PartitionInfoPartition.md) |  | [optional] 
**suspend_time** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_partition_info import V0040PartitionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V0040PartitionInfo from a JSON string
v0040_partition_info_instance = V0040PartitionInfo.from_json(json)
# print the JSON string representation of the object
print(V0040PartitionInfo.to_json())

# convert the object into a dict
v0040_partition_info_dict = v0040_partition_info_instance.to_dict()
# create an instance of V0040PartitionInfo from a dict
v0040_partition_info_from_dict = V0040PartitionInfo.from_dict(v0040_partition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


