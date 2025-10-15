# V0040Wckey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting** | [**List[V0040Accounting]**](V0040Accounting.md) |  | [optional] 
**cluster** | **str** | Cluster name | 
**id** | **int** | Unique ID for this user-cluster-wckey combination | [optional] 
**name** | **str** | WCKey name | 
**user** | **str** | User name | 
**flags** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.v0040_wckey import V0040Wckey

# TODO update the JSON string below
json = "{}"
# create an instance of V0040Wckey from a JSON string
v0040_wckey_instance = V0040Wckey.from_json(json)
# print the JSON string representation of the object
print(V0040Wckey.to_json())

# convert the object into a dict
v0040_wckey_dict = v0040_wckey_instance.to_dict()
# create an instance of V0040Wckey from a dict
v0040_wckey_from_dict = V0040Wckey.from_dict(v0040_wckey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


