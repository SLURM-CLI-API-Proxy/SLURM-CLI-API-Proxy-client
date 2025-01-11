# Dbv0038TresListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | TRES type | [optional] 
**name** | **str** | TRES name (optional) | [optional] 
**id** | **int** | database id | [optional] 
**count** | **int** | count of TRES | [optional] 

## Example

```python
from openapi_client.models.dbv0038_tres_list_inner import Dbv0038TresListInner

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038TresListInner from a JSON string
dbv0038_tres_list_inner_instance = Dbv0038TresListInner.from_json(json)
# print the JSON string representation of the object
print(Dbv0038TresListInner.to_json())

# convert the object into a dict
dbv0038_tres_list_inner_dict = dbv0038_tres_list_inner_instance.to_dict()
# create an instance of Dbv0038TresListInner from a dict
dbv0038_tres_list_inner_from_dict = Dbv0038TresListInner.from_dict(dbv0038_tres_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


