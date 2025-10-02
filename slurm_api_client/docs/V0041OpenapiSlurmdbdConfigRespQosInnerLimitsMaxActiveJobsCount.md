# V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsCount

GrpJobs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsCount

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsCount from a JSON string
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count_instance = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsCount.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsCount.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count_dict = v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsCount from a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count_from_dict = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsCount.from_dict(v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


