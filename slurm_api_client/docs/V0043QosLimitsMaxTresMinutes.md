# V0043QosLimitsMaxTresMinutes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0043Tres]**](V0043Tres.md) |  | [optional] 
**per** | [**V0043QosLimitsMaxTresMinutesPer**](V0043QosLimitsMaxTresMinutesPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_qos_limits_max_tres_minutes import V0043QosLimitsMaxTresMinutes

# TODO update the JSON string below
json = "{}"
# create an instance of V0043QosLimitsMaxTresMinutes from a JSON string
v0043_qos_limits_max_tres_minutes_instance = V0043QosLimitsMaxTresMinutes.from_json(json)
# print the JSON string representation of the object
print(V0043QosLimitsMaxTresMinutes.to_json())

# convert the object into a dict
v0043_qos_limits_max_tres_minutes_dict = v0043_qos_limits_max_tres_minutes_instance.to_dict()
# create an instance of V0043QosLimitsMaxTresMinutes from a dict
v0043_qos_limits_max_tres_minutes_from_dict = V0043QosLimitsMaxTresMinutes.from_dict(v0043_qos_limits_max_tres_minutes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


