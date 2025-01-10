# V0040AssocMax


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**V0040AssocMaxJobs**](V0040AssocMaxJobs.md) |  | [optional] 
**tres** | [**V0040AssocMaxTres**](V0040AssocMaxTres.md) |  | [optional] 
**per** | [**V0040AssocMaxPer**](V0040AssocMaxPer.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_assoc_max import V0040AssocMax

# TODO update the JSON string below
json = "{}"
# create an instance of V0040AssocMax from a JSON string
v0040_assoc_max_instance = V0040AssocMax.from_json(json)
# print the JSON string representation of the object
print(V0040AssocMax.to_json())

# convert the object into a dict
v0040_assoc_max_dict = v0040_assoc_max_instance.to_dict()
# create an instance of V0040AssocMax from a dict
v0040_assoc_max_from_dict = V0040AssocMax.from_dict(v0040_assoc_max_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


