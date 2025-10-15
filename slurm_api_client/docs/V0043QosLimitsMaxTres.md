# V0043QosLimitsMaxTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0043Tres]**](V0043Tres.md) |  | [optional] 
**minutes** | [**V0043QosLimitsMaxTresMinutes**](V0043QosLimitsMaxTresMinutes.md) |  | [optional] 
**per** | [**V0043QosLimitsMaxTresPer**](V0043QosLimitsMaxTresPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_qos_limits_max_tres import V0043QosLimitsMaxTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0043QosLimitsMaxTres from a JSON string
v0043_qos_limits_max_tres_instance = V0043QosLimitsMaxTres.from_json(json)
# print the JSON string representation of the object
print(V0043QosLimitsMaxTres.to_json())

# convert the object into a dict
v0043_qos_limits_max_tres_dict = v0043_qos_limits_max_tres_instance.to_dict()
# create an instance of V0043QosLimitsMaxTres from a dict
v0043_qos_limits_max_tres_from_dict = V0043QosLimitsMaxTres.from_dict(v0043_qos_limits_max_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


