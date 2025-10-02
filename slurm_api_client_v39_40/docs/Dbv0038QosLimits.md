# Dbv0038QosLimits

Assigned limits

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor** | **float** | factor to apply to TRES count for associations using this QOS | [optional] 
**max** | [**Dbv0038QosLimitsMax**](Dbv0038QosLimitsMax.md) |  | [optional] 
**min** | [**Dbv0038QosLimitsMin**](Dbv0038QosLimitsMin.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0038_qos_limits import Dbv0038QosLimits

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038QosLimits from a JSON string
dbv0038_qos_limits_instance = Dbv0038QosLimits.from_json(json)
# print the JSON string representation of the object
print(Dbv0038QosLimits.to_json())

# convert the object into a dict
dbv0038_qos_limits_dict = dbv0038_qos_limits_instance.to_dict()
# create an instance of Dbv0038QosLimits from a dict
dbv0038_qos_limits_from_dict = Dbv0038QosLimits.from_dict(dbv0038_qos_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


