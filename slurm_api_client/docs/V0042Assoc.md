# V0042Assoc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting** | [**List[V0042Accounting]**](V0042Accounting.md) |  | [optional] 
**account** | **str** | Account name | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**comment** | **str** | Arbitrary comment | [optional] 
**default** | [**V0040AssocDefault**](V0040AssocDefault.md) |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**max** | [**V0042AssocMax**](V0042AssocMax.md) |  | [optional] 
**id** | **int** | Unique ID | [optional] 
**is_default** | **bool** | Is default association for user | [optional] 
**lineage** | **str** | Complete path up the hierarchy to the root association | [optional] 
**min** | [**V0042AssocMin**](V0042AssocMin.md) |  | [optional] 
**parent_account** | **str** | Name of parent account | [optional] 
**partition** | **str** | Partition name | [optional] 
**priority** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**qos** | **List[str]** | List of QOS names | [optional] 
**shares_raw** | **int** | Allocated shares used for fairshare calculation | [optional] 
**user** | **str** | User name | 

## Example

```python
from openapi_client.models.v0042_assoc import V0042Assoc

# TODO update the JSON string below
json = "{}"
# create an instance of V0042Assoc from a JSON string
v0042_assoc_instance = V0042Assoc.from_json(json)
# print the JSON string representation of the object
print(V0042Assoc.to_json())

# convert the object into a dict
v0042_assoc_dict = v0042_assoc_instance.to_dict()
# create an instance of V0042Assoc from a dict
v0042_assoc_from_dict = V0042Assoc.from_dict(v0042_assoc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


