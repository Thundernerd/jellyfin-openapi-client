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
from typing import Optional, Set
from typing_extensions import Self

class XbmcMetadataOptions(BaseModel):
    """
    XbmcMetadataOptions
    """ # noqa: E501
    user_id: Optional[StrictStr] = Field(default=None, alias="UserId")
    release_date_format: Optional[StrictStr] = Field(default=None, alias="ReleaseDateFormat")
    save_image_paths_in_nfo: Optional[StrictBool] = Field(default=None, alias="SaveImagePathsInNfo")
    enable_path_substitution: Optional[StrictBool] = Field(default=None, alias="EnablePathSubstitution")
    enable_extra_thumbs_duplication: Optional[StrictBool] = Field(default=None, alias="EnableExtraThumbsDuplication")
    __properties: ClassVar[List[str]] = ["UserId", "ReleaseDateFormat", "SaveImagePathsInNfo", "EnablePathSubstitution", "EnableExtraThumbsDuplication"]

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
        """Create an instance of XbmcMetadataOptions from a JSON string"""
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
        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['UserId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of XbmcMetadataOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "UserId": obj.get("UserId"),
            "ReleaseDateFormat": obj.get("ReleaseDateFormat"),
            "SaveImagePathsInNfo": obj.get("SaveImagePathsInNfo"),
            "EnablePathSubstitution": obj.get("EnablePathSubstitution"),
            "EnableExtraThumbsDuplication": obj.get("EnableExtraThumbsDuplication")
        })
        return _obj


