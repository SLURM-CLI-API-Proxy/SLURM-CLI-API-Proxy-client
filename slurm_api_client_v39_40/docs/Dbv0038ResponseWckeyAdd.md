# Dbv0038ResponseWckeyAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0038Meta**](Dbv0038Meta.md) |  | [optional] 
**errors** | [**List[Dbv0038Error]**](Dbv0038Error.md) | Slurm errors | [optional] 

## Example

```python
from openapi_client.models.dbv0038_response_wckey_add import Dbv0038ResponseWckeyAdd

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038ResponseWckeyAdd from a JSON string
dbv0038_response_wckey_add_instance = Dbv0038ResponseWckeyAdd.from_json(json)
# print the JSON string representation of the object
print(Dbv0038ResponseWckeyAdd.to_json())

# convert the object into a dict
dbv0038_response_wckey_add_dict = dbv0038_response_wckey_add_instance.to_dict()
# create an instance of Dbv0038ResponseWckeyAdd from a dict
dbv0038_response_wckey_add_from_dict = Dbv0038ResponseWckeyAdd.from_dict(dbv0038_response_wckey_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


