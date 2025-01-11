# V0040Instance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **str** |  | [optional] 
**extra** | **str** |  | [optional] 
**instance_id** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 
**node_name** | **str** |  | [optional] 
**time** | [**V0040InstanceTime**](V0040InstanceTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_instance import V0040Instance

# TODO update the JSON string below
json = "{}"
# create an instance of V0040Instance from a JSON string
v0040_instance_instance = V0040Instance.from_json(json)
# print the JSON string representation of the object
print(V0040Instance.to_json())

# convert the object into a dict
v0040_instance_dict = v0040_instance_instance.to_dict()
# create an instance of V0040Instance from a dict
v0040_instance_from_dict = V0040Instance.from_dict(v0040_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


