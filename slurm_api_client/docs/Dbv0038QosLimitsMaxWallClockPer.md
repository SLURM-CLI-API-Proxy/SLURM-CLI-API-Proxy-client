# Dbv0038QosLimitsMaxWallClockPer

Limit on wallclock per settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qos** | **int** | Max wallclock per QOS | [optional] 
**job** | **int** | Max wallclock per job | [optional] 

## Example

```python
from openapi_client.models.dbv0038_qos_limits_max_wall_clock_per import Dbv0038QosLimitsMaxWallClockPer

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038QosLimitsMaxWallClockPer from a JSON string
dbv0038_qos_limits_max_wall_clock_per_instance = Dbv0038QosLimitsMaxWallClockPer.from_json(json)
# print the JSON string representation of the object
print(Dbv0038QosLimitsMaxWallClockPer.to_json())

# convert the object into a dict
dbv0038_qos_limits_max_wall_clock_per_dict = dbv0038_qos_limits_max_wall_clock_per_instance.to_dict()
# create an instance of Dbv0038QosLimitsMaxWallClockPer from a dict
dbv0038_qos_limits_max_wall_clock_per_from_dict = Dbv0038QosLimitsMaxWallClockPer.from_dict(dbv0038_qos_limits_max_wall_clock_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


