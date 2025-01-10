# V0039Assoc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** |  | [optional] 
**cluster** | **str** |  | [optional] 
**default** | [**V0039AssocDefault**](V0039AssocDefault.md) |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**max** | [**V0039AssocMax**](V0039AssocMax.md) |  | [optional] 
**is_default** | **bool** |  | [optional] 
**min** | [**V0039AssocMin**](V0039AssocMin.md) |  | [optional] 
**parent_account** | **str** |  | [optional] 
**partition** | **str** |  | [optional] 
**priority** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**qos** | **List[str]** | List of QOS names | [optional] 
**shares_raw** | **int** |  | [optional] 
**usage** | [**V0039AssocUsage**](V0039AssocUsage.md) |  | [optional] 
**user** | **str** |  | 

## Example

```python
from openapi_client.models.v0039_assoc import V0039Assoc

# TODO update the JSON string below
json = "{}"
# create an instance of V0039Assoc from a JSON string
v0039_assoc_instance = V0039Assoc.from_json(json)
# print the JSON string representation of the object
print(V0039Assoc.to_json())

# convert the object into a dict
v0039_assoc_dict = v0039_assoc_instance.to_dict()
# create an instance of V0039Assoc from a dict
v0039_assoc_from_dict = V0039Assoc.from_dict(v0039_assoc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


