# Dbv0038QosInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0038Meta**](Dbv0038Meta.md) |  | [optional] 
**errors** | [**List[Dbv0038Error]**](Dbv0038Error.md) | Slurm errors | [optional] 
**qos** | [**List[Dbv0038Qos]**](Dbv0038Qos.md) | Array of QOS | [optional] 

## Example

```python
from openapi_client.models.dbv0038_qos_info import Dbv0038QosInfo

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038QosInfo from a JSON string
dbv0038_qos_info_instance = Dbv0038QosInfo.from_json(json)
# print the JSON string representation of the object
print(Dbv0038QosInfo.to_json())

# convert the object into a dict
dbv0038_qos_info_dict = dbv0038_qos_info_instance.to_dict()
# create an instance of Dbv0038QosInfo from a dict
dbv0038_qos_info_from_dict = Dbv0038QosInfo.from_dict(dbv0038_qos_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


