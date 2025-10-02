# V0042QosLimitsMaxTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0042Tres]**](V0042Tres.md) |  | [optional] 
**minutes** | [**V0042QosLimitsMaxTresMinutes**](V0042QosLimitsMaxTresMinutes.md) |  | [optional] 
**per** | [**V0042QosLimitsMaxTresPer**](V0042QosLimitsMaxTresPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_qos_limits_max_tres import V0042QosLimitsMaxTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0042QosLimitsMaxTres from a JSON string
v0042_qos_limits_max_tres_instance = V0042QosLimitsMaxTres.from_json(json)
# print the JSON string representation of the object
print(V0042QosLimitsMaxTres.to_json())

# convert the object into a dict
v0042_qos_limits_max_tres_dict = v0042_qos_limits_max_tres_instance.to_dict()
# create an instance of V0042QosLimitsMaxTres from a dict
v0042_qos_limits_max_tres_from_dict = V0042QosLimitsMaxTres.from_dict(v0042_qos_limits_max_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


