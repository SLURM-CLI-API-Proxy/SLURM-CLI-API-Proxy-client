# V0038DiagRpcu


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | user | [optional] 
**user_id** | **int** | user id | [optional] 
**count** | **int** | rpc count | [optional] 
**average_time** | **int** | average time | [optional] 
**total_time** | **int** | total time | [optional] 

## Example

```python
from openapi_client.models.v0038_diag_rpcu import V0038DiagRpcu

# TODO update the JSON string below
json = "{}"
# create an instance of V0038DiagRpcu from a JSON string
v0038_diag_rpcu_instance = V0038DiagRpcu.from_json(json)
# print the JSON string representation of the object
print(V0038DiagRpcu.to_json())

# convert the object into a dict
v0038_diag_rpcu_dict = v0038_diag_rpcu_instance.to_dict()
# create an instance of V0038DiagRpcu from a dict
v0038_diag_rpcu_from_dict = V0038DiagRpcu.from_dict(v0038_diag_rpcu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


