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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.scroll_direction import ScrollDirection
from openapi_client.models.sort_order import SortOrder
from typing import Optional, Set
from typing_extensions import Self

class DisplayPreferencesDto(BaseModel):
    """
    Defines the display preferences for any item that supports them (usually Folders).
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Gets or sets the user id.", alias="Id")
    view_type: Optional[StrictStr] = Field(default=None, description="Gets or sets the type of the view.", alias="ViewType")
    sort_by: Optional[StrictStr] = Field(default=None, description="Gets or sets the sort by.", alias="SortBy")
    index_by: Optional[StrictStr] = Field(default=None, description="Gets or sets the index by.", alias="IndexBy")
    remember_indexing: Optional[StrictBool] = Field(default=None, description="Gets or sets a value indicating whether [remember indexing].", alias="RememberIndexing")
    primary_image_height: Optional[StrictInt] = Field(default=None, description="Gets or sets the height of the primary image.", alias="PrimaryImageHeight")
    primary_image_width: Optional[StrictInt] = Field(default=None, description="Gets or sets the width of the primary image.", alias="PrimaryImageWidth")
    custom_prefs: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="Gets or sets the custom prefs.", alias="CustomPrefs")
    scroll_direction: Optional[ScrollDirection] = Field(default=None, description="An enum representing the axis that should be scrolled.", alias="ScrollDirection")
    show_backdrop: Optional[StrictBool] = Field(default=None, description="Gets or sets a value indicating whether to show backdrops on this item.", alias="ShowBackdrop")
    remember_sorting: Optional[StrictBool] = Field(default=None, description="Gets or sets a value indicating whether [remember sorting].", alias="RememberSorting")
    sort_order: Optional[SortOrder] = Field(default=None, description="An enum representing the sorting order.", alias="SortOrder")
    show_sidebar: Optional[StrictBool] = Field(default=None, description="Gets or sets a value indicating whether [show sidebar].", alias="ShowSidebar")
    client: Optional[StrictStr] = Field(default=None, description="Gets or sets the client.", alias="Client")
    __properties: ClassVar[List[str]] = ["Id", "ViewType", "SortBy", "IndexBy", "RememberIndexing", "PrimaryImageHeight", "PrimaryImageWidth", "CustomPrefs", "ScrollDirection", "ShowBackdrop", "RememberSorting", "SortOrder", "ShowSidebar", "Client"]

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
        """Create an instance of DisplayPreferencesDto from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['Id'] = None

        # set to None if view_type (nullable) is None
        # and model_fields_set contains the field
        if self.view_type is None and "view_type" in self.model_fields_set:
            _dict['ViewType'] = None

        # set to None if sort_by (nullable) is None
        # and model_fields_set contains the field
        if self.sort_by is None and "sort_by" in self.model_fields_set:
            _dict['SortBy'] = None

        # set to None if index_by (nullable) is None
        # and model_fields_set contains the field
        if self.index_by is None and "index_by" in self.model_fields_set:
            _dict['IndexBy'] = None

        # set to None if client (nullable) is None
        # and model_fields_set contains the field
        if self.client is None and "client" in self.model_fields_set:
            _dict['Client'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DisplayPreferencesDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "ViewType": obj.get("ViewType"),
            "SortBy": obj.get("SortBy"),
            "IndexBy": obj.get("IndexBy"),
            "RememberIndexing": obj.get("RememberIndexing"),
            "PrimaryImageHeight": obj.get("PrimaryImageHeight"),
            "PrimaryImageWidth": obj.get("PrimaryImageWidth"),
            "CustomPrefs": obj.get("CustomPrefs"),
            "ScrollDirection": obj.get("ScrollDirection"),
            "ShowBackdrop": obj.get("ShowBackdrop"),
            "RememberSorting": obj.get("RememberSorting"),
            "SortOrder": obj.get("SortOrder"),
            "ShowSidebar": obj.get("ShowSidebar"),
            "Client": obj.get("Client")
        })
        return _obj


