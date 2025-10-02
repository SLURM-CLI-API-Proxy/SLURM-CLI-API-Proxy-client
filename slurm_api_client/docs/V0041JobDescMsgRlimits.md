# V0041JobDescMsgRlimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**V0041JobDescMsgRlimitsCpu**](V0041JobDescMsgRlimitsCpu.md) |  | [optional] 
**fsize** | [**V0041JobDescMsgRlimitsFsize**](V0041JobDescMsgRlimitsFsize.md) |  | [optional] 
**data** | [**V0041JobDescMsgRlimitsData**](V0041JobDescMsgRlimitsData.md) |  | [optional] 
**stack** | [**V0041JobDescMsgRlimitsStack**](V0041JobDescMsgRlimitsStack.md) |  | [optional] 
**core** | [**V0041JobDescMsgRlimitsCore**](V0041JobDescMsgRlimitsCore.md) |  | [optional] 
**rss** | [**V0041JobDescMsgRlimitsRss**](V0041JobDescMsgRlimitsRss.md) |  | [optional] 
**nproc** | [**V0041JobDescMsgRlimitsNproc**](V0041JobDescMsgRlimitsNproc.md) |  | [optional] 
**nofile** | [**V0041JobDescMsgRlimitsNofile**](V0041JobDescMsgRlimitsNofile.md) |  | [optional] 
**memlock** | [**V0041JobDescMsgRlimitsMemlock**](V0041JobDescMsgRlimitsMemlock.md) |  | [optional] 
**var_as** | [**V0041JobDescMsgRlimitsAs**](V0041JobDescMsgRlimitsAs.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_job_desc_msg_rlimits import V0041JobDescMsgRlimits

# TODO update the JSON string below
json = "{}"
# create an instance of V0041JobDescMsgRlimits from a JSON string
v0041_job_desc_msg_rlimits_instance = V0041JobDescMsgRlimits.from_json(json)
# print the JSON string representation of the object
print(V0041JobDescMsgRlimits.to_json())

# convert the object into a dict
v0041_job_desc_msg_rlimits_dict = v0041_job_desc_msg_rlimits_instance.to_dict()
# create an instance of V0041JobDescMsgRlimits from a dict
v0041_job_desc_msg_rlimits_from_dict = V0041JobDescMsgRlimits.from_dict(v0041_job_desc_msg_rlimits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


