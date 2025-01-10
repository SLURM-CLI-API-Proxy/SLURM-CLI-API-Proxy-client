# Dbv0038DiagStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_start** | **int** | Unix timestamp of start time | [optional] 
**rollups** | [**List[Dbv0038DiagStatisticsRollupsInner]**](Dbv0038DiagStatisticsRollupsInner.md) |  | [optional] 
**rpcs** | [**List[Dbv0038DiagStatisticsRPCsInner]**](Dbv0038DiagStatisticsRPCsInner.md) |  | [optional] 
**users** | [**List[Dbv0038DiagStatisticsUsersInner]**](Dbv0038DiagStatisticsUsersInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0038_diag_statistics import Dbv0038DiagStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038DiagStatistics from a JSON string
dbv0038_diag_statistics_instance = Dbv0038DiagStatistics.from_json(json)
# print the JSON string representation of the object
print(Dbv0038DiagStatistics.to_json())

# convert the object into a dict
dbv0038_diag_statistics_dict = dbv0038_diag_statistics_instance.to_dict()
# create an instance of Dbv0038DiagStatistics from a dict
dbv0038_diag_statistics_from_dict = Dbv0038DiagStatistics.from_dict(dbv0038_diag_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


