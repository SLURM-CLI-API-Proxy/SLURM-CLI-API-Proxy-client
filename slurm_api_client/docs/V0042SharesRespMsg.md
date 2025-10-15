# V0042SharesRespMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares** | [**List[V0042AssocSharesObjWrap]**](V0042AssocSharesObjWrap.md) |  | [optional] 
**total_shares** | **int** | Total number of shares | [optional] 

## Example

```python
from openapi_client.models.v0042_shares_resp_msg import V0042SharesRespMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0042SharesRespMsg from a JSON string
v0042_shares_resp_msg_instance = V0042SharesRespMsg.from_json(json)
# print the JSON string representation of the object
print(V0042SharesRespMsg.to_json())

# convert the object into a dict
v0042_shares_resp_msg_dict = v0042_shares_resp_msg_instance.to_dict()
# create an instance of V0042SharesRespMsg from a dict
v0042_shares_resp_msg_from_dict = V0042SharesRespMsg.from_dict(v0042_shares_resp_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


