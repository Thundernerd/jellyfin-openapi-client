# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.album_info import AlbumInfo

class TestAlbumInfo(unittest.TestCase):
    """AlbumInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlbumInfo:
        """Test AlbumInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlbumInfo`
        """
        model = AlbumInfo()
        if include_optional:
            return AlbumInfo(
                name = '',
                original_title = '',
                path = '',
                metadata_language = '',
                metadata_country_code = '',
                provider_ids = {
                    'key' : ''
                    },
                year = 56,
                index_number = 56,
                parent_index_number = 56,
                premiere_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_automated = True,
                album_artists = [
                    ''
                    ],
                artist_provider_ids = {
                    'key' : ''
                    },
                song_infos = [
                    openapi_client.models.song_info.SongInfo(
                        name = '', 
                        original_title = '', 
                        path = '', 
                        metadata_language = '', 
                        metadata_country_code = '', 
                        provider_ids = {
                            'key' : ''
                            }, 
                        year = 56, 
                        index_number = 56, 
                        parent_index_number = 56, 
                        premiere_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_automated = True, 
                        album_artists = [
                            ''
                            ], 
                        album = '', 
                        artists = [
                            ''
                            ], )
                    ]
            )
        else:
            return AlbumInfo(
        )
        """

    def testAlbumInfo(self):
        """Test AlbumInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
