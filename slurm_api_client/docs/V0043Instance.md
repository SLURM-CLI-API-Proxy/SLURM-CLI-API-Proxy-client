# V0043Instance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **str** | Cluster name | [optional] 
**extra** | **str** | Arbitrary string used for node filtering if extra constraints are enabled | [optional] 
**instance_id** | **str** | Cloud instance ID | [optional] 
**instance_type** | **str** | Cloud instance type | [optional] 
**node_name** | **str** | NodeName | [optional] 
**time** | [**V0043InstanceTime**](V0043InstanceTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_instance import V0043Instance

# TODO update the JSON string below
json = "{}"
# create an instance of V0043Instance from a JSON string
v0043_instance_instance = V0043Instance.from_json(json)
# print the JSON string representation of the object
print(V0043Instance.to_json())

# convert the object into a dict
v0043_instance_dict = v0043_instance_instance.to_dict()
# create an instance of V0043Instance from a dict
v0043_instance_from_dict = V0043Instance.from_dict(v0043_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


