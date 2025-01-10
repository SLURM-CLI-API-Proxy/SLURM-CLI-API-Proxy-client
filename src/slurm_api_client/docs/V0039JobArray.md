# V0039JobArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** |  | [optional] 
**limits** | [**V0039JobArrayLimits**](V0039JobArrayLimits.md) |  | [optional] 
**task_id** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**task** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v0039_job_array import V0039JobArray

# TODO update the JSON string below
json = "{}"
# create an instance of V0039JobArray from a JSON string
v0039_job_array_instance = V0039JobArray.from_json(json)
# print the JSON string representation of the object
print(V0039JobArray.to_json())

# convert the object into a dict
v0039_job_array_dict = v0039_job_array_instance.to_dict()
# create an instance of V0039JobArray from a dict
v0039_job_array_from_dict = V0039JobArray.from_dict(v0039_job_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


