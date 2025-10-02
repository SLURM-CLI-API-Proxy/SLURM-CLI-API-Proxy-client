# V0039PartitionInfoMaximums


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus_per_node** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**cpus_per_socket** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**memory_per_cpu** | **int** |  | [optional] 
**nodes** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**shares** | **int** |  | [optional] 
**time** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**over_time_limit** | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_partition_info_maximums import V0039PartitionInfoMaximums

# TODO update the JSON string below
json = "{}"
# create an instance of V0039PartitionInfoMaximums from a JSON string
v0039_partition_info_maximums_instance = V0039PartitionInfoMaximums.from_json(json)
# print the JSON string representation of the object
print(V0039PartitionInfoMaximums.to_json())

# convert the object into a dict
v0039_partition_info_maximums_dict = v0039_partition_info_maximums_instance.to_dict()
# create an instance of V0039PartitionInfoMaximums from a dict
v0039_partition_info_maximums_from_dict = V0039PartitionInfoMaximums.from_dict(v0039_partition_info_maximums_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


