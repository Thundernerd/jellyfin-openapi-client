# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sync_play_queue_item import SyncPlayQueueItem

class TestSyncPlayQueueItem(unittest.TestCase):
    """SyncPlayQueueItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SyncPlayQueueItem:
        """Test SyncPlayQueueItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SyncPlayQueueItem`
        """
        model = SyncPlayQueueItem()
        if include_optional:
            return SyncPlayQueueItem(
                item_id = '',
                playlist_item_id = ''
            )
        else:
            return SyncPlayQueueItem(
        )
        """

    def testSyncPlayQueueItem(self):
        """Test SyncPlayQueueItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
