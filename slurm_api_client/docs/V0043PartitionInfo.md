# V0043PartitionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**V0043PartitionInfoNodes**](V0043PartitionInfoNodes.md) |  | [optional] 
**accounts** | [**V0043PartitionInfoAccounts**](V0043PartitionInfoAccounts.md) |  | [optional] 
**groups** | [**V0043PartitionInfoGroups**](V0043PartitionInfoGroups.md) |  | [optional] 
**qos** | [**V0043PartitionInfoQos**](V0043PartitionInfoQos.md) |  | [optional] 
**alternate** | **str** | Alternate - Partition name of alternate partition to be used if the state of this partition is DRAIN or INACTIVE | [optional] 
**tres** | [**V0043PartitionInfoTres**](V0043PartitionInfoTres.md) |  | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**select_type** | **List[str]** | Scheduler consumable resource selection type | [optional] 
**cpus** | [**V0043PartitionInfoCpus**](V0043PartitionInfoCpus.md) |  | [optional] 
**defaults** | [**V0043PartitionInfoDefaults**](V0043PartitionInfoDefaults.md) |  | [optional] 
**grace_time** | **int** | GraceTime - Grace time in seconds to be extended to a job which has been selected for preemption | [optional] 
**maximums** | [**V0043PartitionInfoMaximums**](V0043PartitionInfoMaximums.md) |  | [optional] 
**minimums** | [**V0043PartitionInfoMinimums**](V0043PartitionInfoMinimums.md) |  | [optional] 
**name** | **str** | PartitionName - Name by which the partition may be referenced | [optional] 
**node_sets** | **str** | NodeSets - Comma-separated list of nodesets which are associated with this partition | [optional] 
**priority** | [**V0043PartitionInfoPriority**](V0043PartitionInfoPriority.md) |  | [optional] 
**timeouts** | [**V0043PartitionInfoTimeouts**](V0043PartitionInfoTimeouts.md) |  | [optional] 
**topology** | **str** | Topology - Name of the topology, defined in topology.yaml, used by jobs in this partition | [optional] 
**partition** | [**V0041OpenapiPartitionRespPartitionsInnerPartition**](V0041OpenapiPartitionRespPartitionsInnerPartition.md) |  | [optional] 
**suspend_time** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_partition_info import V0043PartitionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V0043PartitionInfo from a JSON string
v0043_partition_info_instance = V0043PartitionInfo.from_json(json)
# print the JSON string representation of the object
print(V0043PartitionInfo.to_json())

# convert the object into a dict
v0043_partition_info_dict = v0043_partition_info_instance.to_dict()
# create an instance of V0043PartitionInfo from a dict
v0043_partition_info_from_dict = V0043PartitionInfo.from_dict(v0043_partition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


