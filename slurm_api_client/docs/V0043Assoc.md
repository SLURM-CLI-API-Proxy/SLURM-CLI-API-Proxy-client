# V0043Assoc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting** | [**List[V0043Accounting]**](V0043Accounting.md) |  | [optional] 
**account** | **str** | Account name | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**comment** | **str** | Arbitrary comment | [optional] 
**default** | [**V0040AssocDefault**](V0040AssocDefault.md) |  | [optional] 
**flags** | **List[str]** | Flags on the association | [optional] 
**max** | [**V0043AssocMax**](V0043AssocMax.md) |  | [optional] 
**id** | **int** | Unique ID (Association ID) | [optional] 
**is_default** | **bool** | Is default association for user | [optional] 
**lineage** | **str** | Complete path up the hierarchy to the root association | [optional] 
**min** | [**V0043AssocMin**](V0043AssocMin.md) |  | [optional] 
**parent_account** | **str** | Name of parent account | [optional] 
**partition** | **str** | Partition name | [optional] 
**priority** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**qos** | **List[str]** | List of QOS names | [optional] 
**shares_raw** | **int** | Allocated shares used for fairshare calculation | [optional] 
**user** | **str** | User name | 

## Example

```python
from openapi_client.models.v0043_assoc import V0043Assoc

# TODO update the JSON string below
json = "{}"
# create an instance of V0043Assoc from a JSON string
v0043_assoc_instance = V0043Assoc.from_json(json)
# print the JSON string representation of the object
print(V0043Assoc.to_json())

# convert the object into a dict
v0043_assoc_dict = v0043_assoc_instance.to_dict()
# create an instance of V0043Assoc from a dict
v0043_assoc_from_dict = V0043Assoc.from_dict(v0043_assoc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


