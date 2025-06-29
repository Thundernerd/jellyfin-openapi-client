# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.xbmc_metadata_options import XbmcMetadataOptions

class TestXbmcMetadataOptions(unittest.TestCase):
    """XbmcMetadataOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> XbmcMetadataOptions:
        """Test XbmcMetadataOptions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `XbmcMetadataOptions`
        """
        model = XbmcMetadataOptions()
        if include_optional:
            return XbmcMetadataOptions(
                user_id = '',
                release_date_format = '',
                save_image_paths_in_nfo = True,
                enable_path_substitution = True,
                enable_extra_thumbs_duplication = True
            )
        else:
            return XbmcMetadataOptions(
        )
        """

    def testXbmcMetadataOptions(self):
        """Test XbmcMetadataOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
