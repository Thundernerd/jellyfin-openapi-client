# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sync_play_user_joined_update import SyncPlayUserJoinedUpdate

class TestSyncPlayUserJoinedUpdate(unittest.TestCase):
    """SyncPlayUserJoinedUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SyncPlayUserJoinedUpdate:
        """Test SyncPlayUserJoinedUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SyncPlayUserJoinedUpdate`
        """
        model = SyncPlayUserJoinedUpdate()
        if include_optional:
            return SyncPlayUserJoinedUpdate(
                group_id = '',
                data = '',
                type = 'UserJoined'
            )
        else:
            return SyncPlayUserJoinedUpdate(
        )
        """

    def testSyncPlayUserJoinedUpdate(self):
        """Test SyncPlayUserJoinedUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
