# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.plugin_installation_cancelled_message import PluginInstallationCancelledMessage

class TestPluginInstallationCancelledMessage(unittest.TestCase):
    """PluginInstallationCancelledMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PluginInstallationCancelledMessage:
        """Test PluginInstallationCancelledMessage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PluginInstallationCancelledMessage`
        """
        model = PluginInstallationCancelledMessage()
        if include_optional:
            return PluginInstallationCancelledMessage(
                data = openapi_client.models.installation_info.InstallationInfo(
                    guid = '', 
                    name = '', 
                    version = '', 
                    changelog = '', 
                    source_url = '', 
                    checksum = '', 
                    package_info = null, ),
                message_id = '',
                message_type = 'ForceKeepAlive'
            )
        else:
            return PluginInstallationCancelledMessage(
        )
        """

    def testPluginInstallationCancelledMessage(self):
        """Test PluginInstallationCancelledMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
