# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.config_image_types import ConfigImageTypes

class TestConfigImageTypes(unittest.TestCase):
    """ConfigImageTypes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigImageTypes:
        """Test ConfigImageTypes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigImageTypes`
        """
        model = ConfigImageTypes()
        if include_optional:
            return ConfigImageTypes(
                backdrop_sizes = [
                    ''
                    ],
                base_url = '',
                logo_sizes = [
                    ''
                    ],
                poster_sizes = [
                    ''
                    ],
                profile_sizes = [
                    ''
                    ],
                secure_base_url = '',
                still_sizes = [
                    ''
                    ]
            )
        else:
            return ConfigImageTypes(
        )
        """

    def testConfigImageTypes(self):
        """Test ConfigImageTypes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
