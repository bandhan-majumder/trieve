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

from trieve_py_client.models.search_within_group_results import SearchWithinGroupResults

class TestSearchWithinGroupResults(unittest.TestCase):
    """SearchWithinGroupResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchWithinGroupResults:
        """Test SearchWithinGroupResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchWithinGroupResults`
        """
        model = SearchWithinGroupResults()
        if include_optional:
            return SearchWithinGroupResults(
                bookmarks = [
                    {"highlights":["highlight is two tokens: high, light","whereas hello is only one token: hello"],"metadata":[{"chunk_html":"<p>Some HTML content</p>","content":"Some content","id":"d290f1ee-6c54-4b01-90e6-d701748f0851","link":"https://example.com","metadata":{"key1":"value1","key2":"value2"},"time_stamp":"2021-01-01 00:00:00.000","weight":0.5}],"score":0.5}
                    ],
                corrected_query = '',
                group = {"created_at":"2021-01-01 00:00:00.000","dataset_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","description":"A group of chunks","file_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","name":"Trieve","tracking_id":"3","updated_at":"2021-01-01 00:00:00.000"},
                total_pages = 56
            )
        else:
            return SearchWithinGroupResults(
                bookmarks = [
                    {"highlights":["highlight is two tokens: high, light","whereas hello is only one token: hello"],"metadata":[{"chunk_html":"<p>Some HTML content</p>","content":"Some content","id":"d290f1ee-6c54-4b01-90e6-d701748f0851","link":"https://example.com","metadata":{"key1":"value1","key2":"value2"},"time_stamp":"2021-01-01 00:00:00.000","weight":0.5}],"score":0.5}
                    ],
                group = {"created_at":"2021-01-01 00:00:00.000","dataset_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","description":"A group of chunks","file_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","name":"Trieve","tracking_id":"3","updated_at":"2021-01-01 00:00:00.000"},
                total_pages = 56,
        )
        """

    def testSearchWithinGroupResults(self):
        """Test SearchWithinGroupResults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
