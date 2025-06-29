# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DlnaProfileType(str, Enum):
    """
    DlnaProfileType
    """

    """
    allowed enum values
    """
    AUDIO = 'Audio'
    VIDEO = 'Video'
    PHOTO = 'Photo'
    SUBTITLE = 'Subtitle'
    LYRIC = 'Lyric'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DlnaProfileType from a JSON string"""
        return cls(json.loads(json_str))


