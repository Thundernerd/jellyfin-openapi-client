# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.task_result import TaskResult

class TestTaskResult(unittest.TestCase):
    """TaskResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskResult:
        """Test TaskResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskResult`
        """
        model = TaskResult()
        if include_optional:
            return TaskResult(
                start_time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                end_time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'Completed',
                name = '',
                key = '',
                id = '',
                error_message = '',
                long_error_message = ''
            )
        else:
            return TaskResult(
        )
        """

    def testTaskResult(self):
        """Test TaskResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
