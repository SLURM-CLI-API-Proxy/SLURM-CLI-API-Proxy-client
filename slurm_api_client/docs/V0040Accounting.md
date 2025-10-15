# V0040Accounting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**V0040AccountingAllocated**](V0040AccountingAllocated.md) |  | [optional] 
**id** | **int** | Association ID or Workload characterization key ID | [optional] 
**start** | **int** | When the record was started | [optional] 
**tres** | [**V0040Tres**](V0040Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_accounting import V0040Accounting

# TODO update the JSON string below
json = "{}"
# create an instance of V0040Accounting from a JSON string
v0040_accounting_instance = V0040Accounting.from_json(json)
# print the JSON string representation of the object
print(V0040Accounting.to_json())

# convert the object into a dict
v0040_accounting_dict = v0040_accounting_instance.to_dict()
# create an instance of V0040Accounting from a dict
v0040_accounting_from_dict = V0040Accounting.from_dict(v0040_accounting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


