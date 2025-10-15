# V0043Accounting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**V0042AccountingAllocated**](V0042AccountingAllocated.md) |  | [optional] 
**id** | **int** | Association ID or Workload characterization key ID | [optional] 
**id_alt** | **int** | Alternate ID (not currently used) | [optional] 
**start** | **int** | When the record was started (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**tres** | [**V0043Tres**](V0043Tres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_accounting import V0043Accounting

# TODO update the JSON string below
json = "{}"
# create an instance of V0043Accounting from a JSON string
v0043_accounting_instance = V0043Accounting.from_json(json)
# print the JSON string representation of the object
print(V0043Accounting.to_json())

# convert the object into a dict
v0043_accounting_dict = v0043_accounting_instance.to_dict()
# create an instance of V0043Accounting from a dict
v0043_accounting_from_dict = V0043Accounting.from_dict(v0043_accounting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


