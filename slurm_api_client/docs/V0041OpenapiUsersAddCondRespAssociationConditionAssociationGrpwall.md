# V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpwall

Maximum wall clock time in minutes able to be allocated by running jobs in this association and its children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_users_add_cond_resp_association_condition_association_grpwall import V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpwall

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpwall from a JSON string
v0041_openapi_users_add_cond_resp_association_condition_association_grpwall_instance = V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpwall.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpwall.to_json())

# convert the object into a dict
v0041_openapi_users_add_cond_resp_association_condition_association_grpwall_dict = v0041_openapi_users_add_cond_resp_association_condition_association_grpwall_instance.to_dict()
# create an instance of V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpwall from a dict
v0041_openapi_users_add_cond_resp_association_condition_association_grpwall_from_dict = V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpwall.from_dict(v0041_openapi_users_add_cond_resp_association_condition_association_grpwall_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


