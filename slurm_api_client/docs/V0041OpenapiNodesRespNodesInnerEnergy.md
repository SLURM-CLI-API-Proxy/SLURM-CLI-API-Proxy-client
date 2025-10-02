# V0041OpenapiNodesRespNodesInnerEnergy

Energy usage data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_watts** | **int** | Average power consumption, in watts | [optional] 
**base_consumed_energy** | **int** | The energy consumed between when the node was powered on and the last time it was registered by slurmd, in joules | [optional] 
**consumed_energy** | **int** | The energy consumed between the last time the node was registered by the slurmd daemon and the last node energy accounting sample, in joules | [optional] 
**current_watts** | [**V0041OpenapiNodesRespNodesInnerEnergyCurrentWatts**](V0041OpenapiNodesRespNodesInnerEnergyCurrentWatts.md) |  | [optional] 
**previous_consumed_energy** | **int** | Previous value of consumed_energy | [optional] 
**last_collected** | **int** | Time when energy data was last retrieved (UNIX timestamp) | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_nodes_resp_nodes_inner_energy import V0041OpenapiNodesRespNodesInnerEnergy

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiNodesRespNodesInnerEnergy from a JSON string
v0041_openapi_nodes_resp_nodes_inner_energy_instance = V0041OpenapiNodesRespNodesInnerEnergy.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiNodesRespNodesInnerEnergy.to_json())

# convert the object into a dict
v0041_openapi_nodes_resp_nodes_inner_energy_dict = v0041_openapi_nodes_resp_nodes_inner_energy_instance.to_dict()
# create an instance of V0041OpenapiNodesRespNodesInnerEnergy from a dict
v0041_openapi_nodes_resp_nodes_inner_energy_from_dict = V0041OpenapiNodesRespNodesInnerEnergy.from_dict(v0041_openapi_nodes_resp_nodes_inner_energy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


