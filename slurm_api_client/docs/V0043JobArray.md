# V0043JobArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | Job ID of job array, or 0 if N/A | [optional] 
**limits** | [**V0040JobArrayLimits**](V0040JobArrayLimits.md) |  | [optional] 
**task_id** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**task** | **str** | String expression of task IDs in this record | [optional] 

## Example

```python
from openapi_client.models.v0043_job_array import V0043JobArray

# TODO update the JSON string below
json = "{}"
# create an instance of V0043JobArray from a JSON string
v0043_job_array_instance = V0043JobArray.from_json(json)
# print the JSON string representation of the object
print(V0043JobArray.to_json())

# convert the object into a dict
v0043_job_array_dict = v0043_job_array_instance.to_dict()
# create an instance of V0043JobArray from a dict
v0043_job_array_from_dict = V0043JobArray.from_dict(v0043_job_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


