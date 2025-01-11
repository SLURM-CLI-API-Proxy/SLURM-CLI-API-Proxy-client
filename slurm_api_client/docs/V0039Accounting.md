# V0039Accounting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**V0039AccountingAllocated**](V0039AccountingAllocated.md) |  | [optional] 
**id** | **int** |  | [optional] 
**start** | **int** |  | [optional] 
**tres** | [**V0039Tres**](V0039Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_accounting import V0039Accounting

# TODO update the JSON string below
json = "{}"
# create an instance of V0039Accounting from a JSON string
v0039_accounting_instance = V0039Accounting.from_json(json)
# print the JSON string representation of the object
print(V0039Accounting.to_json())

# convert the object into a dict
v0039_accounting_dict = v0039_accounting_instance.to_dict()
# create an instance of V0039Accounting from a dict
v0039_accounting_from_dict = V0039Accounting.from_dict(v0039_accounting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


