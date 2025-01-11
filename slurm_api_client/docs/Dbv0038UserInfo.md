# Dbv0038UserInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0038Meta**](Dbv0038Meta.md) |  | [optional] 
**errors** | [**List[Dbv0038Error]**](Dbv0038Error.md) | Slurm errors | [optional] 
**users** | [**List[Dbv0038User]**](Dbv0038User.md) | Array of users | [optional] 

## Example

```python
from openapi_client.models.dbv0038_user_info import Dbv0038UserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038UserInfo from a JSON string
dbv0038_user_info_instance = Dbv0038UserInfo.from_json(json)
# print the JSON string representation of the object
print(Dbv0038UserInfo.to_json())

# convert the object into a dict
dbv0038_user_info_dict = dbv0038_user_info_instance.to_dict()
# create an instance of Dbv0038UserInfo from a dict
dbv0038_user_info_from_dict = Dbv0038UserInfo.from_dict(dbv0038_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


