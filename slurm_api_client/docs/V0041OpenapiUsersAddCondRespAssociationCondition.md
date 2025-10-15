# V0041OpenapiUsersAddCondRespAssociationCondition

Filters to select associations for users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **List[str]** | CSV accounts list | [optional] 
**association** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociation**](V0041OpenapiUsersAddCondRespAssociationConditionAssociation.md) |  | [optional] 
**clusters** | **List[str]** | CSV clusters list | [optional] 
**partitions** | **List[str]** | CSV partitions list | [optional] 
**users** | **List[str]** | CSV users list | 
**wckeys** | **List[str]** | CSV WCKeys list | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_users_add_cond_resp_association_condition import V0041OpenapiUsersAddCondRespAssociationCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiUsersAddCondRespAssociationCondition from a JSON string
v0041_openapi_users_add_cond_resp_association_condition_instance = V0041OpenapiUsersAddCondRespAssociationCondition.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiUsersAddCondRespAssociationCondition.to_json())

# convert the object into a dict
v0041_openapi_users_add_cond_resp_association_condition_dict = v0041_openapi_users_add_cond_resp_association_condition_instance.to_dict()
# create an instance of V0041OpenapiUsersAddCondRespAssociationCondition from a dict
v0041_openapi_users_add_cond_resp_association_condition_from_dict = V0041OpenapiUsersAddCondRespAssociationCondition.from_dict(v0041_openapi_users_add_cond_resp_association_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


