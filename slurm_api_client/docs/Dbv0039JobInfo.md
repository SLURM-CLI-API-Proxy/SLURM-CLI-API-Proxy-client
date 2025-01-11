# Dbv0039JobInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Dbv0039Meta**](Dbv0039Meta.md) |  | [optional] 
**errors** | [**List[Dbv0039Error]**](Dbv0039Error.md) | Slurm errors | [optional] 
**warnings** | [**List[Dbv0039Warning]**](Dbv0039Warning.md) | Slurm warnings | [optional] 
**jobs** | [**List[V0039Job]**](V0039Job.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbv0039_job_info import Dbv0039JobInfo

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0039JobInfo from a JSON string
dbv0039_job_info_instance = Dbv0039JobInfo.from_json(json)
# print the JSON string representation of the object
print(Dbv0039JobInfo.to_json())

# convert the object into a dict
dbv0039_job_info_dict = dbv0039_job_info_instance.to_dict()
# create an instance of Dbv0039JobInfo from a dict
dbv0039_job_info_from_dict = Dbv0039JobInfo.from_dict(dbv0039_job_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


