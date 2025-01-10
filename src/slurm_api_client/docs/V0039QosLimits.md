# V0039QosLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grace_time** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**max** | [**V0039QosLimitsMax**](V0039QosLimitsMax.md) |  | [optional] 
**factor** | **float** |  | [optional] 
**min** | [**V0039QosLimitsMin**](V0039QosLimitsMin.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_qos_limits import V0039QosLimits

# TODO update the JSON string below
json = "{}"
# create an instance of V0039QosLimits from a JSON string
v0039_qos_limits_instance = V0039QosLimits.from_json(json)
# print the JSON string representation of the object
print(V0039QosLimits.to_json())

# convert the object into a dict
v0039_qos_limits_dict = v0039_qos_limits_instance.to_dict()
# create an instance of V0039QosLimits from a dict
v0039_qos_limits_from_dict = V0039QosLimits.from_dict(v0039_qos_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


