# Dbv0038QosLimitsMin

Min limit settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority_threshold** | **int** | Min priority threshold | [optional] 
**tres** | [**Dbv0038QosLimitsMinTres**](Dbv0038QosLimitsMinTres.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0038_qos_limits_min import Dbv0038QosLimitsMin

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038QosLimitsMin from a JSON string
dbv0038_qos_limits_min_instance = Dbv0038QosLimitsMin.from_json(json)
# print the JSON string representation of the object
print(Dbv0038QosLimitsMin.to_json())

# convert the object into a dict
dbv0038_qos_limits_min_dict = dbv0038_qos_limits_min_instance.to_dict()
# create an instance of Dbv0038QosLimitsMin from a dict
dbv0038_qos_limits_min_from_dict = Dbv0038QosLimitsMin.from_dict(dbv0038_qos_limits_min_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


