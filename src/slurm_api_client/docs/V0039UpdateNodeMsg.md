# V0039UpdateNodeMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | arbitrary comment | [optional] 
**cpu_bind** | **int** | default CPU binding type | [optional] 
**extra** | **str** | arbitrary string | [optional] 
**features** | **List[str]** |  | [optional] 
**features_act** | **List[str]** |  | [optional] 
**gres** | **str** | new generic resources for node | [optional] 
**address** | **List[str]** |  | [optional] 
**hostname** | **List[str]** |  | [optional] 
**name** | **List[str]** |  | [optional] 
**state** | **List[str]** | assign new node state | [optional] 
**reason** | **str** | reason for node being DOWN or DRAINING | [optional] 
**reason_uid** | **str** | user ID of sending (needed if user root is sending message) | [optional] 
**resume_after** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**weight** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_update_node_msg import V0039UpdateNodeMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0039UpdateNodeMsg from a JSON string
v0039_update_node_msg_instance = V0039UpdateNodeMsg.from_json(json)
# print the JSON string representation of the object
print(V0039UpdateNodeMsg.to_json())

# convert the object into a dict
v0039_update_node_msg_dict = v0039_update_node_msg_instance.to_dict()
# create an instance of V0039UpdateNodeMsg from a dict
v0039_update_node_msg_from_dict = V0039UpdateNodeMsg.from_dict(v0039_update_node_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


