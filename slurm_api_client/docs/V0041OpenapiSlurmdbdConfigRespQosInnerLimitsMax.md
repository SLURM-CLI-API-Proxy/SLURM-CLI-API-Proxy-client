# V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMax


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_jobs** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobs**](V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobs.md) |  | [optional] 
**tres** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTres**](V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTres.md) |  | [optional] 
**wall_clock** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClock**](V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClock.md) |  | [optional] 
**jobs** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobs**](V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobs.md) |  | [optional] 
**accruing** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing**](V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMax

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMax from a JSON string
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_instance = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMax.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMax.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_dict = v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMax from a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_from_dict = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMax.from_dict(v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


