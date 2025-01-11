# V0040Assoc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting** | [**List[V0040Accounting]**](V0040Accounting.md) |  | [optional] 
**account** | **str** |  | [optional] 
**cluster** | **str** |  | [optional] 
**comment** | **str** | comment for the association | [optional] 
**default** | [**V0039AssocDefault**](V0039AssocDefault.md) |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**max** | [**V0040AssocMax**](V0040AssocMax.md) |  | [optional] 
**id** | [**V0040AssocShort**](V0040AssocShort.md) |  | [optional] 
**is_default** | **bool** |  | [optional] 
**lineage** | **str** | Complete path up the hierarchy to the root association | [optional] 
**min** | [**V0040AssocMin**](V0040AssocMin.md) |  | [optional] 
**parent_account** | **str** |  | [optional] 
**partition** | **str** |  | [optional] 
**priority** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**qos** | **List[str]** | List of QOS names | [optional] 
**shares_raw** | **int** |  | [optional] 
**user** | **str** |  | 

## Example

```python
from openapi_client.models.v0040_assoc import V0040Assoc

# TODO update the JSON string below
json = "{}"
# create an instance of V0040Assoc from a JSON string
v0040_assoc_instance = V0040Assoc.from_json(json)
# print the JSON string representation of the object
print(V0040Assoc.to_json())

# convert the object into a dict
v0040_assoc_dict = v0040_assoc_instance.to_dict()
# create an instance of V0040Assoc from a dict
v0040_assoc_from_dict = V0040Assoc.from_dict(v0040_assoc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


