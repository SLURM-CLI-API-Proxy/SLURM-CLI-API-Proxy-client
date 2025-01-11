# V0039QosLimitsMaxTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0039Tres]**](V0039Tres.md) |  | [optional] 
**minutes** | [**V0039QosLimitsMaxTresMinutes**](V0039QosLimitsMaxTresMinutes.md) |  | [optional] 
**per** | [**V0039QosLimitsMaxTresPer**](V0039QosLimitsMaxTresPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_qos_limits_max_tres import V0039QosLimitsMaxTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0039QosLimitsMaxTres from a JSON string
v0039_qos_limits_max_tres_instance = V0039QosLimitsMaxTres.from_json(json)
# print the JSON string representation of the object
print(V0039QosLimitsMaxTres.to_json())

# convert the object into a dict
v0039_qos_limits_max_tres_dict = v0039_qos_limits_max_tres_instance.to_dict()
# create an instance of V0039QosLimitsMaxTres from a dict
v0039_qos_limits_max_tres_from_dict = V0039QosLimitsMaxTres.from_dict(v0039_qos_limits_max_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


