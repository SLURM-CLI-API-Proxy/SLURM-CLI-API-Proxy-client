# V0039JobRequired


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus** | **int** |  | [optional] 
**memory_per_cpu** | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) |  | [optional] 
**memory_per_node** | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) |  | [optional] 
**memory** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.v0039_job_required import V0039JobRequired

# TODO update the JSON string below
json = "{}"
# create an instance of V0039JobRequired from a JSON string
v0039_job_required_instance = V0039JobRequired.from_json(json)
# print the JSON string representation of the object
print(V0039JobRequired.to_json())

# convert the object into a dict
v0039_job_required_dict = v0039_job_required_instance.to_dict()
# create an instance of V0039JobRequired from a dict
v0039_job_required_from_dict = V0039JobRequired.from_dict(v0039_job_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


