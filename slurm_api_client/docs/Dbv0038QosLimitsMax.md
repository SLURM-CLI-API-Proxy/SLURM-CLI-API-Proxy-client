# Dbv0038QosLimitsMax

Limits on max settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wall_clock** | [**Dbv0038QosLimitsMaxWallClock**](Dbv0038QosLimitsMaxWallClock.md) |  | [optional] 
**jobs** | [**Dbv0038QosLimitsMaxJobs**](Dbv0038QosLimitsMaxJobs.md) |  | [optional] 
**accruing** | [**Dbv0038QosLimitsMaxAccruing**](Dbv0038QosLimitsMaxAccruing.md) |  | [optional] 
**tres** | [**Dbv0038QosLimitsMaxTres**](Dbv0038QosLimitsMaxTres.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0038_qos_limits_max import Dbv0038QosLimitsMax

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038QosLimitsMax from a JSON string
dbv0038_qos_limits_max_instance = Dbv0038QosLimitsMax.from_json(json)
# print the JSON string representation of the object
print(Dbv0038QosLimitsMax.to_json())

# convert the object into a dict
dbv0038_qos_limits_max_dict = dbv0038_qos_limits_max_instance.to_dict()
# create an instance of Dbv0038QosLimitsMax from a dict
dbv0038_qos_limits_max_from_dict = Dbv0038QosLimitsMax.from_dict(dbv0038_qos_limits_max_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


