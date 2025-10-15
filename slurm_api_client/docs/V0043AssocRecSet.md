# V0043AssocRecSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Arbitrary comment | [optional] 
**defaultqos** | **str** | Default QOS | [optional] 
**grpjobs** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**grpjobsaccrue** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**grpsubmitjobs** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**grptres** | [**List[V0043Tres]**](V0043Tres.md) |  | [optional] 
**grptresmins** | [**List[V0043Tres]**](V0043Tres.md) |  | [optional] 
**grptresrunmins** | [**List[V0043Tres]**](V0043Tres.md) |  | [optional] 
**grpwall** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**maxjobs** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**maxjobsaccrue** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**maxsubmitjobs** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**maxtresminsperjob** | [**List[V0043Tres]**](V0043Tres.md) |  | [optional] 
**maxtresrunmins** | [**List[V0043Tres]**](V0043Tres.md) |  | [optional] 
**maxtresperjob** | [**List[V0043Tres]**](V0043Tres.md) |  | [optional] 
**maxtrespernode** | [**List[V0043Tres]**](V0043Tres.md) |  | [optional] 
**maxwalldurationperjob** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**minpriothresh** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**parent** | **str** | Name of parent account | [optional] 
**priority** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 
**qoslevel** | **List[str]** | List of QOS names | [optional] 
**fairshare** | **int** | Allocated shares used for fairshare calculation | [optional] 

## Example

```python
from openapi_client.models.v0043_assoc_rec_set import V0043AssocRecSet

# TODO update the JSON string below
json = "{}"
# create an instance of V0043AssocRecSet from a JSON string
v0043_assoc_rec_set_instance = V0043AssocRecSet.from_json(json)
# print the JSON string representation of the object
print(V0043AssocRecSet.to_json())

# convert the object into a dict
v0043_assoc_rec_set_dict = v0043_assoc_rec_set_instance.to_dict()
# create an instance of V0043AssocRecSet from a dict
v0043_assoc_rec_set_from_dict = V0043AssocRecSet.from_dict(v0043_assoc_rec_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


