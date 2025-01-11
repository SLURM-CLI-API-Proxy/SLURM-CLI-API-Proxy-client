# Dbv0039Diag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0039Meta**](Dbv0039Meta.md) |  | [optional] 
**errors** | [**List[Dbv0039Error]**](Dbv0039Error.md) | Slurm errors | [optional] 
**warnings** | [**List[Dbv0039Warning]**](Dbv0039Warning.md) | Slurm warnings | [optional] 
**statistics** | [**V0039StatsRec**](V0039StatsRec.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0039_diag import Dbv0039Diag

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0039Diag from a JSON string
dbv0039_diag_instance = Dbv0039Diag.from_json(json)
# print the JSON string representation of the object
print(Dbv0039Diag.to_json())

# convert the object into a dict
dbv0039_diag_dict = dbv0039_diag_instance.to_dict()
# create an instance of Dbv0039Diag from a dict
dbv0039_diag_from_dict = Dbv0039Diag.from_dict(dbv0039_diag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


