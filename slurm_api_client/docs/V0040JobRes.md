# V0040JobRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | **str** | Node(s) allocated to the job | [optional] 
**allocated_cores** | **int** | Number of allocated cores | [optional] 
**allocated_cpus** | **int** | Number of allocated CPUs | [optional] 
**allocated_hosts** | **int** | Number of allocated hosts | [optional] 
**allocated_nodes** | **List[object]** | job node resources | [optional] 

## Example

```python
from openapi_client.models.v0040_job_res import V0040JobRes

# TODO update the JSON string below
json = "{}"
# create an instance of V0040JobRes from a JSON string
v0040_job_res_instance = V0040JobRes.from_json(json)
# print the JSON string representation of the object
print(V0040JobRes.to_json())

# convert the object into a dict
v0040_job_res_dict = v0040_job_res_instance.to_dict()
# create an instance of V0040JobRes from a dict
v0040_job_res_from_dict = V0040JobRes.from_dict(v0040_job_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


