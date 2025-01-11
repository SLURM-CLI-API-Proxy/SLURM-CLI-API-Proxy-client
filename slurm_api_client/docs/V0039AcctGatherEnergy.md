# V0039AcctGatherEnergy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_watts** | **int** |  | [optional] 
**base_consumed_energy** | **int** |  | [optional] 
**consumed_energy** | **int** |  | [optional] 
**current_watts** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**previous_consumed_energy** | **int** |  | [optional] 
**last_collected** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.v0039_acct_gather_energy import V0039AcctGatherEnergy

# TODO update the JSON string below
json = "{}"
# create an instance of V0039AcctGatherEnergy from a JSON string
v0039_acct_gather_energy_instance = V0039AcctGatherEnergy.from_json(json)
# print the JSON string representation of the object
print(V0039AcctGatherEnergy.to_json())

# convert the object into a dict
v0039_acct_gather_energy_dict = v0039_acct_gather_energy_instance.to_dict()
# create an instance of V0039AcctGatherEnergy from a dict
v0039_acct_gather_energy_from_dict = V0039AcctGatherEnergy.from_dict(v0039_acct_gather_energy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


