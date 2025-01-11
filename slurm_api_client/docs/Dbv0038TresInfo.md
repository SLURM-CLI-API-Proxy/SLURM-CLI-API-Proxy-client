# Dbv0038TresInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0038Meta**](Dbv0038Meta.md) |  | [optional] 
**errors** | [**List[Dbv0038Error]**](Dbv0038Error.md) | Slurm errors | [optional] 
**tres** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 

## Example

```python
from openapi_client.models.dbv0038_tres_info import Dbv0038TresInfo

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038TresInfo from a JSON string
dbv0038_tres_info_instance = Dbv0038TresInfo.from_json(json)
# print the JSON string representation of the object
print(Dbv0038TresInfo.to_json())

# convert the object into a dict
dbv0038_tres_info_dict = dbv0038_tres_info_instance.to_dict()
# create an instance of Dbv0038TresInfo from a dict
dbv0038_tres_info_from_dict = Dbv0038TresInfo.from_dict(dbv0038_tres_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


