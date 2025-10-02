# V0040JobTimeTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** | Sum of System and User CPU time used by the job in seconds | [optional] 
**microseconds** | **int** | Sum of System and User CPU time used by the job in microseconds | [optional] 

## Example

```python
from openapi_client.models.v0040_job_time_total import V0040JobTimeTotal

# TODO update the JSON string below
json = "{}"
# create an instance of V0040JobTimeTotal from a JSON string
v0040_job_time_total_instance = V0040JobTimeTotal.from_json(json)
# print the JSON string representation of the object
print(V0040JobTimeTotal.to_json())

# convert the object into a dict
v0040_job_time_total_dict = v0040_job_time_total_instance.to_dict()
# create an instance of V0040JobTimeTotal from a dict
v0040_job_time_total_from_dict = V0040JobTimeTotal.from_dict(v0040_job_time_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


