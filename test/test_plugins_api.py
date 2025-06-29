# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.plugins_api import PluginsApi


class TestPluginsApi(unittest.TestCase):
    """PluginsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PluginsApi()

    def tearDown(self) -> None:
        pass

    def test_disable_plugin(self) -> None:
        """Test case for disable_plugin

        Disable a plugin.
        """
        pass

    def test_enable_plugin(self) -> None:
        """Test case for enable_plugin

        Enables a disabled plugin.
        """
        pass

    def test_get_plugin_configuration(self) -> None:
        """Test case for get_plugin_configuration

        Gets plugin configuration.
        """
        pass

    def test_get_plugin_image(self) -> None:
        """Test case for get_plugin_image

        Gets a plugin's image.
        """
        pass

    def test_get_plugin_manifest(self) -> None:
        """Test case for get_plugin_manifest

        Gets a plugin's manifest.
        """
        pass

    def test_get_plugins(self) -> None:
        """Test case for get_plugins

        Gets a list of currently installed plugins.
        """
        pass

    def test_uninstall_plugin(self) -> None:
        """Test case for uninstall_plugin

        Uninstalls a plugin.
        """
        pass

    def test_uninstall_plugin_by_version(self) -> None:
        """Test case for uninstall_plugin_by_version

        Uninstalls a plugin by version.
        """
        pass

    def test_update_plugin_configuration(self) -> None:
        """Test case for update_plugin_configuration

        Updates plugin configuration.
        """
        pass


if __name__ == '__main__':
    unittest.main()
