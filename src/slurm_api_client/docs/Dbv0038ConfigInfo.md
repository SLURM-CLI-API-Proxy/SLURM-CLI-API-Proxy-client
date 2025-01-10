# Dbv0038ConfigInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0038Meta**](Dbv0038Meta.md) |  | [optional] 
**errors** | [**List[Dbv0038Error]**](Dbv0038Error.md) | Slurm errors | [optional] 
**tres** | **List[List[Dbv0038TresListInner]]** | Array of TRES | [optional] 
**accounts** | [**List[Dbv0038Account]**](Dbv0038Account.md) | Array of accounts | [optional] 
**associations** | [**List[Dbv0038Association]**](Dbv0038Association.md) | Array of associations | [optional] 
**users** | [**List[Dbv0038User]**](Dbv0038User.md) | Array of users | [optional] 
**qos** | [**List[Dbv0038Qos]**](Dbv0038Qos.md) | Array of qos | [optional] 
**wckeys** | [**List[Dbv0038Wckey]**](Dbv0038Wckey.md) | Array of wckeys | [optional] 

## Example

```python
from openapi_client.models.dbv0038_config_info import Dbv0038ConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038ConfigInfo from a JSON string
dbv0038_config_info_instance = Dbv0038ConfigInfo.from_json(json)
# print the JSON string representation of the object
print(Dbv0038ConfigInfo.to_json())

# convert the object into a dict
dbv0038_config_info_dict = dbv0038_config_info_instance.to_dict()
# create an instance of Dbv0038ConfigInfo from a dict
dbv0038_config_info_from_dict = Dbv0038ConfigInfo.from_dict(dbv0038_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


