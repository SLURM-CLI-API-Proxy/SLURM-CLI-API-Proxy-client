# V0040PowerMgmtData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_watts** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**current_watts** | **int** |  | [optional] 
**total_energy** | **int** |  | [optional] 
**new_maximum_watts** | **int** |  | [optional] 
**peak_watts** | **int** |  | [optional] 
**lowest_watts** | **int** |  | [optional] 
**new_job_time** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**state** | **int** |  | [optional] 
**time_start_day** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.v0040_power_mgmt_data import V0040PowerMgmtData

# TODO update the JSON string below
json = "{}"
# create an instance of V0040PowerMgmtData from a JSON string
v0040_power_mgmt_data_instance = V0040PowerMgmtData.from_json(json)
# print the JSON string representation of the object
print(V0040PowerMgmtData.to_json())

# convert the object into a dict
v0040_power_mgmt_data_dict = v0040_power_mgmt_data_instance.to_dict()
# create an instance of V0040PowerMgmtData from a dict
v0040_power_mgmt_data_from_dict = V0040PowerMgmtData.from_dict(v0040_power_mgmt_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


