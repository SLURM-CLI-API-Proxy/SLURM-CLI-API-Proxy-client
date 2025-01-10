# Dbv0039SetConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[V0039ClusterRec]**](V0039ClusterRec.md) |  | [optional] 
**tres** | **List[List[V0039Tres]]** |  | [optional] 
**accounts** | [**List[V0039Account]**](V0039Account.md) |  | [optional] 
**users** | [**List[V0039User]**](V0039User.md) |  | [optional] 
**qos** | [**List[V0039Qos]**](V0039Qos.md) |  | [optional] 
**wckeys** | [**List[V0039Wckey]**](V0039Wckey.md) |  | [optional] 
**associations** | [**List[V0039Assoc]**](V0039Assoc.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0039_set_config import Dbv0039SetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0039SetConfig from a JSON string
dbv0039_set_config_instance = Dbv0039SetConfig.from_json(json)
# print the JSON string representation of the object
print(Dbv0039SetConfig.to_json())

# convert the object into a dict
dbv0039_set_config_dict = dbv0039_set_config_instance.to_dict()
# create an instance of Dbv0039SetConfig from a dict
dbv0039_set_config_from_dict = Dbv0039SetConfig.from_dict(dbv0039_set_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


