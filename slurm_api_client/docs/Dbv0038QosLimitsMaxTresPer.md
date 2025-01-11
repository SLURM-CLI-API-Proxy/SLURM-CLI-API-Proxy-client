# Dbv0038QosLimitsMaxTresPer

Max TRES per settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 
**job** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 
**node** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 
**user** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 

## Example

```python
from openapi_client.models.dbv0038_qos_limits_max_tres_per import Dbv0038QosLimitsMaxTresPer

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038QosLimitsMaxTresPer from a JSON string
dbv0038_qos_limits_max_tres_per_instance = Dbv0038QosLimitsMaxTresPer.from_json(json)
# print the JSON string representation of the object
print(Dbv0038QosLimitsMaxTresPer.to_json())

# convert the object into a dict
dbv0038_qos_limits_max_tres_per_dict = dbv0038_qos_limits_max_tres_per_instance.to_dict()
# create an instance of Dbv0038QosLimitsMaxTresPer from a dict
dbv0038_qos_limits_max_tres_per_from_dict = Dbv0038QosLimitsMaxTresPer.from_dict(dbv0038_qos_limits_max_tres_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


