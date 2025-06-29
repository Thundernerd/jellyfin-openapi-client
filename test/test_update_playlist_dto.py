# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.update_playlist_dto import UpdatePlaylistDto

class TestUpdatePlaylistDto(unittest.TestCase):
    """UpdatePlaylistDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdatePlaylistDto:
        """Test UpdatePlaylistDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdatePlaylistDto`
        """
        model = UpdatePlaylistDto()
        if include_optional:
            return UpdatePlaylistDto(
                name = '',
                ids = [
                    ''
                    ],
                users = [
                    openapi_client.models.playlist_user_permissions.PlaylistUserPermissions(
                        user_id = '', 
                        can_edit = True, )
                    ],
                is_public = True
            )
        else:
            return UpdatePlaylistDto(
        )
        """

    def testUpdatePlaylistDto(self):
        """Test UpdatePlaylistDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
