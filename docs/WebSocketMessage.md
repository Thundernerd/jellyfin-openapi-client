# WebSocketMessage

Represents the possible websocket types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GroupUpdate**](GroupUpdate.md) | Group update data | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.SYNCPLAYGROUPUPDATE]

## Example

```python
from openapi_client.models.web_socket_message import WebSocketMessage

# TODO update the JSON string below
json = "{}"
# create an instance of WebSocketMessage from a JSON string
web_socket_message_instance = WebSocketMessage.from_json(json)
# print the JSON string representation of the object
print(WebSocketMessage.to_json())

# convert the object into a dict
web_socket_message_dict = web_socket_message_instance.to_dict()
# create an instance of WebSocketMessage from a dict
web_socket_message_from_dict = WebSocketMessage.from_dict(web_socket_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


