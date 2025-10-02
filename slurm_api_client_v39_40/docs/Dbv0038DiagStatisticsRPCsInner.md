# Dbv0038DiagStatisticsRPCsInner

Statistics by RPC type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rpc** | **str** | RPC type | [optional] 
**count** | **int** | Number of RPCs | [optional] 
**time** | [**Dbv0038DiagStatisticsRPCsInnerTime**](Dbv0038DiagStatisticsRPCsInnerTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0038_diag_statistics_rpcs_inner import Dbv0038DiagStatisticsRPCsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038DiagStatisticsRPCsInner from a JSON string
dbv0038_diag_statistics_rpcs_inner_instance = Dbv0038DiagStatisticsRPCsInner.from_json(json)
# print the JSON string representation of the object
print(Dbv0038DiagStatisticsRPCsInner.to_json())

# convert the object into a dict
dbv0038_diag_statistics_rpcs_inner_dict = dbv0038_diag_statistics_rpcs_inner_instance.to_dict()
# create an instance of Dbv0038DiagStatisticsRPCsInner from a dict
dbv0038_diag_statistics_rpcs_inner_from_dict = Dbv0038DiagStatisticsRPCsInner.from_dict(dbv0038_diag_statistics_rpcs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


