# V0043JobHet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | Heterogeneous job ID, if applicable | [optional] 
**job_offset** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_job_het import V0043JobHet

# TODO update the JSON string below
json = "{}"
# create an instance of V0043JobHet from a JSON string
v0043_job_het_instance = V0043JobHet.from_json(json)
# print the JSON string representation of the object
print(V0043JobHet.to_json())

# convert the object into a dict
v0043_job_het_dict = v0043_job_het_instance.to_dict()
# create an instance of V0043JobHet from a dict
v0043_job_het_from_dict = V0043JobHet.from_dict(v0043_job_het_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


