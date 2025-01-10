# Dbv0039ResponseAssociationsDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0039Meta**](Dbv0039Meta.md) |  | [optional] 
**errors** | [**List[Dbv0039Error]**](Dbv0039Error.md) | Slurm errors | [optional] 
**warnings** | [**List[Dbv0039Warning]**](Dbv0039Warning.md) | Slurm warnings | [optional] 
**removed_associations** | **List[str]** | the associations | [optional] 

## Example

```python
from openapi_client.models.dbv0039_response_associations_delete import Dbv0039ResponseAssociationsDelete

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0039ResponseAssociationsDelete from a JSON string
dbv0039_response_associations_delete_instance = Dbv0039ResponseAssociationsDelete.from_json(json)
# print the JSON string representation of the object
print(Dbv0039ResponseAssociationsDelete.to_json())

# convert the object into a dict
dbv0039_response_associations_delete_dict = dbv0039_response_associations_delete_instance.to_dict()
# create an instance of Dbv0039ResponseAssociationsDelete from a dict
dbv0039_response_associations_delete_from_dict = Dbv0039ResponseAssociationsDelete.from_dict(dbv0039_response_associations_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


