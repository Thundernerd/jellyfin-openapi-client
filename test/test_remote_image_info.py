# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.remote_image_info import RemoteImageInfo

class TestRemoteImageInfo(unittest.TestCase):
    """RemoteImageInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemoteImageInfo:
        """Test RemoteImageInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RemoteImageInfo`
        """
        model = RemoteImageInfo()
        if include_optional:
            return RemoteImageInfo(
                provider_name = '',
                url = '',
                thumbnail_url = '',
                height = 56,
                width = 56,
                community_rating = 1.337,
                vote_count = 56,
                language = '',
                type = 'Primary',
                rating_type = 'Score'
            )
        else:
            return RemoteImageInfo(
        )
        """

    def testRemoteImageInfo(self):
        """Test RemoteImageInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
