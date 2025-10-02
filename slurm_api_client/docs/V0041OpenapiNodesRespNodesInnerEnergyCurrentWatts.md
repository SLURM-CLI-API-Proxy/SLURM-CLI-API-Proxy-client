# V0041OpenapiNodesRespNodesInnerEnergyCurrentWatts

The instantaneous power consumption at the time of the last node energy accounting sample, in watts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_nodes_resp_nodes_inner_energy_current_watts import V0041OpenapiNodesRespNodesInnerEnergyCurrentWatts

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiNodesRespNodesInnerEnergyCurrentWatts from a JSON string
v0041_openapi_nodes_resp_nodes_inner_energy_current_watts_instance = V0041OpenapiNodesRespNodesInnerEnergyCurrentWatts.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiNodesRespNodesInnerEnergyCurrentWatts.to_json())

# convert the object into a dict
v0041_openapi_nodes_resp_nodes_inner_energy_current_watts_dict = v0041_openapi_nodes_resp_nodes_inner_energy_current_watts_instance.to_dict()
# create an instance of V0041OpenapiNodesRespNodesInnerEnergyCurrentWatts from a dict
v0041_openapi_nodes_resp_nodes_inner_energy_current_watts_from_dict = V0041OpenapiNodesRespNodesInnerEnergyCurrentWatts.from_dict(v0041_openapi_nodes_resp_nodes_inner_energy_current_watts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


