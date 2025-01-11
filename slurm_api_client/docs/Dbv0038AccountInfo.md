# Dbv0038AccountInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0038Meta**](Dbv0038Meta.md) |  | [optional] 
**errors** | [**List[Dbv0038Error]**](Dbv0038Error.md) | Slurm errors | [optional] 
**accounts** | [**List[Dbv0038Account]**](Dbv0038Account.md) | List of accounts | [optional] 

## Example

```python
from openapi_client.models.dbv0038_account_info import Dbv0038AccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038AccountInfo from a JSON string
dbv0038_account_info_instance = Dbv0038AccountInfo.from_json(json)
# print the JSON string representation of the object
print(Dbv0038AccountInfo.to_json())

# convert the object into a dict
dbv0038_account_info_dict = dbv0038_account_info_instance.to_dict()
# create an instance of Dbv0038AccountInfo from a dict
dbv0038_account_info_from_dict = Dbv0038AccountInfo.from_dict(dbv0038_account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


