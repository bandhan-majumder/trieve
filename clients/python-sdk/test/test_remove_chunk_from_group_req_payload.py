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

from trieve_py_client.models.remove_chunk_from_group_req_payload import RemoveChunkFromGroupReqPayload

class TestRemoveChunkFromGroupReqPayload(unittest.TestCase):
    """RemoveChunkFromGroupReqPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemoveChunkFromGroupReqPayload:
        """Test RemoveChunkFromGroupReqPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RemoveChunkFromGroupReqPayload`
        """
        model = RemoveChunkFromGroupReqPayload()
        if include_optional:
            return RemoveChunkFromGroupReqPayload(
                chunk_id = ''
            )
        else:
            return RemoveChunkFromGroupReqPayload(
                chunk_id = '',
        )
        """

    def testRemoveChunkFromGroupReqPayload(self):
        """Test RemoveChunkFromGroupReqPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
