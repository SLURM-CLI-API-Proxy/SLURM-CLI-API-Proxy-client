# Dbv0038Wckey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **str** | Cluster name | [optional] 
**id** | **int** | wckey database unique id | [optional] 
**name** | **str** | wckey name | [optional] 
**user** | **str** | wckey user | [optional] 
**flags** | **List[str]** | List of properties of wckey | [optional] 
**accounting** | [**List[Dbv0038Accounting]**](Dbv0038Accounting.md) | List of accounting records | [optional] 

## Example

```python
from openapi_client.models.dbv0038_wckey import Dbv0038Wckey

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038Wckey from a JSON string
dbv0038_wckey_instance = Dbv0038Wckey.from_json(json)
# print the JSON string representation of the object
print(Dbv0038Wckey.to_json())

# convert the object into a dict
dbv0038_wckey_dict = dbv0038_wckey_instance.to_dict()
# create an instance of Dbv0038Wckey from a dict
dbv0038_wckey_from_dict = Dbv0038Wckey.from_dict(dbv0038_wckey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


