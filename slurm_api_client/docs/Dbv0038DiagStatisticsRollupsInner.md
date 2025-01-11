# Dbv0038DiagStatisticsRollupsInner

Rollup statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of rollup | [optional] 
**last_run** | **int** | Timestamp of last rollup | [optional] 
**last_cycle** | **int** | Timestamp of last cycle | [optional] 
**max_cycle** | **int** | Max time of all cycles | [optional] 
**total_time** | **int** | Total time (s) spent doing rollup | [optional] 
**mean_cycles** | **int** | Average time (s) of cycle | [optional] 

## Example

```python
from openapi_client.models.dbv0038_diag_statistics_rollups_inner import Dbv0038DiagStatisticsRollupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038DiagStatisticsRollupsInner from a JSON string
dbv0038_diag_statistics_rollups_inner_instance = Dbv0038DiagStatisticsRollupsInner.from_json(json)
# print the JSON string representation of the object
print(Dbv0038DiagStatisticsRollupsInner.to_json())

# convert the object into a dict
dbv0038_diag_statistics_rollups_inner_dict = dbv0038_diag_statistics_rollups_inner_instance.to_dict()
# create an instance of Dbv0038DiagStatisticsRollupsInner from a dict
dbv0038_diag_statistics_rollups_inner_from_dict = Dbv0038DiagStatisticsRollupsInner.from_dict(dbv0038_diag_statistics_rollups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


