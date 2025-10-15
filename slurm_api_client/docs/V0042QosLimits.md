# V0042QosLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grace_time** | **int** | GraceTime | [optional] 
**max** | [**V0042QosLimitsMax**](V0042QosLimitsMax.md) |  | [optional] 
**factor** | [**V0042Float64NoValStruct**](V0042Float64NoValStruct.md) |  | [optional] 
**min** | [**V0042QosLimitsMin**](V0042QosLimitsMin.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_qos_limits import V0042QosLimits

# TODO update the JSON string below
json = "{}"
# create an instance of V0042QosLimits from a JSON string
v0042_qos_limits_instance = V0042QosLimits.from_json(json)
# print the JSON string representation of the object
print(V0042QosLimits.to_json())

# convert the object into a dict
v0042_qos_limits_dict = v0042_qos_limits_instance.to_dict()
# create an instance of V0042QosLimits from a dict
v0042_qos_limits_from_dict = V0042QosLimits.from_dict(v0042_qos_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


