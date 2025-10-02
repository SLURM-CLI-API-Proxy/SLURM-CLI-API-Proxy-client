# V0041OpenapiSlurmdbdConfigRespQosInnerLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grace_time** | **int** | GraceTime | [optional] 
**max** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMax**](V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMax.md) |  | [optional] 
**factor** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor**](V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor.md) |  | [optional] 
**min** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMin**](V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMin.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits import V0041OpenapiSlurmdbdConfigRespQosInnerLimits

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimits from a JSON string
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_instance = V0041OpenapiSlurmdbdConfigRespQosInnerLimits.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespQosInnerLimits.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_dict = v0041_openapi_slurmdbd_config_resp_qos_inner_limits_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimits from a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_from_dict = V0041OpenapiSlurmdbdConfigRespQosInnerLimits.from_dict(v0041_openapi_slurmdbd_config_resp_qos_inner_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


