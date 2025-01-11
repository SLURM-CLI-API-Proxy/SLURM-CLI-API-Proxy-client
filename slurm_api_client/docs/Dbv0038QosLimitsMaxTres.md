# Dbv0038QosLimitsMaxTres

Limits on TRES

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes** | [**Dbv0038QosLimitsMaxTresMinutes**](Dbv0038QosLimitsMaxTresMinutes.md) |  | [optional] 
**per** | [**Dbv0038QosLimitsMaxTresPer**](Dbv0038QosLimitsMaxTresPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0038_qos_limits_max_tres import Dbv0038QosLimitsMaxTres

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038QosLimitsMaxTres from a JSON string
dbv0038_qos_limits_max_tres_instance = Dbv0038QosLimitsMaxTres.from_json(json)
# print the JSON string representation of the object
print(Dbv0038QosLimitsMaxTres.to_json())

# convert the object into a dict
dbv0038_qos_limits_max_tres_dict = dbv0038_qos_limits_max_tres_instance.to_dict()
# create an instance of Dbv0038QosLimitsMaxTres from a dict
dbv0038_qos_limits_max_tres_from_dict = Dbv0038QosLimitsMaxTres.from_dict(dbv0038_qos_limits_max_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


