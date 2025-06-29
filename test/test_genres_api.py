# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.genres_api import GenresApi


class TestGenresApi(unittest.TestCase):
    """GenresApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GenresApi()

    def tearDown(self) -> None:
        pass

    def test_get_genre(self) -> None:
        """Test case for get_genre

        Gets a genre, by name.
        """
        pass

    def test_get_genres(self) -> None:
        """Test case for get_genres

        Gets all genres from a given item, folder, or the entire library.
        """
        pass


if __name__ == '__main__':
    unittest.main()
