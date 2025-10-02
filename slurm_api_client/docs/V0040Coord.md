# V0040Coord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User name | 
**direct** | **bool** | Indicates whether the coordinator was directly assigned to this account | [optional] 

## Example

```python
from openapi_client.models.v0040_coord import V0040Coord

# TODO update the JSON string below
json = "{}"
# create an instance of V0040Coord from a JSON string
v0040_coord_instance = V0040Coord.from_json(json)
# print the JSON string representation of the object
print(V0040Coord.to_json())

# convert the object into a dict
v0040_coord_dict = v0040_coord_instance.to_dict()
# create an instance of V0040Coord from a dict
v0040_coord_from_dict = V0040Coord.from_dict(v0040_coord_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


