# V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutesPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qos** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | GrpTRESRunMins | [optional] 
**job** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | MaxTRESMinsPerJob | [optional] 
**account** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | MaxTRESRunMinsPerAccount | [optional] 
**user** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | MaxTRESRunMinsPerUser | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutesPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutesPer from a JSON string
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per_instance = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutesPer.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutesPer.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per_dict = v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutesPer from a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per_from_dict = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutesPer.from_dict(v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


