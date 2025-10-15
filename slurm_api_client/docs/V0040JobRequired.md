# V0040JobRequired


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus** | **int** | Minimum number of CPUs required | [optional] 
**memory_per_cpu** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**memory_per_node** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_job_required import V0040JobRequired

# TODO update the JSON string below
json = "{}"
# create an instance of V0040JobRequired from a JSON string
v0040_job_required_instance = V0040JobRequired.from_json(json)
# print the JSON string representation of the object
print(V0040JobRequired.to_json())

# convert the object into a dict
v0040_job_required_dict = v0040_job_required_instance.to_dict()
# create an instance of V0040JobRequired from a dict
v0040_job_required_from_dict = V0040JobRequired.from_dict(v0040_job_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


