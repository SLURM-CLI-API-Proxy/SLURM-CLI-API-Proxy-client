# Dbv0038User

User description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator_level** | **str** | Description of administrator level | [optional] 
**associations** | [**List[Dbv0038AssociationShortInfo]**](Dbv0038AssociationShortInfo.md) | Assigned associations | [optional] 
**coordinators** | [**List[Dbv0038CoordinatorInfo]**](Dbv0038CoordinatorInfo.md) | List of assigned coordinators | [optional] 
**default** | [**Dbv0038UserDefault**](Dbv0038UserDefault.md) |  | [optional] 
**flags** | **List[str]** | List of properties of user | [optional] 
**name** | **str** | User name | [optional] 

## Example

```python
from openapi_client.models.dbv0038_user import Dbv0038User

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038User from a JSON string
dbv0038_user_instance = Dbv0038User.from_json(json)
# print the JSON string representation of the object
print(Dbv0038User.to_json())

# convert the object into a dict
dbv0038_user_dict = dbv0038_user_instance.to_dict()
# create an instance of Dbv0038User from a dict
dbv0038_user_from_dict = Dbv0038User.from_dict(dbv0038_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


