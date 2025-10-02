# Dbv0038AssociationMaxTres

Max TRES settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per** | [**Dbv0038AssociationMaxTresPer**](Dbv0038AssociationMaxTresPer.md) |  | [optional] 
**total** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 
**minutes** | [**Dbv0038AssociationMaxTresMinutes**](Dbv0038AssociationMaxTresMinutes.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0038_association_max_tres import Dbv0038AssociationMaxTres

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038AssociationMaxTres from a JSON string
dbv0038_association_max_tres_instance = Dbv0038AssociationMaxTres.from_json(json)
# print the JSON string representation of the object
print(Dbv0038AssociationMaxTres.to_json())

# convert the object into a dict
dbv0038_association_max_tres_dict = dbv0038_association_max_tres_instance.to_dict()
# create an instance of Dbv0038AssociationMaxTres from a dict
dbv0038_association_max_tres_from_dict = Dbv0038AssociationMaxTres.from_dict(dbv0038_association_max_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


