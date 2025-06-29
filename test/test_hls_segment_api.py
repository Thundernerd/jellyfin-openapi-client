# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.hls_segment_api import HlsSegmentApi


class TestHlsSegmentApi(unittest.TestCase):
    """HlsSegmentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HlsSegmentApi()

    def tearDown(self) -> None:
        pass

    def test_get_hls_audio_segment_legacy_aac(self) -> None:
        """Test case for get_hls_audio_segment_legacy_aac

        Gets the specified audio segment for an audio item.
        """
        pass

    def test_get_hls_audio_segment_legacy_mp3(self) -> None:
        """Test case for get_hls_audio_segment_legacy_mp3

        Gets the specified audio segment for an audio item.
        """
        pass

    def test_get_hls_playlist_legacy(self) -> None:
        """Test case for get_hls_playlist_legacy

        Gets a hls video playlist.
        """
        pass

    def test_get_hls_video_segment_legacy(self) -> None:
        """Test case for get_hls_video_segment_legacy

        Gets a hls video segment.
        """
        pass

    def test_stop_encoding_process(self) -> None:
        """Test case for stop_encoding_process

        Stops an active encoding.
        """
        pass


if __name__ == '__main__':
    unittest.main()
