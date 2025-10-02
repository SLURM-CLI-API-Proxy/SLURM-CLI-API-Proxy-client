# V0041JobDescMsgRlimitsRss

Largest resident set size, in bytes. This affects swapping; processes that are exceeding their resident set size will be more likely to have physical memory taken from them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0041_job_desc_msg_rlimits_rss import V0041JobDescMsgRlimitsRss

# TODO update the JSON string below
json = "{}"
# create an instance of V0041JobDescMsgRlimitsRss from a JSON string
v0041_job_desc_msg_rlimits_rss_instance = V0041JobDescMsgRlimitsRss.from_json(json)
# print the JSON string representation of the object
print(V0041JobDescMsgRlimitsRss.to_json())

# convert the object into a dict
v0041_job_desc_msg_rlimits_rss_dict = v0041_job_desc_msg_rlimits_rss_instance.to_dict()
# create an instance of V0041JobDescMsgRlimitsRss from a dict
v0041_job_desc_msg_rlimits_rss_from_dict = V0041JobDescMsgRlimitsRss.from_dict(v0041_job_desc_msg_rlimits_rss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


