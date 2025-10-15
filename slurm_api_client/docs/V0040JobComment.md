# V0040JobComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator** | **str** | Arbitrary comment made by administrator | [optional] 
**job** | **str** | Arbitrary comment made by user | [optional] 
**system** | **str** | Arbitrary comment from slurmctld | [optional] 

## Example

```python
from openapi_client.models.v0040_job_comment import V0040JobComment

# TODO update the JSON string below
json = "{}"
# create an instance of V0040JobComment from a JSON string
v0040_job_comment_instance = V0040JobComment.from_json(json)
# print the JSON string representation of the object
print(V0040JobComment.to_json())

# convert the object into a dict
v0040_job_comment_dict = v0040_job_comment_instance.to_dict()
# create an instance of V0040JobComment from a dict
v0040_job_comment_from_dict = V0040JobComment.from_dict(v0040_job_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


