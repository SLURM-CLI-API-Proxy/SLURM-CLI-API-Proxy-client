# Dbv0038Diag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0038Meta**](Dbv0038Meta.md) |  | [optional] 
**errors** | [**List[Dbv0038Error]**](Dbv0038Error.md) | Slurm errors | [optional] 
**statistics** | [**Dbv0038DiagStatistics**](Dbv0038DiagStatistics.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0038_diag import Dbv0038Diag

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038Diag from a JSON string
dbv0038_diag_instance = Dbv0038Diag.from_json(json)
# print the JSON string representation of the object
print(Dbv0038Diag.to_json())

# convert the object into a dict
dbv0038_diag_dict = dbv0038_diag_instance.to_dict()
# create an instance of Dbv0038Diag from a dict
dbv0038_diag_from_dict = Dbv0038Diag.from_dict(dbv0038_diag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


