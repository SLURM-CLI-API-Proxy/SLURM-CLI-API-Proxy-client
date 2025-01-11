# V0039JobArrayResponseMsgInner

ArrayJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | JobId | [optional] 
**error_code** | **int** | numeric error code | [optional] 
**error** | **str** | error code description | [optional] 
**why** | **str** | error message | [optional] 

## Example

```python
from openapi_client.models.v0039_job_array_response_msg_inner import V0039JobArrayResponseMsgInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0039JobArrayResponseMsgInner from a JSON string
v0039_job_array_response_msg_inner_instance = V0039JobArrayResponseMsgInner.from_json(json)
# print the JSON string representation of the object
print(V0039JobArrayResponseMsgInner.to_json())

# convert the object into a dict
v0039_job_array_response_msg_inner_dict = v0039_job_array_response_msg_inner_instance.to_dict()
# create an instance of V0039JobArrayResponseMsgInner from a dict
v0039_job_array_response_msg_inner_from_dict = V0039JobArrayResponseMsgInner.from_dict(v0039_job_array_response_msg_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


