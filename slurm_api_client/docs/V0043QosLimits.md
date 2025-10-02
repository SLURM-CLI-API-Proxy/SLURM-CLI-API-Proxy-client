# V0043QosLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grace_time** | **int** | GraceTime - Preemption grace time in seconds to be extended to a job which has been selected for preemption | [optional] 
**max** | [**V0043QosLimitsMax**](V0043QosLimitsMax.md) |  | [optional] 
**factor** | [**V0043Float64NoValStruct**](V0043Float64NoValStruct.md) |  | [optional] 
**min** | [**V0043QosLimitsMin**](V0043QosLimitsMin.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_qos_limits import V0043QosLimits

# TODO update the JSON string below
json = "{}"
# create an instance of V0043QosLimits from a JSON string
v0043_qos_limits_instance = V0043QosLimits.from_json(json)
# print the JSON string representation of the object
print(V0043QosLimits.to_json())

# convert the object into a dict
v0043_qos_limits_dict = v0043_qos_limits_instance.to_dict()
# create an instance of V0043QosLimits from a dict
v0043_qos_limits_from_dict = V0043QosLimits.from_dict(v0043_qos_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


