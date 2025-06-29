# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.user_updated_message import UserUpdatedMessage

class TestUserUpdatedMessage(unittest.TestCase):
    """UserUpdatedMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserUpdatedMessage:
        """Test UserUpdatedMessage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserUpdatedMessage`
        """
        model = UserUpdatedMessage()
        if include_optional:
            return UserUpdatedMessage(
                data = openapi_client.models.user_dto.UserDto(
                    name = '', 
                    server_id = '', 
                    server_name = '', 
                    id = '', 
                    primary_image_tag = '', 
                    has_password = True, 
                    has_configured_password = True, 
                    has_configured_easy_password = True, 
                    enable_auto_login = True, 
                    last_login_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_activity_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    configuration = null, 
                    policy = null, 
                    primary_image_aspect_ratio = 1.337, ),
                message_id = '',
                message_type = 'ForceKeepAlive'
            )
        else:
            return UserUpdatedMessage(
        )
        """

    def testUserUpdatedMessage(self):
        """Test UserUpdatedMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
