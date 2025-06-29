# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TrickplayInfo(BaseModel):
    """
    An entity representing the metadata for a group of trickplay tiles.
    """ # noqa: E501
    item_id: Optional[StrictStr] = Field(default=None, description="Gets or sets the id of the associated item.", alias="ItemId")
    width: Optional[StrictInt] = Field(default=None, description="Gets or sets width of an individual thumbnail.", alias="Width")
    height: Optional[StrictInt] = Field(default=None, description="Gets or sets height of an individual thumbnail.", alias="Height")
    tile_width: Optional[StrictInt] = Field(default=None, description="Gets or sets amount of thumbnails per row.", alias="TileWidth")
    tile_height: Optional[StrictInt] = Field(default=None, description="Gets or sets amount of thumbnails per column.", alias="TileHeight")
    thumbnail_count: Optional[StrictInt] = Field(default=None, description="Gets or sets total amount of non-black thumbnails.", alias="ThumbnailCount")
    interval: Optional[StrictInt] = Field(default=None, description="Gets or sets interval in milliseconds between each trickplay thumbnail.", alias="Interval")
    bandwidth: Optional[StrictInt] = Field(default=None, description="Gets or sets peak bandwidth usage in bits per second.", alias="Bandwidth")
    __properties: ClassVar[List[str]] = ["ItemId", "Width", "Height", "TileWidth", "TileHeight", "ThumbnailCount", "Interval", "Bandwidth"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TrickplayInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrickplayInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ItemId": obj.get("ItemId"),
            "Width": obj.get("Width"),
            "Height": obj.get("Height"),
            "TileWidth": obj.get("TileWidth"),
            "TileHeight": obj.get("TileHeight"),
            "ThumbnailCount": obj.get("ThumbnailCount"),
            "Interval": obj.get("Interval"),
            "Bandwidth": obj.get("Bandwidth")
        })
        return _obj


