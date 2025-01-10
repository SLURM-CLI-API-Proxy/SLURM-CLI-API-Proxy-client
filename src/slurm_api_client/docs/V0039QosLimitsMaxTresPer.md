# V0039QosLimitsMaxTresPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**List[V0039Tres]**](V0039Tres.md) |  | [optional] 
**job** | [**List[V0039Tres]**](V0039Tres.md) |  | [optional] 
**node** | [**List[V0039Tres]**](V0039Tres.md) |  | [optional] 
**user** | [**List[V0039Tres]**](V0039Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_qos_limits_max_tres_per import V0039QosLimitsMaxTresPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0039QosLimitsMaxTresPer from a JSON string
v0039_qos_limits_max_tres_per_instance = V0039QosLimitsMaxTresPer.from_json(json)
# print the JSON string representation of the object
print(V0039QosLimitsMaxTresPer.to_json())

# convert the object into a dict
v0039_qos_limits_max_tres_per_dict = v0039_qos_limits_max_tres_per_instance.to_dict()
# create an instance of V0039QosLimitsMaxTresPer from a dict
v0039_qos_limits_max_tres_per_from_dict = V0039QosLimitsMaxTresPer.from_dict(v0039_qos_limits_max_tres_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


