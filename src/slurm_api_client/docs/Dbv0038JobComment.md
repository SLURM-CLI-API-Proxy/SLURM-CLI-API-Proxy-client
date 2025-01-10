# Dbv0038JobComment

Job comments by type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator** | **str** | Administrator set comment | [optional] 
**job** | **str** | Job comment | [optional] 
**system** | **str** | System set comment | [optional] 

## Example

```python
from openapi_client.models.dbv0038_job_comment import Dbv0038JobComment

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038JobComment from a JSON string
dbv0038_job_comment_instance = Dbv0038JobComment.from_json(json)
# print the JSON string representation of the object
print(Dbv0038JobComment.to_json())

# convert the object into a dict
dbv0038_job_comment_dict = dbv0038_job_comment_instance.to_dict()
# create an instance of Dbv0038JobComment from a dict
dbv0038_job_comment_from_dict = Dbv0038JobComment.from_dict(dbv0038_job_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


