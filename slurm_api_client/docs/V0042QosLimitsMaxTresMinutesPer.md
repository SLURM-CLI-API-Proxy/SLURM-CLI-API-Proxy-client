# V0042QosLimitsMaxTresMinutesPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qos** | [**List[V0042Tres]**](V0042Tres.md) |  | [optional] 
**job** | [**List[V0042Tres]**](V0042Tres.md) |  | [optional] 
**account** | [**List[V0042Tres]**](V0042Tres.md) |  | [optional] 
**user** | [**List[V0042Tres]**](V0042Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_qos_limits_max_tres_minutes_per import V0042QosLimitsMaxTresMinutesPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0042QosLimitsMaxTresMinutesPer from a JSON string
v0042_qos_limits_max_tres_minutes_per_instance = V0042QosLimitsMaxTresMinutesPer.from_json(json)
# print the JSON string representation of the object
print(V0042QosLimitsMaxTresMinutesPer.to_json())

# convert the object into a dict
v0042_qos_limits_max_tres_minutes_per_dict = v0042_qos_limits_max_tres_minutes_per_instance.to_dict()
# create an instance of V0042QosLimitsMaxTresMinutesPer from a dict
v0042_qos_limits_max_tres_minutes_per_from_dict = V0042QosLimitsMaxTresMinutesPer.from_dict(v0042_qos_limits_max_tres_minutes_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


