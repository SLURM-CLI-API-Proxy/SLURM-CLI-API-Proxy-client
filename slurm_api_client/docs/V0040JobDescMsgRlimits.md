# V0040JobDescMsgRlimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**fsize** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**data** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**stack** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**core** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**rss** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**nproc** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**nofile** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**memlock** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**var_as** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_job_desc_msg_rlimits import V0040JobDescMsgRlimits

# TODO update the JSON string below
json = "{}"
# create an instance of V0040JobDescMsgRlimits from a JSON string
v0040_job_desc_msg_rlimits_instance = V0040JobDescMsgRlimits.from_json(json)
# print the JSON string representation of the object
print(V0040JobDescMsgRlimits.to_json())

# convert the object into a dict
v0040_job_desc_msg_rlimits_dict = v0040_job_desc_msg_rlimits_instance.to_dict()
# create an instance of V0040JobDescMsgRlimits from a dict
v0040_job_desc_msg_rlimits_from_dict = V0040JobDescMsgRlimits.from_dict(v0040_job_desc_msg_rlimits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


