# V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobsPerUser

MaxJobsPerUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_user import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobsPerUser

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobsPerUser from a JSON string
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_user_instance = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobsPerUser.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobsPerUser.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_user_dict = v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_user_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobsPerUser from a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_user_from_dict = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobsPerUser.from_dict(v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


