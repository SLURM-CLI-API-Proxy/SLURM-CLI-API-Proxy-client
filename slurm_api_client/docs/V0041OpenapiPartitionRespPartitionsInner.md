# V0041OpenapiPartitionRespPartitionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**V0040PartitionInfoNodes**](V0040PartitionInfoNodes.md) |  | [optional] 
**accounts** | [**V0040PartitionInfoAccounts**](V0040PartitionInfoAccounts.md) |  | [optional] 
**groups** | [**V0040PartitionInfoGroups**](V0040PartitionInfoGroups.md) |  | [optional] 
**qos** | [**V0040PartitionInfoQos**](V0040PartitionInfoQos.md) |  | [optional] 
**alternate** | **str** | Alternate | [optional] 
**tres** | [**V0040PartitionInfoTres**](V0040PartitionInfoTres.md) |  | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**select_type** | **List[str]** | Scheduler consumable resource selection type | [optional] 
**cpus** | [**V0040PartitionInfoCpus**](V0040PartitionInfoCpus.md) |  | [optional] 
**defaults** | [**V0041OpenapiPartitionRespPartitionsInnerDefaults**](V0041OpenapiPartitionRespPartitionsInnerDefaults.md) |  | [optional] 
**grace_time** | **int** | GraceTime | [optional] 
**maximums** | [**V0041OpenapiPartitionRespPartitionsInnerMaximums**](V0041OpenapiPartitionRespPartitionsInnerMaximums.md) |  | [optional] 
**minimums** | [**V0040PartitionInfoMinimums**](V0040PartitionInfoMinimums.md) |  | [optional] 
**name** | **str** | PartitionName | [optional] 
**node_sets** | **str** | NodeSets | [optional] 
**priority** | [**V0040PartitionInfoPriority**](V0040PartitionInfoPriority.md) |  | [optional] 
**timeouts** | [**V0041OpenapiPartitionRespPartitionsInnerTimeouts**](V0041OpenapiPartitionRespPartitionsInnerTimeouts.md) |  | [optional] 
**partition** | [**V0041OpenapiPartitionRespPartitionsInnerPartition**](V0041OpenapiPartitionRespPartitionsInnerPartition.md) |  | [optional] 
**suspend_time** | [**V0041OpenapiPartitionRespPartitionsInnerSuspendTime**](V0041OpenapiPartitionRespPartitionsInnerSuspendTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner import V0041OpenapiPartitionRespPartitionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiPartitionRespPartitionsInner from a JSON string
v0041_openapi_partition_resp_partitions_inner_instance = V0041OpenapiPartitionRespPartitionsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiPartitionRespPartitionsInner.to_json())

# convert the object into a dict
v0041_openapi_partition_resp_partitions_inner_dict = v0041_openapi_partition_resp_partitions_inner_instance.to_dict()
# create an instance of V0041OpenapiPartitionRespPartitionsInner from a dict
v0041_openapi_partition_resp_partitions_inner_from_dict = V0041OpenapiPartitionRespPartitionsInner.from_dict(v0041_openapi_partition_resp_partitions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


