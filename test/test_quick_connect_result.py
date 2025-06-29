# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.quick_connect_result import QuickConnectResult

class TestQuickConnectResult(unittest.TestCase):
    """QuickConnectResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuickConnectResult:
        """Test QuickConnectResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuickConnectResult`
        """
        model = QuickConnectResult()
        if include_optional:
            return QuickConnectResult(
                authenticated = True,
                secret = '',
                code = '',
                device_id = '',
                device_name = '',
                app_name = '',
                app_version = '',
                date_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return QuickConnectResult(
        )
        """

    def testQuickConnectResult(self):
        """Test QuickConnectResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
