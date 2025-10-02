# V0042QosLimitsMin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority_threshold** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**tres** | [**V0042QosLimitsMinTres**](V0042QosLimitsMinTres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_qos_limits_min import V0042QosLimitsMin

# TODO update the JSON string below
json = "{}"
# create an instance of V0042QosLimitsMin from a JSON string
v0042_qos_limits_min_instance = V0042QosLimitsMin.from_json(json)
# print the JSON string representation of the object
print(V0042QosLimitsMin.to_json())

# convert the object into a dict
v0042_qos_limits_min_dict = v0042_qos_limits_min_instance.to_dict()
# create an instance of V0042QosLimitsMin from a dict
v0042_qos_limits_min_from_dict = V0042QosLimitsMin.from_dict(v0042_qos_limits_min_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


