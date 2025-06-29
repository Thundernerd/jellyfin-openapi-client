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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.library_option_info_dto import LibraryOptionInfoDto
from openapi_client.models.library_type_options_dto import LibraryTypeOptionsDto
from typing import Optional, Set
from typing_extensions import Self

class LibraryOptionsResultDto(BaseModel):
    """
    Library options result dto.
    """ # noqa: E501
    metadata_savers: Optional[List[LibraryOptionInfoDto]] = Field(default=None, description="Gets or sets the metadata savers.", alias="MetadataSavers")
    metadata_readers: Optional[List[LibraryOptionInfoDto]] = Field(default=None, description="Gets or sets the metadata readers.", alias="MetadataReaders")
    subtitle_fetchers: Optional[List[LibraryOptionInfoDto]] = Field(default=None, description="Gets or sets the subtitle fetchers.", alias="SubtitleFetchers")
    lyric_fetchers: Optional[List[LibraryOptionInfoDto]] = Field(default=None, description="Gets or sets the list of lyric fetchers.", alias="LyricFetchers")
    media_segment_providers: Optional[List[LibraryOptionInfoDto]] = Field(default=None, description="Gets or sets the list of MediaSegment Providers.", alias="MediaSegmentProviders")
    type_options: Optional[List[LibraryTypeOptionsDto]] = Field(default=None, description="Gets or sets the type options.", alias="TypeOptions")
    __properties: ClassVar[List[str]] = ["MetadataSavers", "MetadataReaders", "SubtitleFetchers", "LyricFetchers", "MediaSegmentProviders", "TypeOptions"]

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
        """Create an instance of LibraryOptionsResultDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in metadata_savers (list)
        _items = []
        if self.metadata_savers:
            for _item_metadata_savers in self.metadata_savers:
                if _item_metadata_savers:
                    _items.append(_item_metadata_savers.to_dict())
            _dict['MetadataSavers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in metadata_readers (list)
        _items = []
        if self.metadata_readers:
            for _item_metadata_readers in self.metadata_readers:
                if _item_metadata_readers:
                    _items.append(_item_metadata_readers.to_dict())
            _dict['MetadataReaders'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in subtitle_fetchers (list)
        _items = []
        if self.subtitle_fetchers:
            for _item_subtitle_fetchers in self.subtitle_fetchers:
                if _item_subtitle_fetchers:
                    _items.append(_item_subtitle_fetchers.to_dict())
            _dict['SubtitleFetchers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in lyric_fetchers (list)
        _items = []
        if self.lyric_fetchers:
            for _item_lyric_fetchers in self.lyric_fetchers:
                if _item_lyric_fetchers:
                    _items.append(_item_lyric_fetchers.to_dict())
            _dict['LyricFetchers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in media_segment_providers (list)
        _items = []
        if self.media_segment_providers:
            for _item_media_segment_providers in self.media_segment_providers:
                if _item_media_segment_providers:
                    _items.append(_item_media_segment_providers.to_dict())
            _dict['MediaSegmentProviders'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in type_options (list)
        _items = []
        if self.type_options:
            for _item_type_options in self.type_options:
                if _item_type_options:
                    _items.append(_item_type_options.to_dict())
            _dict['TypeOptions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LibraryOptionsResultDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "MetadataSavers": [LibraryOptionInfoDto.from_dict(_item) for _item in obj["MetadataSavers"]] if obj.get("MetadataSavers") is not None else None,
            "MetadataReaders": [LibraryOptionInfoDto.from_dict(_item) for _item in obj["MetadataReaders"]] if obj.get("MetadataReaders") is not None else None,
            "SubtitleFetchers": [LibraryOptionInfoDto.from_dict(_item) for _item in obj["SubtitleFetchers"]] if obj.get("SubtitleFetchers") is not None else None,
            "LyricFetchers": [LibraryOptionInfoDto.from_dict(_item) for _item in obj["LyricFetchers"]] if obj.get("LyricFetchers") is not None else None,
            "MediaSegmentProviders": [LibraryOptionInfoDto.from_dict(_item) for _item in obj["MediaSegmentProviders"]] if obj.get("MediaSegmentProviders") is not None else None,
            "TypeOptions": [LibraryTypeOptionsDto.from_dict(_item) for _item in obj["TypeOptions"]] if obj.get("TypeOptions") is not None else None
        })
        return _obj


