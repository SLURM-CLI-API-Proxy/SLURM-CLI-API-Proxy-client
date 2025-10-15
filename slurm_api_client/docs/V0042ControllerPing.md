# V0042ControllerPing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Target for ping | [optional] 
**pinged** | **str** | Ping result | [optional] 
**responding** | **bool** | If ping RPC responded with pong from controller | 
**latency** | **int** | Number of microseconds it took to successfully ping or timeout | [optional] 
**mode** | **str** | The operating mode of the responding slurmctld | [optional] 
**primary** | **bool** | Is responding slurmctld the primary controller | 

## Example

```python
from openapi_client.models.v0042_controller_ping import V0042ControllerPing

# TODO update the JSON string below
json = "{}"
# create an instance of V0042ControllerPing from a JSON string
v0042_controller_ping_instance = V0042ControllerPing.from_json(json)
# print the JSON string representation of the object
print(V0042ControllerPing.to_json())

# convert the object into a dict
v0042_controller_ping_dict = v0042_controller_ping_instance.to_dict()
# create an instance of V0042ControllerPing from a dict
v0042_controller_ping_from_dict = V0042ControllerPing.from_dict(v0042_controller_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


