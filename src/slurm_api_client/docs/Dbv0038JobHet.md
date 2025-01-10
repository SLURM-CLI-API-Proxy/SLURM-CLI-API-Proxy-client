# Dbv0038JobHet

Heterogeneous Job details (optional)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | Parent HetJob id | [optional] 
**job_offset** | **int** | Offset of this job to parent | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_het import Dbv0038JobHet

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobHet from a JSON string
dbv0038_job_het_instance = Dbv0038JobHet.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobHet.to_json())

# convert the object into a dict
dbv0038_job_het_dict = dbv0038_job_het_instance.to_dict()
# create an instance of Dbv0038JobHet from a dict
dbv0038_job_het_from_dict = Dbv0038JobHet.from_dict(dbv0038_job_het_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


