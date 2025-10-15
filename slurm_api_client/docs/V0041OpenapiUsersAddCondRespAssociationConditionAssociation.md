# V0041OpenapiUsersAddCondRespAssociationConditionAssociation

Association limits and options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Arbitrary comment | [optional] 
**defaultqos** | **str** | Default QOS | [optional] 
**grpjobs** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpjobs**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpjobs.md) |  | [optional] 
**grpjobsaccrue** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpjobsaccrue**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpjobsaccrue.md) |  | [optional] 
**grpsubmitjobs** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs.md) |  | [optional] 
**grptres** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Maximum number of TRES able to be allocated by running jobs in this association and its children | [optional] 
**grptresmins** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Total number of TRES minutes that can possibly be used by past, present and future jobs in this association and its children | [optional] 
**grptresrunmins** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Maximum number of TRES minutes able to be allocated by running jobs in this association and its children | [optional] 
**grpwall** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpwall**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpwall.md) |  | [optional] 
**maxjobs** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobs**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobs.md) |  | [optional] 
**maxjobsaccrue** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobsaccrue**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobsaccrue.md) |  | [optional] 
**maxsubmitjobs** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxsubmitjobs**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxsubmitjobs.md) |  | [optional] 
**maxtresminsperjob** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Maximum number of TRES minutes each job is able to use in this association | [optional] 
**maxtresrunmins** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Maximum number of TRES minutes able to be allocated by running jobs in this association | [optional] 
**maxtresperjob** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Maximum number of TRES each job is able to use in this association | [optional] 
**maxtrespernode** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Maximum number of TRES each node is able to use | [optional] 
**maxwalldurationperjob** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxwalldurationperjob**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxwalldurationperjob.md) |  | [optional] 
**minpriothresh** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationMinpriothresh**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationMinpriothresh.md) |  | [optional] 
**parent** | **str** | Name of parent account | [optional] 
**priority** | [**V0041OpenapiSlurmdbdConfigRespAssociationsInnerPriority**](V0041OpenapiSlurmdbdConfigRespAssociationsInnerPriority.md) |  | [optional] 
**qoslevel** | **List[str]** | List of available QOS names | [optional] 
**fairshare** | **int** | Allocated shares used for fairshare calculation | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_users_add_cond_resp_association_condition_association import V0041OpenapiUsersAddCondRespAssociationConditionAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiUsersAddCondRespAssociationConditionAssociation from a JSON string
v0041_openapi_users_add_cond_resp_association_condition_association_instance = V0041OpenapiUsersAddCondRespAssociationConditionAssociation.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiUsersAddCondRespAssociationConditionAssociation.to_json())

# convert the object into a dict
v0041_openapi_users_add_cond_resp_association_condition_association_dict = v0041_openapi_users_add_cond_resp_association_condition_association_instance.to_dict()
# create an instance of V0041OpenapiUsersAddCondRespAssociationConditionAssociation from a dict
v0041_openapi_users_add_cond_resp_association_condition_association_from_dict = V0041OpenapiUsersAddCondRespAssociationConditionAssociation.from_dict(v0041_openapi_users_add_cond_resp_association_condition_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


