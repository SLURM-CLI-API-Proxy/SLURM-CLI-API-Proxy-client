# V0040AssocRecSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Arbitrary comment | [optional] 
**defaultqos** | **str** | Default QOS | [optional] 
**grpjobs** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**grpjobsaccrue** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**grpsubmitjobs** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**grptres** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**grptresmins** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**grptresrunmins** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**grpwall** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**maxjobs** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**maxjobsaccrue** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**maxsubmitjobs** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**maxtresminsperjob** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**maxtresrunmins** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**maxtresperjob** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**maxtrespernode** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**maxwalldurationperjob** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**minpriothresh** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**parent** | **str** | Name of parent account | [optional] 
**priority** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**qoslevel** | **List[str]** | List of QOS names | [optional] 
**fairshare** | **int** | Allocated shares used for fairshare calculation | [optional] 

## Example

```python
from openapi_client.models.v0040_assoc_rec_set import V0040AssocRecSet

# TODO update the JSON string below
json = "{}"
# create an instance of V0040AssocRecSet from a JSON string
v0040_assoc_rec_set_instance = V0040AssocRecSet.from_json(json)
# print the JSON string representation of the object
print(V0040AssocRecSet.to_json())

# convert the object into a dict
v0040_assoc_rec_set_dict = v0040_assoc_rec_set_instance.to_dict()
# create an instance of V0040AssocRecSet from a dict
v0040_assoc_rec_set_from_dict = V0040AssocRecSet.from_dict(v0040_assoc_rec_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


