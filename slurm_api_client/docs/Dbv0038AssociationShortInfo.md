# Dbv0038AssociationShortInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account name | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**partition** | **str** | Partition name (optional) | [optional] 
**user** | **str** | User name | [optional] 

## Example

```python
from openapi_client.models.dbv0038_association_short_info import Dbv0038AssociationShortInfo

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038AssociationShortInfo from a JSON string
dbv0038_association_short_info_instance = Dbv0038AssociationShortInfo.from_json(json)
# print the JSON string representation of the object
print(Dbv0038AssociationShortInfo.to_json())

# convert the object into a dict
dbv0038_association_short_info_dict = dbv0038_association_short_info_instance.to_dict()
# create an instance of Dbv0038AssociationShortInfo from a dict
dbv0038_association_short_info_from_dict = Dbv0038AssociationShortInfo.from_dict(dbv0038_association_short_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


