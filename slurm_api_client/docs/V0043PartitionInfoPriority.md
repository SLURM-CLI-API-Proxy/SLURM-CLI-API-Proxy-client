# V0043PartitionInfoPriority


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_factor** | **int** | PriorityJobFactor - Partition factor used by priority/multifactor plugin in calculating job priority | [optional] 
**tier** | **int** | PriorityTier - Controls the order in which the scheduler evaluates jobs from different partitions | [optional] 

## Example

```python
from openapi_client.models.v0043_partition_info_priority import V0043PartitionInfoPriority

# TODO update the JSON string below
json = "{}"
# create an instance of V0043PartitionInfoPriority from a JSON string
v0043_partition_info_priority_instance = V0043PartitionInfoPriority.from_json(json)
# print the JSON string representation of the object
print(V0043PartitionInfoPriority.to_json())

# convert the object into a dict
v0043_partition_info_priority_dict = v0043_partition_info_priority_instance.to_dict()
# create an instance of V0043PartitionInfoPriority from a dict
v0043_partition_info_priority_from_dict = V0043PartitionInfoPriority.from_dict(v0043_partition_info_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


