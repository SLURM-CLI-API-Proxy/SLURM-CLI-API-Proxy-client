# V0042QosLimitsMaxTresMinutes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0042Tres]**](V0042Tres.md) |  | [optional] 
**per** | [**V0042QosLimitsMaxTresMinutesPer**](V0042QosLimitsMaxTresMinutesPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_qos_limits_max_tres_minutes import V0042QosLimitsMaxTresMinutes

# TODO update the JSON string below
json = "{}"
# create an instance of V0042QosLimitsMaxTresMinutes from a JSON string
v0042_qos_limits_max_tres_minutes_instance = V0042QosLimitsMaxTresMinutes.from_json(json)
# print the JSON string representation of the object
print(V0042QosLimitsMaxTresMinutes.to_json())

# convert the object into a dict
v0042_qos_limits_max_tres_minutes_dict = v0042_qos_limits_max_tres_minutes_instance.to_dict()
# create an instance of V0042QosLimitsMaxTresMinutes from a dict
v0042_qos_limits_max_tres_minutes_from_dict = V0042QosLimitsMaxTresMinutes.from_dict(v0042_qos_limits_max_tres_minutes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


