# V0039PartitionInfoDefaults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_per_cpu** | **int** |  | [optional] 
**time** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**job** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v0039_partition_info_defaults import V0039PartitionInfoDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of V0039PartitionInfoDefaults from a JSON string
v0039_partition_info_defaults_instance = V0039PartitionInfoDefaults.from_json(json)
# print the JSON string representation of the object
print(V0039PartitionInfoDefaults.to_json())

# convert the object into a dict
v0039_partition_info_defaults_dict = v0039_partition_info_defaults_instance.to_dict()
# create an instance of V0039PartitionInfoDefaults from a dict
v0039_partition_info_defaults_from_dict = V0039PartitionInfoDefaults.from_dict(v0039_partition_info_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


