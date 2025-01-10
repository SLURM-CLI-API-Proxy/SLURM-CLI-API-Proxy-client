# Dbv0038DiagStatisticsUsersInner

Statistics by user RPCs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | User name | [optional] 
**count** | **int** | Number of RPCs | [optional] 
**time** | [**Dbv0038DiagStatisticsUsersInnerTime**](Dbv0038DiagStatisticsUsersInnerTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0038_diag_statistics_users_inner import Dbv0038DiagStatisticsUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038DiagStatisticsUsersInner from a JSON string
dbv0038_diag_statistics_users_inner_instance = Dbv0038DiagStatisticsUsersInner.from_json(json)
# print the JSON string representation of the object
print(Dbv0038DiagStatisticsUsersInner.to_json())

# convert the object into a dict
dbv0038_diag_statistics_users_inner_dict = dbv0038_diag_statistics_users_inner_instance.to_dict()
# create an instance of Dbv0038DiagStatisticsUsersInner from a dict
dbv0038_diag_statistics_users_inner_from_dict = Dbv0038DiagStatisticsUsersInner.from_dict(dbv0038_diag_statistics_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


