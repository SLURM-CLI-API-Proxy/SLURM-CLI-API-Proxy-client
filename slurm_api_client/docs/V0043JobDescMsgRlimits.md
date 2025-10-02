# V0043JobDescMsgRlimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**fsize** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**data** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**stack** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**core** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**rss** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**nproc** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**nofile** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**memlock** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 
**var_as** | [**V0043Uint64NoValStruct**](V0043Uint64NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_job_desc_msg_rlimits import V0043JobDescMsgRlimits

# TODO update the JSON string below
json = "{}"
# create an instance of V0043JobDescMsgRlimits from a JSON string
v0043_job_desc_msg_rlimits_instance = V0043JobDescMsgRlimits.from_json(json)
# print the JSON string representation of the object
print(V0043JobDescMsgRlimits.to_json())

# convert the object into a dict
v0043_job_desc_msg_rlimits_dict = v0043_job_desc_msg_rlimits_instance.to_dict()
# create an instance of V0043JobDescMsgRlimits from a dict
v0043_job_desc_msg_rlimits_from_dict = V0043JobDescMsgRlimits.from_dict(v0043_job_desc_msg_rlimits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


