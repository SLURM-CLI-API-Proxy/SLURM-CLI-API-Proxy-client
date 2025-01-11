# Dbv0038AssociationMaxTresPer

Max TRES per settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 
**node** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 

## Example

```python
from openapi_client.models.dbv0038_association_max_tres_per import Dbv0038AssociationMaxTresPer

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038AssociationMaxTresPer from a JSON string
dbv0038_association_max_tres_per_instance = Dbv0038AssociationMaxTresPer.from_json(json)
# print the JSON string representation of the object
print(Dbv0038AssociationMaxTresPer.to_json())

# convert the object into a dict
dbv0038_association_max_tres_per_dict = dbv0038_association_max_tres_per_instance.to_dict()
# create an instance of Dbv0038AssociationMaxTresPer from a dict
dbv0038_association_max_tres_per_from_dict = Dbv0038AssociationMaxTresPer.from_dict(dbv0038_association_max_tres_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


