# Dbv0038Association

Association description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Assigned account | [optional] 
**cluster** | **str** | Assigned cluster | [optional] 
**default** | [**Dbv0038AssociationDefault**](Dbv0038AssociationDefault.md) |  | [optional] 
**flags** | **List[str]** | List of properties of association | [optional] 
**max** | [**Dbv0038AssociationMax**](Dbv0038AssociationMax.md) |  | [optional] 
**min** | [**Dbv0038AssociationMin**](Dbv0038AssociationMin.md) |  | [optional] 
**parent_account** | **str** | Parent account name | [optional] 
**partition** | **str** | Assigned partition | [optional] 
**priority** | **int** | Assigned priority | [optional] 
**shares_raw** | **int** | Raw fairshare shares | [optional] 
**usage** | [**Dbv0038AssociationUsage**](Dbv0038AssociationUsage.md) |  | [optional] 
**user** | **str** | Assigned user | [optional] 
**qos** | **List[str]** | Assigned QOS | [optional] 

## Example

```python
from openapi_client.models.dbv0038_association import Dbv0038Association

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038Association from a JSON string
dbv0038_association_instance = Dbv0038Association.from_json(json)
# print the JSON string representation of the object
print(Dbv0038Association.to_json())

# convert the object into a dict
dbv0038_association_dict = dbv0038_association_instance.to_dict()
# create an instance of Dbv0038Association from a dict
dbv0038_association_from_dict = Dbv0038Association.from_dict(dbv0038_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


