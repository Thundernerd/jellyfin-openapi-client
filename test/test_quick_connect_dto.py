# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.quick_connect_dto import QuickConnectDto

class TestQuickConnectDto(unittest.TestCase):
    """QuickConnectDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuickConnectDto:
        """Test QuickConnectDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuickConnectDto`
        """
        model = QuickConnectDto()
        if include_optional:
            return QuickConnectDto(
                secret = ''
            )
        else:
            return QuickConnectDto(
                secret = '',
        )
        """

    def testQuickConnectDto(self):
        """Test QuickConnectDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
