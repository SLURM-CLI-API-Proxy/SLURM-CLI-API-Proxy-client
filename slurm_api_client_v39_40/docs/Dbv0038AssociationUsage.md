# Dbv0038AssociationUsage

Association usage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrue_job_count** | **int** | Jobs accuring priority | [optional] 
**group_used_wallclock** | **float** | Group used wallclock time (s) | [optional] 
**fairshare_factor** | **float** | Fairshare factor | [optional] 
**fairshare_shares** | **int** | Fairshare shares | [optional] 
**normalized_priority** | **int** | Currently active jobs | [optional] 
**normalized_shares** | **float** | Normalized shares | [optional] 
**effective_normalized_usage** | **float** | Effective normalized usage | [optional] 
**raw_usage** | **int** | Raw usage | [optional] 
**job_count** | **int** | Total jobs submitted | [optional] 
**fairshare_level** | **float** | Fairshare level | [optional] 

## Example

```python
from openapi_client.models.dbv0038_association_usage import Dbv0038AssociationUsage

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038AssociationUsage from a JSON string
dbv0038_association_usage_instance = Dbv0038AssociationUsage.from_json(json)
# print the JSON string representation of the object
print(Dbv0038AssociationUsage.to_json())

# convert the object into a dict
dbv0038_association_usage_dict = dbv0038_association_usage_instance.to_dict()
# create an instance of Dbv0038AssociationUsage from a dict
dbv0038_association_usage_from_dict = Dbv0038AssociationUsage.from_dict(dbv0038_association_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


