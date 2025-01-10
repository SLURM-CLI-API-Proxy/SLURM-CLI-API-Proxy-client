# V0039Wckey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting** | [**List[V0039Accounting]**](V0039Accounting.md) |  | [optional] 
**cluster** | **str** |  | 
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**user** | **str** |  | 
**flags** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.v0039_wckey import V0039Wckey

# TODO update the JSON string below
json = "{}"
# create an instance of V0039Wckey from a JSON string
v0039_wckey_instance = V0039Wckey.from_json(json)
# print the JSON string representation of the object
print(V0039Wckey.to_json())

# convert the object into a dict
v0039_wckey_dict = v0039_wckey_instance.to_dict()
# create an instance of V0039Wckey from a dict
v0039_wckey_from_dict = V0039Wckey.from_dict(v0039_wckey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


