# Dbv0038JobTimeTotal

System time values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** | Total number of CPU-seconds used by the job, in seconds | [optional] 
**microseconds** | **int** | Total number of CPU-seconds used by the job, in microseconds | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_time_total import Dbv0038JobTimeTotal

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobTimeTotal from a JSON string
dbv0038_job_time_total_instance = Dbv0038JobTimeTotal.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobTimeTotal.to_json())

# convert the object into a dict
dbv0038_job_time_total_dict = dbv0038_job_time_total_instance.to_dict()
# create an instance of Dbv0038JobTimeTotal from a dict
dbv0038_job_time_total_from_dict = Dbv0038JobTimeTotal.from_dict(dbv0038_job_time_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


