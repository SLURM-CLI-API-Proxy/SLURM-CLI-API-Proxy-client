# V0040InstanceTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_end** | **int** | When the instance will end (UNIX timestamp) | [optional] 
**time_start** | **int** | When the instance will start (UNIX timestamp) | [optional] 

## Example

```python
from openapi_client.models.v0040_instance_time import V0040InstanceTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0040InstanceTime from a JSON string
v0040_instance_time_instance = V0040InstanceTime.from_json(json)
# print the JSON string representation of the object
print(V0040InstanceTime.to_json())

# convert the object into a dict
v0040_instance_time_dict = v0040_instance_time_instance.to_dict()
# create an instance of V0040InstanceTime from a dict
v0040_instance_time_from_dict = V0040InstanceTime.from_dict(v0040_instance_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


