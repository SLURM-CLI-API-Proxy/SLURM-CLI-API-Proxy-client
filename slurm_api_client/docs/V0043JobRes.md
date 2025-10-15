# V0043JobRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select_type** | **List[str]** | Scheduler consumable resource selection type | 
**nodes** | [**V0043JobResNodes**](V0043JobResNodes.md) |  | [optional] 
**cpus** | **int** | Number of allocated CPUs | 
**threads_per_core** | [**V0043Uint16NoValStruct**](V0043Uint16NoValStruct.md) |  | 

## Example

```python
from openapi_client.models.v0043_job_res import V0043JobRes

# TODO update the JSON string below
json = "{}"
# create an instance of V0043JobRes from a JSON string
v0043_job_res_instance = V0043JobRes.from_json(json)
# print the JSON string representation of the object
print(V0043JobRes.to_json())

# convert the object into a dict
v0043_job_res_dict = v0043_job_res_instance.to_dict()
# create an instance of V0043JobRes from a dict
v0043_job_res_from_dict = V0043JobRes.from_dict(v0043_job_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


