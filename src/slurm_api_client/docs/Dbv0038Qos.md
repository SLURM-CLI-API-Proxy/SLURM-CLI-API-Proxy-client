# Dbv0038Qos

QOS description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | QOS description | [optional] 
**flags** | **List[str]** | List of properties of QOS | [optional] 
**id** | **str** | Database id | [optional] 
**limits** | [**Dbv0038QosLimits**](Dbv0038QosLimits.md) |  | [optional] 
**preempt** | [**Dbv0038QosPreempt**](Dbv0038QosPreempt.md) |  | [optional] 
**priority** | **int** | QOS priority | [optional] 
**usage_factor** | **float** | Usage factor | [optional] 
**usage_threshold** | **float** | Usage threshold | [optional] 
**name** | **str** | Assigned name of QOS | [optional] 

## Example

```python
from openapi_client.models.dbv0038_qos import Dbv0038Qos

# TODO update the JSON string below
json = "{}"
# create an instance of Dbv0038Qos from a JSON string
dbv0038_qos_instance = Dbv0038Qos.from_json(json)
# print the JSON string representation of the object
print(Dbv0038Qos.to_json())

# convert the object into a dict
dbv0038_qos_dict = dbv0038_qos_instance.to_dict()
# create an instance of Dbv0038Qos from a dict
dbv0038_qos_from_dict = Dbv0038Qos.from_dict(dbv0038_qos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


