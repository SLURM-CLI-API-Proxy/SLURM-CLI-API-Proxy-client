# V0039CronEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | **List[str]** |  | [optional] 
**minute** | **str** |  | [optional] 
**hour** | **str** |  | [optional] 
**day_of_month** | **str** |  | [optional] 
**month** | **str** |  | [optional] 
**day_of_week** | **str** |  | [optional] 
**specification** | **str** |  | [optional] 
**command** | **str** |  | [optional] 
**line** | [**V0039CronEntryLine**](V0039CronEntryLine.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_cron_entry import V0039CronEntry

# TODO update the JSON string below
json = "{}"
# create an instance of V0039CronEntry from a JSON string
v0039_cron_entry_instance = V0039CronEntry.from_json(json)
# print the JSON string representation of the object
print(V0039CronEntry.to_json())

# convert the object into a dict
v0039_cron_entry_dict = v0039_cron_entry_instance.to_dict()
# create an instance of V0039CronEntry from a dict
v0039_cron_entry_from_dict = V0039CronEntry.from_dict(v0039_cron_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


