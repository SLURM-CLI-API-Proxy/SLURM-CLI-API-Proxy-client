# V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | MaxTRESMinsPerJob | [optional] 
**per** | [**V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutesPer**](V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutesPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_minutes import V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes from a JSON string
v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_minutes_instance = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_minutes_dict = v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_minutes_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes from a dict
v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_minutes_from_dict = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes.from_dict(v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_minutes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


