# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.client_capabilities_dto import ClientCapabilitiesDto

class TestClientCapabilitiesDto(unittest.TestCase):
    """ClientCapabilitiesDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientCapabilitiesDto:
        """Test ClientCapabilitiesDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientCapabilitiesDto`
        """
        model = ClientCapabilitiesDto()
        if include_optional:
            return ClientCapabilitiesDto(
                playable_media_types = [
                    'Unknown'
                    ],
                supported_commands = [
                    'MoveUp'
                    ],
                supports_media_control = True,
                supports_persistent_identifier = True,
                device_profile = openapi_client.models.device_profile.DeviceProfile(
                    name = '', 
                    id = '', 
                    max_streaming_bitrate = 56, 
                    max_static_bitrate = 56, 
                    music_streaming_transcoding_bitrate = 56, 
                    max_static_music_bitrate = 56, 
                    direct_play_profiles = [
                        openapi_client.models.direct_play_profile.DirectPlayProfile(
                            container = '', 
                            audio_codec = '', 
                            video_codec = '', 
                            type = 'Audio', )
                        ], 
                    transcoding_profiles = [
                        openapi_client.models.transcoding_profile.TranscodingProfile(
                            container = '', 
                            type = 'Audio', 
                            video_codec = '', 
                            audio_codec = '', 
                            protocol = 'http', 
                            estimate_content_length = True, 
                            enable_mpegts_m2_ts_mode = True, 
                            transcode_seek_info = 'Auto', 
                            copy_timestamps = True, 
                            context = 'Streaming', 
                            enable_subtitles_in_manifest = True, 
                            max_audio_channels = '', 
                            min_segments = 56, 
                            segment_length = 56, 
                            break_on_non_key_frames = True, 
                            conditions = [
                                openapi_client.models.profile_condition.ProfileCondition(
                                    condition = 'Equals', 
                                    property = 'AudioChannels', 
                                    value = '', 
                                    is_required = True, )
                                ], 
                            enable_audio_vbr_encoding = True, )
                        ], 
                    container_profiles = [
                        openapi_client.models.container_profile.ContainerProfile(
                            type = 'Audio', 
                            container = '', 
                            sub_container = '', )
                        ], 
                    codec_profiles = [
                        openapi_client.models.codec_profile.CodecProfile(
                            type = 'Video', 
                            apply_conditions = [
                                openapi_client.models.profile_condition.ProfileCondition(
                                    condition = 'Equals', 
                                    property = 'AudioChannels', 
                                    value = '', 
                                    is_required = True, )
                                ], 
                            codec = '', 
                            container = '', 
                            sub_container = '', )
                        ], 
                    subtitle_profiles = [
                        openapi_client.models.subtitle_profile.SubtitleProfile(
                            format = '', 
                            method = 'Encode', 
                            didl_mode = '', 
                            language = '', 
                            container = '', )
                        ], ),
                app_store_url = '',
                icon_url = ''
            )
        else:
            return ClientCapabilitiesDto(
        )
        """

    def testClientCapabilitiesDto(self):
        """Test ClientCapabilitiesDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
