# Dbv0038AssociationMaxTresMinutes

Max TRES minutes settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per** | [**Dbv0038AssociationMaxTresMinutesPer**](Dbv0038AssociationMaxTresMinutesPer.md) |  | [optional] 
**total** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 

## Example

```python
from openapi_client.models.dbv0038_association_max_tres_minutes import Dbv0038AssociationMaxTresMinutes

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038AssociationMaxTresMinutes from a JSON string
dbv0038_association_max_tres_minutes_instance = Dbv0038AssociationMaxTresMinutes.from_json(json)
# print the JSON string representation of the object
print(Dbv0038AssociationMaxTresMinutes.to_json())

# convert the object into a dict
dbv0038_association_max_tres_minutes_dict = dbv0038_association_max_tres_minutes_instance.to_dict()
# create an instance of Dbv0038AssociationMaxTresMinutes from a dict
dbv0038_association_max_tres_minutes_from_dict = Dbv0038AssociationMaxTresMinutes.from_dict(dbv0038_association_max_tres_minutes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


