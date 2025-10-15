# V0043Wckey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting** | [**List[V0043Accounting]**](V0043Accounting.md) |  | [optional] 
**cluster** | **str** | Cluster name | 
**id** | **int** | Unique ID for this user-cluster-wckey combination | [optional] 
**name** | **str** | WCKey name | 
**user** | **str** | User name | 
**flags** | **List[str]** | Flags associated with this WCKey | [optional] 

## Example

```python
from openapi_client.models.v0043_wckey import V0043Wckey

# TODO update the JSON string below
json = "{}"
# create an instance of V0043Wckey from a JSON string
v0043_wckey_instance = V0043Wckey.from_json(json)
# print the JSON string representation of the object
print(V0043Wckey.to_json())

# convert the object into a dict
v0043_wckey_dict = v0043_wckey_instance.to_dict()
# create an instance of V0043Wckey from a dict
v0043_wckey_from_dict = V0043Wckey.from_dict(v0043_wckey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


