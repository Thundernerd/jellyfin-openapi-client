# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.listings_provider_info import ListingsProviderInfo

class TestListingsProviderInfo(unittest.TestCase):
    """ListingsProviderInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListingsProviderInfo:
        """Test ListingsProviderInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListingsProviderInfo`
        """
        model = ListingsProviderInfo()
        if include_optional:
            return ListingsProviderInfo(
                id = '',
                type = '',
                username = '',
                password = '',
                listings_id = '',
                zip_code = '',
                country = '',
                path = '',
                enabled_tuners = [
                    ''
                    ],
                enable_all_tuners = True,
                news_categories = [
                    ''
                    ],
                sports_categories = [
                    ''
                    ],
                kids_categories = [
                    ''
                    ],
                movie_categories = [
                    ''
                    ],
                channel_mappings = [
                    openapi_client.models.name_value_pair.NameValuePair(
                        name = '', 
                        value = '', )
                    ],
                movie_prefix = '',
                preferred_language = '',
                user_agent = ''
            )
        else:
            return ListingsProviderInfo(
        )
        """

    def testListingsProviderInfo(self):
        """Test ListingsProviderInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
