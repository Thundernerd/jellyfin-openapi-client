# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.upload_subtitle_dto import UploadSubtitleDto

class TestUploadSubtitleDto(unittest.TestCase):
    """UploadSubtitleDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UploadSubtitleDto:
        """Test UploadSubtitleDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UploadSubtitleDto`
        """
        model = UploadSubtitleDto()
        if include_optional:
            return UploadSubtitleDto(
                language = '',
                format = '',
                is_forced = True,
                is_hearing_impaired = True,
                data = ''
            )
        else:
            return UploadSubtitleDto(
                language = '',
                format = '',
                is_forced = True,
                is_hearing_impaired = True,
                data = '',
        )
        """

    def testUploadSubtitleDto(self):
        """Test UploadSubtitleDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
