# Dbv0038Account

Account description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associations** | [**List[Dbv0038AssociationShortInfo]**](Dbv0038AssociationShortInfo.md) | List of assigned associations | [optional] 
**coordinators** | [**List[Dbv0038CoordinatorInfo]**](Dbv0038CoordinatorInfo.md) | List of assigned coordinators | [optional] 
**description** | **str** | Description of account | [optional] 
**name** | **str** | Name of account | [optional] 
**organization** | **str** | Assigned organization of account | [optional] 
**flags** | **List[str]** | List of properties of account | [optional] 

## Example

```python
from openapi_client.models.dbv0038_account import Dbv0038Account

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038Account from a JSON string
dbv0038_account_instance = Dbv0038Account.from_json(json)
# print the JSON string representation of the object
print(Dbv0038Account.to_json())

# convert the object into a dict
dbv0038_account_dict = dbv0038_account_instance.to_dict()
# create an instance of Dbv0038Account from a dict
dbv0038_account_from_dict = Dbv0038Account.from_dict(dbv0038_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


