# V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | GrpTRES | [optional] 
**group** | [**V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup**](V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresGroup.md) |  | [optional] 
**minutes** | [**V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes**](V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes.md) |  | [optional] 
**per** | [**V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresPer**](V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres import V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres from a JSON string
v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_instance = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_dict = v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres from a dict
v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_from_dict = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTres.from_dict(v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


