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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.media_type import MediaType
from openapi_client.models.playlist_user_permissions import PlaylistUserPermissions
from typing import Optional, Set
from typing_extensions import Self

class CreatePlaylistDto(BaseModel):
    """
    Create new playlist dto.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Gets or sets the name of the new playlist.", alias="Name")
    ids: Optional[List[StrictStr]] = Field(default=None, description="Gets or sets item ids to add to the playlist.", alias="Ids")
    user_id: Optional[StrictStr] = Field(default=None, description="Gets or sets the user id.", alias="UserId")
    media_type: Optional[MediaType] = Field(default=None, description="Gets or sets the media type.", alias="MediaType")
    users: Optional[List[PlaylistUserPermissions]] = Field(default=None, description="Gets or sets the playlist users.", alias="Users")
    is_public: Optional[StrictBool] = Field(default=None, description="Gets or sets a value indicating whether the playlist is public.", alias="IsPublic")
    __properties: ClassVar[List[str]] = ["Name", "Ids", "UserId", "MediaType", "Users", "IsPublic"]

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
        """Create an instance of CreatePlaylistDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item_users in self.users:
                if _item_users:
                    _items.append(_item_users.to_dict())
            _dict['Users'] = _items
        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['UserId'] = None

        # set to None if media_type (nullable) is None
        # and model_fields_set contains the field
        if self.media_type is None and "media_type" in self.model_fields_set:
            _dict['MediaType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreatePlaylistDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Name": obj.get("Name"),
            "Ids": obj.get("Ids"),
            "UserId": obj.get("UserId"),
            "MediaType": obj.get("MediaType"),
            "Users": [PlaylistUserPermissions.from_dict(_item) for _item in obj["Users"]] if obj.get("Users") is not None else None,
            "IsPublic": obj.get("IsPublic")
        })
        return _obj


