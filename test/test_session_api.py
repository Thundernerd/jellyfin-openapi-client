# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.session_api import SessionApi


class TestSessionApi(unittest.TestCase):
    """SessionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SessionApi()

    def tearDown(self) -> None:
        pass

    def test_add_user_to_session(self) -> None:
        """Test case for add_user_to_session

        Adds an additional user to a session.
        """
        pass

    def test_display_content(self) -> None:
        """Test case for display_content

        Instructs a session to browse to an item or view.
        """
        pass

    def test_get_auth_providers(self) -> None:
        """Test case for get_auth_providers

        Get all auth providers.
        """
        pass

    def test_get_password_reset_providers(self) -> None:
        """Test case for get_password_reset_providers

        Get all password reset providers.
        """
        pass

    def test_get_sessions(self) -> None:
        """Test case for get_sessions

        Gets a list of sessions.
        """
        pass

    def test_play(self) -> None:
        """Test case for play

        Instructs a session to play an item.
        """
        pass

    def test_post_capabilities(self) -> None:
        """Test case for post_capabilities

        Updates capabilities for a device.
        """
        pass

    def test_post_full_capabilities(self) -> None:
        """Test case for post_full_capabilities

        Updates capabilities for a device.
        """
        pass

    def test_remove_user_from_session(self) -> None:
        """Test case for remove_user_from_session

        Removes an additional user from a session.
        """
        pass

    def test_report_session_ended(self) -> None:
        """Test case for report_session_ended

        Reports that a session has ended.
        """
        pass

    def test_report_viewing(self) -> None:
        """Test case for report_viewing

        Reports that a session is viewing an item.
        """
        pass

    def test_send_full_general_command(self) -> None:
        """Test case for send_full_general_command

        Issues a full general command to a client.
        """
        pass

    def test_send_general_command(self) -> None:
        """Test case for send_general_command

        Issues a general command to a client.
        """
        pass

    def test_send_message_command(self) -> None:
        """Test case for send_message_command

        Issues a command to a client to display a message to the user.
        """
        pass

    def test_send_playstate_command(self) -> None:
        """Test case for send_playstate_command

        Issues a playstate command to a client.
        """
        pass

    def test_send_system_command(self) -> None:
        """Test case for send_system_command

        Issues a system command to a client.
        """
        pass


if __name__ == '__main__':
    unittest.main()
