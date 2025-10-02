# Dbv0038WckeyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0038Meta**](Dbv0038Meta.md) |  | [optional] 
**errors** | [**List[Dbv0038Error]**](Dbv0038Error.md) | Slurm errors | [optional] 
**wckeys** | [**List[Dbv0038Wckey]**](Dbv0038Wckey.md) | List of wckeys | [optional] 

## Example

```python
from openapi_client.models.dbv0038_wckey_info import Dbv0038WckeyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038WckeyInfo from a JSON string
dbv0038_wckey_info_instance = Dbv0038WckeyInfo.from_json(json)
# print the JSON string representation of the object
print(Dbv0038WckeyInfo.to_json())

# convert the object into a dict
dbv0038_wckey_info_dict = dbv0038_wckey_info_instance.to_dict()
# create an instance of Dbv0038WckeyInfo from a dict
dbv0038_wckey_info_from_dict = Dbv0038WckeyInfo.from_dict(dbv0038_wckey_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


