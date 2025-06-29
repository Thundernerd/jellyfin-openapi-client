# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.user_library_api import UserLibraryApi


class TestUserLibraryApi(unittest.TestCase):
    """UserLibraryApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserLibraryApi()

    def tearDown(self) -> None:
        pass

    def test_delete_user_item_rating(self) -> None:
        """Test case for delete_user_item_rating

        Deletes a user's saved personal rating for an item.
        """
        pass

    def test_get_intros(self) -> None:
        """Test case for get_intros

        Gets intros to play before the main media item plays.
        """
        pass

    def test_get_item(self) -> None:
        """Test case for get_item

        Gets an item from a user's library.
        """
        pass

    def test_get_latest_media(self) -> None:
        """Test case for get_latest_media

        Gets latest media.
        """
        pass

    def test_get_local_trailers(self) -> None:
        """Test case for get_local_trailers

        Gets local trailers for an item.
        """
        pass

    def test_get_root_folder(self) -> None:
        """Test case for get_root_folder

        Gets the root folder from a user's library.
        """
        pass

    def test_get_special_features(self) -> None:
        """Test case for get_special_features

        Gets special features for an item.
        """
        pass

    def test_mark_favorite_item(self) -> None:
        """Test case for mark_favorite_item

        Marks an item as a favorite.
        """
        pass

    def test_unmark_favorite_item(self) -> None:
        """Test case for unmark_favorite_item

        Unmarks item as a favorite.
        """
        pass

    def test_update_user_item_rating(self) -> None:
        """Test case for update_user_item_rating

        Updates a user's rating for an item.
        """
        pass


if __name__ == '__main__':
    unittest.main()
