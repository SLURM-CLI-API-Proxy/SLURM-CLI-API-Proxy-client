# V0043OpenapiSlurmdbdStatsResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statistics** | [**V0043StatsRec**](V0043StatsRec.md) |  | 
**meta** | [**V0043OpenapiMeta**](V0043OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0043OpenapiError]**](V0043OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0043OpenapiWarning]**](V0043OpenapiWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_openapi_slurmdbd_stats_resp import V0043OpenapiSlurmdbdStatsResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0043OpenapiSlurmdbdStatsResp from a JSON string
v0043_openapi_slurmdbd_stats_resp_instance = V0043OpenapiSlurmdbdStatsResp.from_json(json)
# print the JSON string representation of the object
print(V0043OpenapiSlurmdbdStatsResp.to_json())

# convert the object into a dict
v0043_openapi_slurmdbd_stats_resp_dict = v0043_openapi_slurmdbd_stats_resp_instance.to_dict()
# create an instance of V0043OpenapiSlurmdbdStatsResp from a dict
v0043_openapi_slurmdbd_stats_resp_from_dict = V0043OpenapiSlurmdbdStatsResp.from_dict(v0043_openapi_slurmdbd_stats_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


