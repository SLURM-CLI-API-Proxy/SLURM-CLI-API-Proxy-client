# V0038NodeAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory** | **int** | amount of assigned job memory | [optional] 
**cpus** | **int** | number of assigned job CPUs | [optional] 
**sockets** | [**V0038NodeAllocationSockets**](V0038NodeAllocationSockets.md) |  | [optional] 
**nodename** | **str** | node name | [optional] 

## Example

```python
from openapi_client.models.v0038_node_allocation import V0038NodeAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of V0038NodeAllocation from a JSON string
v0038_node_allocation_instance = V0038NodeAllocation.from_json(json)
# print the JSON string representation of the object
print(V0038NodeAllocation.to_json())

# convert the object into a dict
v0038_node_allocation_dict = v0038_node_allocation_instance.to_dict()
# create an instance of V0038NodeAllocation from a dict
v0038_node_allocation_from_dict = V0038NodeAllocation.from_dict(v0038_node_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


