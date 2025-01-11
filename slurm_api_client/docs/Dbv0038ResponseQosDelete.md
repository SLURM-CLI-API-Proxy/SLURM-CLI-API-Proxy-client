# Dbv0038ResponseQosDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0038Meta**](Dbv0038Meta.md) |  | [optional] 
**errors** | [**List[Dbv0038Error]**](Dbv0038Error.md) | Slurm errors | [optional] 

## Example

```python
from openapi_client.models.dbv0038_response_qos_delete import Dbv0038ResponseQosDelete

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038ResponseQosDelete from a JSON string
dbv0038_response_qos_delete_instance = Dbv0038ResponseQosDelete.from_json(json)
# print the JSON string representation of the object
print(Dbv0038ResponseQosDelete.to_json())

# convert the object into a dict
dbv0038_response_qos_delete_dict = dbv0038_response_qos_delete_instance.to_dict()
# create an instance of Dbv0038ResponseQosDelete from a dict
dbv0038_response_qos_delete_from_dict = Dbv0038ResponseQosDelete.from_dict(dbv0038_response_qos_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


