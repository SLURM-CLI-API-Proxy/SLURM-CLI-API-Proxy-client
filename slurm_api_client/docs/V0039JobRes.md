# V0039JobRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | **str** |  | [optional] 
**allocated_cores** | **int** |  | [optional] 
**allocated_cpus** | **int** |  | [optional] 
**allocated_hosts** | **int** |  | [optional] 
**allocated_nodes** | **List[object]** | job node resources | [optional] 

## Example

```python
from openapi_client.models.v0039_job_res import V0039JobRes

# TODO update the JSON string below
json = "{}"
# create an instance of V0039JobRes from a JSON string
v0039_job_res_instance = V0039JobRes.from_json(json)
# print the JSON string representation of the object
print(V0039JobRes.to_json())

# convert the object into a dict
v0039_job_res_dict = v0039_job_res_instance.to_dict()
# create an instance of V0039JobRes from a dict
v0039_job_res_from_dict = V0039JobRes.from_dict(v0039_job_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


