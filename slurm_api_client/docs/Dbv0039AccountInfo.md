# Dbv0039AccountInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0039Meta**](Dbv0039Meta.md) |  | [optional] 
**errors** | [**List[Dbv0039Error]**](Dbv0039Error.md) | Slurm errors | [optional] 
**warnings** | [**List[Dbv0039Warning]**](Dbv0039Warning.md) | Slurm warnings | [optional] 
**accounts** | [**List[V0039Account]**](V0039Account.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0039_account_info import Dbv0039AccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0039AccountInfo from a JSON string
dbv0039_account_info_instance = Dbv0039AccountInfo.from_json(json)
# print the JSON string representation of the object
print(Dbv0039AccountInfo.to_json())

# convert the object into a dict
dbv0039_account_info_dict = dbv0039_account_info_instance.to_dict()
# create an instance of Dbv0039AccountInfo from a dict
dbv0039_account_info_from_dict = Dbv0039AccountInfo.from_dict(dbv0039_account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


