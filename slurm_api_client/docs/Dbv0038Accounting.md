# Dbv0038Accounting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | **int** | total seconds allocated | [optional] 
**id** | **int** | association/wckey ID | [optional] 
**start** | **int** | UNIX timestamp when accounting period started | [optional] 
**tres** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 

## Example

```python
from openapi_client.models.dbv0038_accounting import Dbv0038Accounting

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038Accounting from a JSON string
dbv0038_accounting_instance = Dbv0038Accounting.from_json(json)
# print the JSON string representation of the object
print(Dbv0038Accounting.to_json())

# convert the object into a dict
dbv0038_accounting_dict = dbv0038_accounting_instance.to_dict()
# create an instance of Dbv0038Accounting from a dict
dbv0038_accounting_from_dict = Dbv0038Accounting.from_dict(dbv0038_accounting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


