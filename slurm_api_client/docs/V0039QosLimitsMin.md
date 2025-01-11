# V0039QosLimitsMin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority_threshold** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**tres** | [**V0039QosLimitsMinTres**](V0039QosLimitsMinTres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_qos_limits_min import V0039QosLimitsMin

# TODO update the JSON string below
json = "{}"
# create an instance of V0039QosLimitsMin from a JSON string
v0039_qos_limits_min_instance = V0039QosLimitsMin.from_json(json)
# print the JSON string representation of the object
print(V0039QosLimitsMin.to_json())

# convert the object into a dict
v0039_qos_limits_min_dict = v0039_qos_limits_min_instance.to_dict()
# create an instance of V0039QosLimitsMin from a dict
v0039_qos_limits_min_from_dict = V0039QosLimitsMin.from_dict(v0039_qos_limits_min_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


