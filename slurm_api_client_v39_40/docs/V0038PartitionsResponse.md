# V0038PartitionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**V0038Meta**](V0038Meta.md) |  | [optional] 
**errors** | [**List[V0038Error]**](V0038Error.md) | slurm errors | [optional] 
**partitions** | [**List[V0038Partition]**](V0038Partition.md) | partition info | [optional] 

## Example

```python
from openapi_client.models.v0038_partitions_response import V0038PartitionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V0038PartitionsResponse from a JSON string
v0038_partitions_response_instance = V0038PartitionsResponse.from_json(json)
# print the JSON string representation of the object
print(V0038PartitionsResponse.to_json())

# convert the object into a dict
v0038_partitions_response_dict = v0038_partitions_response_instance.to_dict()
# create an instance of V0038PartitionsResponse from a dict
v0038_partitions_response_from_dict = V0038PartitionsResponse.from_dict(v0038_partitions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


