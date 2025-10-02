# V0043JobRequired


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus** | **int** | Minimum number of CPUs required | [optional] 
**memory_per_cpu** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**memory_per_node** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_job_required import V0043JobRequired

# TODO update the JSON string below
json = "{}"
# create an instance of V0043JobRequired from a JSON string
v0043_job_required_instance = V0043JobRequired.from_json(json)
# print the JSON string representation of the object
print(V0043JobRequired.to_json())

# convert the object into a dict
v0043_job_required_dict = v0043_job_required_instance.to_dict()
# create an instance of V0043JobRequired from a dict
v0043_job_required_from_dict = V0043JobRequired.from_dict(v0043_job_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


