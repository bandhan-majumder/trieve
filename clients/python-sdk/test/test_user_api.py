# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.11.8
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_py_client.api.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()

    def tearDown(self) -> None:
        pass

    def test_delete_user_api_key(self) -> None:
        """Test case for delete_user_api_key

        Delete User Api Key
        """
        pass

    def test_set_user_api_key(self) -> None:
        """Test case for set_user_api_key

        Set User Api Key
        """
        pass

    def test_update_user(self) -> None:
        """Test case for update_user

        Update User
        """
        pass


if __name__ == '__main__':
    unittest.main()
