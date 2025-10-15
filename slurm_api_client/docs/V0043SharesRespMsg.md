# V0043SharesRespMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares** | [**List[V0043AssocSharesObjWrap]**](V0043AssocSharesObjWrap.md) |  | [optional] 
**total_shares** | **int** | Total number of shares | [optional] 

## Example

```python
from openapi_client.models.v0043_shares_resp_msg import V0043SharesRespMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0043SharesRespMsg from a JSON string
v0043_shares_resp_msg_instance = V0043SharesRespMsg.from_json(json)
# print the JSON string representation of the object
print(V0043SharesRespMsg.to_json())

# convert the object into a dict
v0043_shares_resp_msg_dict = v0043_shares_resp_msg_instance.to_dict()
# create an instance of V0043SharesRespMsg from a dict
v0043_shares_resp_msg_from_dict = V0043SharesRespMsg.from_dict(v0043_shares_resp_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


