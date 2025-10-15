# V0042JobRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select_type** | **List[str]** |  | 
**nodes** | [**V0042JobResNodes**](V0042JobResNodes.md) |  | [optional] 
**cpus** | **int** | Number of allocated CPUs | 
**threads_per_core** | [**V0042Uint16NoValStruct**](V0042Uint16NoValStruct.md) |  | 

## Example

```python
from openapi_client.models.v0042_job_res import V0042JobRes

# TODO update the JSON string below
json = "{}"
# create an instance of V0042JobRes from a JSON string
v0042_job_res_instance = V0042JobRes.from_json(json)
# print the JSON string representation of the object
print(V0042JobRes.to_json())

# convert the object into a dict
v0042_job_res_dict = v0042_job_res_instance.to_dict()
# create an instance of V0042JobRes from a dict
v0042_job_res_from_dict = V0042JobRes.from_dict(v0042_job_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


