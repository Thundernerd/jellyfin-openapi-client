# ExternalIdInfo

Represents the external id information for serialization to the client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the display name of the external id provider (IE: IMDB, MusicBrainz, etc). | [optional] 
**key** | **str** | Gets or sets the unique key for this id. This key should be unique across all providers. | [optional] 
**type** | [**ExternalIdMediaType**](ExternalIdMediaType.md) | Gets or sets the specific media type for this id. This is used to distinguish between the different  external id types for providers with multiple ids.  A null value indicates there is no specific media type associated with the external id, or this is the  default id for the external provider so there is no need to specify a type. | [optional] 

## Example

```python
from openapi_client.models.external_id_info import ExternalIdInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIdInfo from a JSON string
external_id_info_instance = ExternalIdInfo.from_json(json)
# print the JSON string representation of the object
print(ExternalIdInfo.to_json())

# convert the object into a dict
external_id_info_dict = external_id_info_instance.to_dict()
# create an instance of ExternalIdInfo from a dict
external_id_info_from_dict = ExternalIdInfo.from_dict(external_id_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


