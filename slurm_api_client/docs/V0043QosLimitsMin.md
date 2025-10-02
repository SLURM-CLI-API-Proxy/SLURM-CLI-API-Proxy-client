# V0043QosLimitsMin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority_threshold** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**tres** | [**V0043QosLimitsMinTres**](V0043QosLimitsMinTres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_qos_limits_min import V0043QosLimitsMin

# TODO update the JSON string below
json = "{}"
# create an instance of V0043QosLimitsMin from a JSON string
v0043_qos_limits_min_instance = V0043QosLimitsMin.from_json(json)
# print the JSON string representation of the object
print(V0043QosLimitsMin.to_json())

# convert the object into a dict
v0043_qos_limits_min_dict = v0043_qos_limits_min_instance.to_dict()
# create an instance of V0043QosLimitsMin from a dict
v0043_qos_limits_min_from_dict = V0043QosLimitsMin.from_dict(v0043_qos_limits_min_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


