# V0042JobHet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | Heterogeneous job ID, if applicable | [optional] 
**job_offset** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0042_job_het import V0042JobHet

# TODO update the JSON string below
json = "{}"
# create an instance of V0042JobHet from a JSON string
v0042_job_het_instance = V0042JobHet.from_json(json)
# print the JSON string representation of the object
print(V0042JobHet.to_json())

# convert the object into a dict
v0042_job_het_dict = v0042_job_het_instance.to_dict()
# create an instance of V0042JobHet from a dict
v0042_job_het_from_dict = V0042JobHet.from_dict(v0042_job_het_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


