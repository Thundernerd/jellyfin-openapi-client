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


class GeneralCommandType(str, Enum):
    """
    This exists simply to identify a set of known commands.
    """

    """
    allowed enum values
    """
    MOVEUP = 'MoveUp'
    MOVEDOWN = 'MoveDown'
    MOVELEFT = 'MoveLeft'
    MOVERIGHT = 'MoveRight'
    PAGEUP = 'PageUp'
    PAGEDOWN = 'PageDown'
    PREVIOUSLETTER = 'PreviousLetter'
    NEXTLETTER = 'NextLetter'
    TOGGLEOSD = 'ToggleOsd'
    TOGGLECONTEXTMENU = 'ToggleContextMenu'
    SELECT = 'Select'
    BACK = 'Back'
    TAKESCREENSHOT = 'TakeScreenshot'
    SENDKEY = 'SendKey'
    SENDSTRING = 'SendString'
    GOHOME = 'GoHome'
    GOTOSETTINGS = 'GoToSettings'
    VOLUMEUP = 'VolumeUp'
    VOLUMEDOWN = 'VolumeDown'
    MUTE = 'Mute'
    UNMUTE = 'Unmute'
    TOGGLEMUTE = 'ToggleMute'
    SETVOLUME = 'SetVolume'
    SETAUDIOSTREAMINDEX = 'SetAudioStreamIndex'
    SETSUBTITLESTREAMINDEX = 'SetSubtitleStreamIndex'
    TOGGLEFULLSCREEN = 'ToggleFullscreen'
    DISPLAYCONTENT = 'DisplayContent'
    GOTOSEARCH = 'GoToSearch'
    DISPLAYMESSAGE = 'DisplayMessage'
    SETREPEATMODE = 'SetRepeatMode'
    CHANNELUP = 'ChannelUp'
    CHANNELDOWN = 'ChannelDown'
    GUIDE = 'Guide'
    TOGGLESTATS = 'ToggleStats'
    PLAYMEDIASOURCE = 'PlayMediaSource'
    PLAYTRAILERS = 'PlayTrailers'
    SETSHUFFLEQUEUE = 'SetShuffleQueue'
    PLAYSTATE = 'PlayState'
    PLAYNEXT = 'PlayNext'
    TOGGLEOSDMENU = 'ToggleOsdMenu'
    PLAY = 'Play'
    SETMAXSTREAMINGBITRATE = 'SetMaxStreamingBitrate'
    SETPLAYBACKORDER = 'SetPlaybackOrder'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GeneralCommandType from a JSON string"""
        return cls(json.loads(json_str))


