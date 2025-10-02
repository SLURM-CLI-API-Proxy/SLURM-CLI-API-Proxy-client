# V0040QosLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grace_time** | **int** | GraceTime | [optional] 
**max** | [**V0040QosLimitsMax**](V0040QosLimitsMax.md) |  | [optional] 
**factor** | [**V0040Float64NoVal**](V0040Float64NoVal.md) |  | [optional] 
**min** | [**V0040QosLimitsMin**](V0040QosLimitsMin.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_qos_limits import V0040QosLimits

# TODO update the JSON string below
json = "{}"
# create an instance of V0040QosLimits from a JSON string
v0040_qos_limits_instance = V0040QosLimits.from_json(json)
# print the JSON string representation of the object
print(V0040QosLimits.to_json())

# convert the object into a dict
v0040_qos_limits_dict = v0040_qos_limits_instance.to_dict()
# create an instance of V0040QosLimits from a dict
v0040_qos_limits_from_dict = V0040QosLimits.from_dict(v0040_qos_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


