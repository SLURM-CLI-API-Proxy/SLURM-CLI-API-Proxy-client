# Dbv0039Meta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin** | [**Dbv0038MetaPlugin**](Dbv0038MetaPlugin.md) |  | [optional] 
**slurm** | [**Dbv0039MetaSlurm**](Dbv0039MetaSlurm.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0039_meta import Dbv0039Meta

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0039Meta from a JSON string
dbv0039_meta_instance = Dbv0039Meta.from_json(json)
# print the JSON string representation of the object
print(Dbv0039Meta.to_json())

# convert the object into a dict
dbv0039_meta_dict = dbv0039_meta_instance.to_dict()
# create an instance of Dbv0039Meta from a dict
dbv0039_meta_from_dict = Dbv0039Meta.from_dict(dbv0039_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


