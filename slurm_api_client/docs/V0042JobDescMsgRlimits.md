# V0042JobDescMsgRlimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**fsize** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**data** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**stack** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**core** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**rss** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**nproc** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**nofile** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**memlock** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**var_as** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_job_desc_msg_rlimits import V0042JobDescMsgRlimits

# TODO update the JSON string below
json = "{}"
# create an instance of V0042JobDescMsgRlimits from a JSON string
v0042_job_desc_msg_rlimits_instance = V0042JobDescMsgRlimits.from_json(json)
# print the JSON string representation of the object
print(V0042JobDescMsgRlimits.to_json())

# convert the object into a dict
v0042_job_desc_msg_rlimits_dict = v0042_job_desc_msg_rlimits_instance.to_dict()
# create an instance of V0042JobDescMsgRlimits from a dict
v0042_job_desc_msg_rlimits_from_dict = V0042JobDescMsgRlimits.from_dict(v0042_job_desc_msg_rlimits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


