# Dbv0039UserInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0039Meta**](Dbv0039Meta.md) |  | [optional] 
**errors** | [**List[Dbv0039Error]**](Dbv0039Error.md) | Slurm errors | [optional] 
**warnings** | [**List[Dbv0039Warning]**](Dbv0039Warning.md) | Slurm warnings | [optional] 
**users** | [**List[V0039User]**](V0039User.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0039_user_info import Dbv0039UserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0039UserInfo from a JSON string
dbv0039_user_info_instance = Dbv0039UserInfo.from_json(json)
# print the JSON string representation of the object
print(Dbv0039UserInfo.to_json())

# convert the object into a dict
dbv0039_user_info_dict = dbv0039_user_info_instance.to_dict()
# create an instance of Dbv0039UserInfo from a dict
dbv0039_user_info_from_dict = Dbv0039UserInfo.from_dict(dbv0039_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


