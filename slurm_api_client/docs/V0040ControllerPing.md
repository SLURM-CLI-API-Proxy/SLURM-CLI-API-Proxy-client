# V0040ControllerPing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Target for ping | [optional] 
**pinged** | **str** | Ping result | [optional] 
**latency** | **int** | Number of microseconds it took to successfully ping or timeout | [optional] 
**mode** | **str** | The operating mode of the responding slurmctld | [optional] 

## Example

```python
from openapi_client.models.v0040_controller_ping import V0040ControllerPing

# TODO update the JSON string below
json = "{}"
# create an instance of V0040ControllerPing from a JSON string
v0040_controller_ping_instance = V0040ControllerPing.from_json(json)
# print the JSON string representation of the object
print(V0040ControllerPing.to_json())

# convert the object into a dict
v0040_controller_ping_dict = v0040_controller_ping_instance.to_dict()
# create an instance of V0040ControllerPing from a dict
v0040_controller_ping_from_dict = V0040ControllerPing.from_dict(v0040_controller_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


