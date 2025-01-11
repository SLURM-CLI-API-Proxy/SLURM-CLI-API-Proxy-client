# V0039PowerMgmtData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_watts** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**current_watts** | **int** |  | [optional] 
**total_energy** | **int** |  | [optional] 
**new_maximum_watts** | **int** |  | [optional] 
**peak_watts** | **int** |  | [optional] 
**lowest_watts** | **int** |  | [optional] 
**new_job_time** | **int** |  | [optional] 
**state** | **int** |  | [optional] 
**time_start_day** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.v0039_power_mgmt_data import V0039PowerMgmtData

# TODO update the JSON string below
json = "{}"
# create an instance of V0039PowerMgmtData from a JSON string
v0039_power_mgmt_data_instance = V0039PowerMgmtData.from_json(json)
# print the JSON string representation of the object
print(V0039PowerMgmtData.to_json())

# convert the object into a dict
v0039_power_mgmt_data_dict = v0039_power_mgmt_data_instance.to_dict()
# create an instance of V0039PowerMgmtData from a dict
v0039_power_mgmt_data_from_dict = V0039PowerMgmtData.from_dict(v0039_power_mgmt_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


