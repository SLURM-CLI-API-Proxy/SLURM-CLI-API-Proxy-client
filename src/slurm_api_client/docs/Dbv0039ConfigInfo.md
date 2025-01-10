# Dbv0039ConfigInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0039Meta**](Dbv0039Meta.md) |  | [optional] 
**errors** | [**List[Dbv0039Error]**](Dbv0039Error.md) | Slurm errors | [optional] 
**warnings** | [**List[Dbv0039Warning]**](Dbv0039Warning.md) | Slurm warnings | [optional] 
**tres** | [**List[V0039Tres]**](V0039Tres.md) |  | [optional] 
**accounts** | [**List[V0039Account]**](V0039Account.md) |  | [optional] 
**associations** | [**List[V0039Assoc]**](V0039Assoc.md) |  | [optional] 
**users** | [**List[V0039User]**](V0039User.md) |  | [optional] 
**qos** | [**List[V0039Qos]**](V0039Qos.md) |  | [optional] 
**wckeys** | [**List[V0039Wckey]**](V0039Wckey.md) |  | [optional] 
**clusters** | [**List[V0039ClusterRec]**](V0039ClusterRec.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0039_config_info import Dbv0039ConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0039ConfigInfo from a JSON string
dbv0039_config_info_instance = Dbv0039ConfigInfo.from_json(json)
# print the JSON string representation of the object
print(Dbv0039ConfigInfo.to_json())

# convert the object into a dict
dbv0039_config_info_dict = dbv0039_config_info_instance.to_dict()
# create an instance of Dbv0039ConfigInfo from a dict
dbv0039_config_info_from_dict = Dbv0039ConfigInfo.from_dict(dbv0039_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


