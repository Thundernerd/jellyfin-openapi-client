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
from openapi_client.models.live_tv_service_info import LiveTvServiceInfo
from typing import Optional, Set
from typing_extensions import Self

class LiveTvInfo(BaseModel):
    """
    LiveTvInfo
    """ # noqa: E501
    services: Optional[List[LiveTvServiceInfo]] = Field(default=None, description="Gets or sets the services.", alias="Services")
    is_enabled: Optional[StrictBool] = Field(default=None, description="Gets or sets a value indicating whether this instance is enabled.", alias="IsEnabled")
    enabled_users: Optional[List[StrictStr]] = Field(default=None, description="Gets or sets the enabled users.", alias="EnabledUsers")
    __properties: ClassVar[List[str]] = ["Services", "IsEnabled", "EnabledUsers"]

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
        """Create an instance of LiveTvInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in services (list)
        _items = []
        if self.services:
            for _item_services in self.services:
                if _item_services:
                    _items.append(_item_services.to_dict())
            _dict['Services'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LiveTvInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Services": [LiveTvServiceInfo.from_dict(_item) for _item in obj["Services"]] if obj.get("Services") is not None else None,
            "IsEnabled": obj.get("IsEnabled"),
            "EnabledUsers": obj.get("EnabledUsers")
        })
        return _obj


