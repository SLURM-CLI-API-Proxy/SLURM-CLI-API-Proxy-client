# Dbv0038JobTres

TRES settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 
**requested** | [**List[Dbv0038TresListInner]**](Dbv0038TresListInner.md) | TRES list of attributes | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_tres import Dbv0038JobTres

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobTres from a JSON string
dbv0038_job_tres_instance = Dbv0038JobTres.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobTres.to_json())

# convert the object into a dict
dbv0038_job_tres_dict = dbv0038_job_tres_instance.to_dict()
# create an instance of Dbv0038JobTres from a dict
dbv0038_job_tres_from_dict = Dbv0038JobTres.from_dict(dbv0038_job_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


