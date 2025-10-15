# V0042Accounting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**V0042AccountingAllocated**](V0042AccountingAllocated.md) |  | [optional] 
**id** | **int** | Association ID or Workload characterization key ID | [optional] 
**id_alt** | **int** | Alternate ID (not currently used) | [optional] 
**start** | **int** | When the record was started (UNIX timestamp) | [optional] 
**tres** | [**V0042Tres**](V0042Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_accounting import V0042Accounting

# TODO update the JSON string below
json = "{}"
# create an instance of V0042Accounting from a JSON string
v0042_accounting_instance = V0042Accounting.from_json(json)
# print the JSON string representation of the object
print(V0042Accounting.to_json())

# convert the object into a dict
v0042_accounting_dict = v0042_accounting_instance.to_dict()
# create an instance of V0042Accounting from a dict
v0042_accounting_from_dict = V0042Accounting.from_dict(v0042_accounting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


