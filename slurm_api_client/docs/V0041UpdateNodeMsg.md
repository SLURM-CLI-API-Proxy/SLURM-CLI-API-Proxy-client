# V0041UpdateNodeMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Arbitrary comment | [optional] 
**cpu_bind** | **int** | Default method for binding tasks to allocated CPUs | [optional] 
**extra** | **str** | Arbitrary string used for node filtering if extra constraints are enabled | [optional] 
**features** | **List[str]** | Available features | [optional] 
**features_act** | **List[str]** | Currently active features | [optional] 
**gres** | **str** | Generic resources | [optional] 
**address** | **List[str]** | NodeAddr, used to establish a communication path | [optional] 
**hostname** | **List[str]** | NodeHostname | [optional] 
**name** | **List[str]** | NodeName | [optional] 
**state** | **List[str]** | New state to assign to the node | [optional] 
**reason** | **str** | Reason for node being DOWN or DRAINING | [optional] 
**reason_uid** | **str** | User ID to associate with the reason (needed if user root is sending message) | [optional] 
**resume_after** | [**V0041UpdateNodeMsgResumeAfter**](V0041UpdateNodeMsgResumeAfter.md) |  | [optional] 
**weight** | [**V0041UpdateNodeMsgWeight**](V0041UpdateNodeMsgWeight.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_update_node_msg import V0041UpdateNodeMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0041UpdateNodeMsg from a JSON string
v0041_update_node_msg_instance = V0041UpdateNodeMsg.from_json(json)
# print the JSON string representation of the object
print(V0041UpdateNodeMsg.to_json())

# convert the object into a dict
v0041_update_node_msg_dict = v0041_update_node_msg_instance.to_dict()
# create an instance of V0041UpdateNodeMsg from a dict
v0041_update_node_msg_from_dict = V0041UpdateNodeMsg.from_dict(v0041_update_node_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


