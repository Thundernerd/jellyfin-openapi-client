# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.device_info_dto import DeviceInfoDto

class TestDeviceInfoDto(unittest.TestCase):
    """DeviceInfoDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceInfoDto:
        """Test DeviceInfoDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceInfoDto`
        """
        model = DeviceInfoDto()
        if include_optional:
            return DeviceInfoDto(
                name = '',
                custom_name = '',
                access_token = '',
                id = '',
                last_user_name = '',
                app_name = '',
                app_version = '',
                last_user_id = '',
                date_last_activity = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                capabilities = openapi_client.models.client_capabilities_dto.ClientCapabilitiesDto(
                    playable_media_types = [
                        'Unknown'
                        ], 
                    supported_commands = [
                        'MoveUp'
                        ], 
                    supports_media_control = True, 
                    supports_persistent_identifier = True, 
                    device_profile = null, 
                    app_store_url = '', 
                    icon_url = '', ),
                icon_url = ''
            )
        else:
            return DeviceInfoDto(
        )
        """

    def testDeviceInfoDto(self):
        """Test DeviceInfoDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
