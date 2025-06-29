# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.scheduled_tasks_api import ScheduledTasksApi


class TestScheduledTasksApi(unittest.TestCase):
    """ScheduledTasksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ScheduledTasksApi()

    def tearDown(self) -> None:
        pass

    def test_get_task(self) -> None:
        """Test case for get_task

        Get task by id.
        """
        pass

    def test_get_tasks(self) -> None:
        """Test case for get_tasks

        Get tasks.
        """
        pass

    def test_start_task(self) -> None:
        """Test case for start_task

        Start specified task.
        """
        pass

    def test_stop_task(self) -> None:
        """Test case for stop_task

        Stop specified task.
        """
        pass

    def test_update_task(self) -> None:
        """Test case for update_task

        Update specified task triggers.
        """
        pass


if __name__ == '__main__':
    unittest.main()
