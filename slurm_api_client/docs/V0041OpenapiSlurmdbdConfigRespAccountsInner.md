# V0041OpenapiSlurmdbdConfigRespAccountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associations** | [**List[V0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner]**](V0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner.md) | Associations involving this account (only populated if requested) | [optional] 
**coordinators** | [**List[V0041OpenapiSlurmdbdConfigRespAccountsInnerCoordinatorsInner]**](V0041OpenapiSlurmdbdConfigRespAccountsInnerCoordinatorsInner.md) | List of users that are a coordinator of this account (only populated if requested) | [optional] 
**description** | **str** | Arbitrary string describing the account | 
**name** | **str** | Account name | 
**organization** | **str** | Organization to which the account belongs | 
**flags** | **List[str]** | Flags associated with the account | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_accounts_inner import V0041OpenapiSlurmdbdConfigRespAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespAccountsInner from a JSON string
v0041_openapi_slurmdbd_config_resp_accounts_inner_instance = V0041OpenapiSlurmdbdConfigRespAccountsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespAccountsInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_accounts_inner_dict = v0041_openapi_slurmdbd_config_resp_accounts_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespAccountsInner from a dict
v0041_openapi_slurmdbd_config_resp_accounts_inner_from_dict = V0041OpenapiSlurmdbdConfigRespAccountsInner.from_dict(v0041_openapi_slurmdbd_config_resp_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


