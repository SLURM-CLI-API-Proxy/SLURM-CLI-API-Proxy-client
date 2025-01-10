# V0039ExtSensorsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumed_energy** | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) |  | [optional] 
**temperature** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**energy_update_time** | **int** |  | [optional] 
**current_watts** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.v0039_ext_sensors_data import V0039ExtSensorsData

# TODO update the JSON string below
json = "{}"
# create an instance of V0039ExtSensorsData from a JSON string
v0039_ext_sensors_data_instance = V0039ExtSensorsData.from_json(json)
# print the JSON string representation of the object
print(V0039ExtSensorsData.to_json())

# convert the object into a dict
v0039_ext_sensors_data_dict = v0039_ext_sensors_data_instance.to_dict()
# create an instance of V0039ExtSensorsData from a dict
v0039_ext_sensors_data_from_dict = V0039ExtSensorsData.from_dict(v0039_ext_sensors_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


