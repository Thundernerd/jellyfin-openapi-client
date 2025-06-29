# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.server_configuration import ServerConfiguration

class TestServerConfiguration(unittest.TestCase):
    """ServerConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServerConfiguration:
        """Test ServerConfiguration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServerConfiguration`
        """
        model = ServerConfiguration()
        if include_optional:
            return ServerConfiguration(
                log_file_retention_days = 56,
                is_startup_wizard_completed = True,
                cache_path = '',
                previous_version = '',
                previous_version_str = '',
                enable_metrics = True,
                enable_normalized_item_by_name_ids = True,
                is_port_authorized = True,
                quick_connect_available = True,
                enable_case_sensitive_item_ids = True,
                disable_live_tv_channel_user_data_name = True,
                metadata_path = '',
                preferred_metadata_language = '',
                metadata_country_code = '',
                sort_replace_characters = [
                    ''
                    ],
                sort_remove_characters = [
                    ''
                    ],
                sort_remove_words = [
                    ''
                    ],
                min_resume_pct = 56,
                max_resume_pct = 56,
                min_resume_duration_seconds = 56,
                min_audiobook_resume = 56,
                max_audiobook_resume = 56,
                inactive_session_threshold = 56,
                library_monitor_delay = 56,
                library_update_duration = 56,
                cache_size = 56,
                image_saving_convention = 'Legacy',
                metadata_options = [
                    openapi_client.models.metadata_options.MetadataOptions(
                        item_type = '', 
                        disabled_metadata_savers = [
                            ''
                            ], 
                        local_metadata_reader_order = [
                            ''
                            ], 
                        disabled_metadata_fetchers = [
                            ''
                            ], 
                        metadata_fetcher_order = [
                            ''
                            ], 
                        disabled_image_fetchers = [
                            ''
                            ], 
                        image_fetcher_order = [
                            ''
                            ], )
                    ],
                skip_deserialization_for_basic_types = True,
                server_name = '',
                ui_culture = '',
                save_metadata_hidden = True,
                content_types = [
                    openapi_client.models.name_value_pair.NameValuePair(
                        name = '', 
                        value = '', )
                    ],
                remote_client_bitrate_limit = 56,
                enable_folder_view = True,
                enable_grouping_movies_into_collections = True,
                enable_grouping_shows_into_collections = True,
                display_specials_within_seasons = True,
                codecs_used = [
                    ''
                    ],
                plugin_repositories = [
                    openapi_client.models.repository_info.RepositoryInfo(
                        name = '', 
                        url = '', 
                        enabled = True, )
                    ],
                enable_external_content_in_suggestions = True,
                image_extraction_timeout_ms = 56,
                path_substitutions = [
                    openapi_client.models.path_substitution.PathSubstitution(
                        from = '', 
                        to = '', )
                    ],
                enable_slow_response_warning = True,
                slow_response_threshold_ms = 56,
                cors_hosts = [
                    ''
                    ],
                activity_log_retention_days = 56,
                library_scan_fanout_concurrency = 56,
                library_metadata_refresh_concurrency = 56,
                allow_client_log_upload = True,
                dummy_chapter_duration = 56,
                chapter_image_resolution = 'MatchSource',
                parallel_image_encoding_limit = 56,
                cast_receiver_applications = [
                    openapi_client.models.cast_receiver_application.CastReceiverApplication(
                        id = '', 
                        name = '', )
                    ],
                trickplay_options = openapi_client.models.trickplay_options.TrickplayOptions(
                    enable_hw_acceleration = True, 
                    enable_hw_encoding = True, 
                    enable_key_frame_only_extraction = True, 
                    scan_behavior = 'Blocking', 
                    process_priority = 'Normal', 
                    interval = 56, 
                    width_resolutions = [
                        56
                        ], 
                    tile_width = 56, 
                    tile_height = 56, 
                    qscale = 56, 
                    jpeg_quality = 56, 
                    process_threads = 56, ),
                enable_legacy_authorization = True
            )
        else:
            return ServerConfiguration(
        )
        """

    def testServerConfiguration(self):
        """Test ServerConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
