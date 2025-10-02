# V0043ControllerPing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Target for ping | [optional] 
**pinged** | **str** | Ping result | [optional] 
**responding** | **bool** | If ping RPC responded with pong from controller | 
**latency** | **int** | Number of microseconds it took to successfully ping or timeout | [optional] 
**mode** | **str** | The operating mode of the responding slurmctld | [optional] 
**primary** | **bool** | Is responding slurmctld the primary controller (Is responding slurmctld the primary controller) | 

## Example

```python
from openapi_client.models.v0043_controller_ping import V0043ControllerPing

# TODO update the JSON string below
json = "{}"
# create an instance of V0043ControllerPing from a JSON string
v0043_controller_ping_instance = V0043ControllerPing.from_json(json)
# print the JSON string representation of the object
print(V0043ControllerPing.to_json())

# convert the object into a dict
v0043_controller_ping_dict = v0043_controller_ping_instance.to_dict()
# create an instance of V0043ControllerPing from a dict
v0043_controller_ping_from_dict = V0043ControllerPing.from_dict(v0043_controller_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


