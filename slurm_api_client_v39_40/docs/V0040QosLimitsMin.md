# V0040QosLimitsMin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority_threshold** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**tres** | [**V0040QosLimitsMinTres**](V0040QosLimitsMinTres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_qos_limits_min import V0040QosLimitsMin

# TODO update the JSON string below
json = "{}"
# create an instance of V0040QosLimitsMin from a JSON string
v0040_qos_limits_min_instance = V0040QosLimitsMin.from_json(json)
# print the JSON string representation of the object
print(V0040QosLimitsMin.to_json())

# convert the object into a dict
v0040_qos_limits_min_dict = v0040_qos_limits_min_instance.to_dict()
# create an instance of V0040QosLimitsMin from a dict
v0040_qos_limits_min_from_dict = V0040QosLimitsMin.from_dict(v0040_qos_limits_min_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


