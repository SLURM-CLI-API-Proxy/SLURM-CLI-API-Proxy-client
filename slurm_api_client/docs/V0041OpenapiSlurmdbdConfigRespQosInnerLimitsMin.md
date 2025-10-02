# V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority_threshold** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinPriorityThreshold**](V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinPriorityThreshold.md) |  | [optional] 
**tres** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTres**](V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_min import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMin

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMin from a JSON string
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_min_instance = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMin.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMin.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_min_dict = v0041_openapi_slurmdbd_config_resp_qos_inner_limits_min_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMin from a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_min_from_dict = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMin.from_dict(v0041_openapi_slurmdbd_config_resp_qos_inner_limits_min_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


