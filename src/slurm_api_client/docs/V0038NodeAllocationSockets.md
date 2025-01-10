# V0038NodeAllocationSockets

assignment status of each socket by numeric socket id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cores** | **object** | assignment status of each core by core id in each socket | [optional] 

## Example

```python
from openapi_client.models.v0038_node_allocation_sockets import V0038NodeAllocationSockets

# TODO update the JSON string below
json = "{}"
# create an instance of V0038NodeAllocationSockets from a JSON string
v0038_node_allocation_sockets_instance = V0038NodeAllocationSockets.from_json(json)
# print the JSON string representation of the object
print(V0038NodeAllocationSockets.to_json())

# convert the object into a dict
v0038_node_allocation_sockets_dict = v0038_node_allocation_sockets_instance.to_dict()
# create an instance of V0038NodeAllocationSockets from a dict
v0038_node_allocation_sockets_from_dict = V0038NodeAllocationSockets.from_dict(v0038_node_allocation_sockets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


