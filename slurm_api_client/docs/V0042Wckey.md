# V0042Wckey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting** | [**List[V0042Accounting]**](V0042Accounting.md) |  | [optional] 
**cluster** | **str** | Cluster name | 
**id** | **int** | Unique ID for this user-cluster-wckey combination | [optional] 
**name** | **str** | WCKey name | 
**user** | **str** | User name | 
**flags** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.v0042_wckey import V0042Wckey

# TODO update the JSON string below
json = "{}"
# create an instance of V0042Wckey from a JSON string
v0042_wckey_instance = V0042Wckey.from_json(json)
# print the JSON string representation of the object
print(V0042Wckey.to_json())

# convert the object into a dict
v0042_wckey_dict = v0042_wckey_instance.to_dict()
# create an instance of V0042Wckey from a dict
v0042_wckey_from_dict = V0042Wckey.from_dict(v0042_wckey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


