# V0040PartitionInfoPriority


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_factor** | **int** | PriorityJobFactor | [optional] 
**tier** | **int** | PriorityTier | [optional] 

## Example

```python
from openapi_client.models.v0040_partition_info_priority import V0040PartitionInfoPriority

# TODO update the JSON string below
json = "{}"
# create an instance of V0040PartitionInfoPriority from a JSON string
v0040_partition_info_priority_instance = V0040PartitionInfoPriority.from_json(json)
# print the JSON string representation of the object
print(V0040PartitionInfoPriority.to_json())

# convert the object into a dict
v0040_partition_info_priority_dict = v0040_partition_info_priority_instance.to_dict()
# create an instance of V0040PartitionInfoPriority from a dict
v0040_partition_info_priority_from_dict = V0040PartitionInfoPriority.from_dict(v0040_partition_info_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


