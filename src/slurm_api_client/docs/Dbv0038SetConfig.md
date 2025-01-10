# Dbv0038SetConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[Dbv0038ClustersProperties]**](Dbv0038ClustersProperties.md) |  | [optional] 
**tres** | **List[List[Dbv0038TresListInner]]** |  | [optional] 
**accounts** | [**List[Dbv0038UpdateAccount]**](Dbv0038UpdateAccount.md) |  | [optional] 
**users** | [**List[Dbv0038User]**](Dbv0038User.md) |  | [optional] 
**qos** | [**List[Dbv0038Qos]**](Dbv0038Qos.md) |  | [optional] 
**wckeys** | [**List[Dbv0038Wckey]**](Dbv0038Wckey.md) |  | [optional] 
**associations** | [**List[Dbv0038Association]**](Dbv0038Association.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0038_set_config import Dbv0038SetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038SetConfig from a JSON string
dbv0038_set_config_instance = Dbv0038SetConfig.from_json(json)
# print the JSON string representation of the object
print(Dbv0038SetConfig.to_json())

# convert the object into a dict
dbv0038_set_config_dict = dbv0038_set_config_instance.to_dict()
# create an instance of Dbv0038SetConfig from a dict
dbv0038_set_config_from_dict = Dbv0038SetConfig.from_dict(dbv0038_set_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


