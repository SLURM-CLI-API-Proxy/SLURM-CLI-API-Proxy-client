# V0040BfExitFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_job_queue** | **int** | Reached end of queue | [optional] 
**bf_max_job_start** | **int** | Reached number of jobs allowed to start | [optional] 
**bf_max_job_test** | **int** | Reached number of jobs allowed to be tested | [optional] 
**bf_max_time** | **int** | Reached maximum allowed scheduler time | [optional] 
**bf_node_space_size** | **int** | Reached table size limit | [optional] 
**state_changed** | **int** | System state changed | [optional] 

## Example

```python
from openapi_client.models.v0040_bf_exit_fields import V0040BfExitFields

# TODO update the JSON string below
json = "{}"
# create an instance of V0040BfExitFields from a JSON string
v0040_bf_exit_fields_instance = V0040BfExitFields.from_json(json)
# print the JSON string representation of the object
print(V0040BfExitFields.to_json())

# convert the object into a dict
v0040_bf_exit_fields_dict = v0040_bf_exit_fields_instance.to_dict()
# create an instance of V0040BfExitFields from a dict
v0040_bf_exit_fields_from_dict = V0040BfExitFields.from_dict(v0040_bf_exit_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


