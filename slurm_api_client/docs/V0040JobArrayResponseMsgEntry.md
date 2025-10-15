# V0040JobArrayResponseMsgEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | Job ID for updated Job | [optional] 
**step_id** | **str** | Step ID for updated Job | [optional] 
**error** | **str** | Verbose update status or error | [optional] 
**error_code** | **int** | Verbose update status or error | [optional] 
**why** | **str** | Update response message | [optional] 

## Example

```python
from openapi_client.models.v0040_job_array_response_msg_entry import V0040JobArrayResponseMsgEntry

# TODO update the JSON string below
json = "{}"
# create an instance of V0040JobArrayResponseMsgEntry from a JSON string
v0040_job_array_response_msg_entry_instance = V0040JobArrayResponseMsgEntry.from_json(json)
# print the JSON string representation of the object
print(V0040JobArrayResponseMsgEntry.to_json())

# convert the object into a dict
v0040_job_array_response_msg_entry_dict = v0040_job_array_response_msg_entry_instance.to_dict()
# create an instance of V0040JobArrayResponseMsgEntry from a dict
v0040_job_array_response_msg_entry_from_dict = V0040JobArrayResponseMsgEntry.from_dict(v0040_job_array_response_msg_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


