# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.update_user_password import UpdateUserPassword

class TestUpdateUserPassword(unittest.TestCase):
    """UpdateUserPassword unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateUserPassword:
        """Test UpdateUserPassword
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateUserPassword`
        """
        model = UpdateUserPassword()
        if include_optional:
            return UpdateUserPassword(
                current_password = '',
                current_pw = '',
                new_pw = '',
                reset_password = True
            )
        else:
            return UpdateUserPassword(
        )
        """

    def testUpdateUserPassword(self):
        """Test UpdateUserPassword"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
