# V0040QosLimitsMaxTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**minutes** | [**V0040QosLimitsMaxTresMinutes**](V0040QosLimitsMaxTresMinutes.md) |  | [optional] 
**per** | [**V0040QosLimitsMaxTresPer**](V0040QosLimitsMaxTresPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_qos_limits_max_tres import V0040QosLimitsMaxTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0040QosLimitsMaxTres from a JSON string
v0040_qos_limits_max_tres_instance = V0040QosLimitsMaxTres.from_json(json)
# print the JSON string representation of the object
print(V0040QosLimitsMaxTres.to_json())

# convert the object into a dict
v0040_qos_limits_max_tres_dict = v0040_qos_limits_max_tres_instance.to_dict()
# create an instance of V0040QosLimitsMaxTres from a dict
v0040_qos_limits_max_tres_from_dict = V0040QosLimitsMaxTres.from_dict(v0040_qos_limits_max_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


