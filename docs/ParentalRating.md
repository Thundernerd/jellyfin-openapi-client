# ParentalRating

Class ParentalRating.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**value** | **int** | Gets or sets the value. | [optional] 
**rating_score** | [**ParentalRatingScore**](ParentalRatingScore.md) | Gets or sets the rating score. | [optional] 

## Example

```python
from openapi_client.models.parental_rating import ParentalRating

# TODO update the JSON string below
json = "{}"
# create an instance of ParentalRating from a JSON string
parental_rating_instance = ParentalRating.from_json(json)
# print the JSON string representation of the object
print(ParentalRating.to_json())

# convert the object into a dict
parental_rating_dict = parental_rating_instance.to_dict()
# create an instance of ParentalRating from a dict
parental_rating_from_dict = ParentalRating.from_dict(parental_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


