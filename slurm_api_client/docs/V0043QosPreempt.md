# V0043QosPreempt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | **List[str]** |  | [optional] 
**mode** | **List[str]** | PreemptMode - Mechanism used to preempt jobs or enable gang scheduling | [optional] 
**exempt_time** | [**V0043Uint32NoValStruct**](V0043Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0043_qos_preempt import V0043QosPreempt

# TODO update the JSON string below
json = "{}"
# create an instance of V0043QosPreempt from a JSON string
v0043_qos_preempt_instance = V0043QosPreempt.from_json(json)
# print the JSON string representation of the object
print(V0043QosPreempt.to_json())

# convert the object into a dict
v0043_qos_preempt_dict = v0043_qos_preempt_instance.to_dict()
# create an instance of V0043QosPreempt from a dict
v0043_qos_preempt_from_dict = V0043QosPreempt.from_dict(v0043_qos_preempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


