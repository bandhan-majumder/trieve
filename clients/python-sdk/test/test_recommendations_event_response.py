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

from trieve_py_client.models.recommendations_event_response import RecommendationsEventResponse

class TestRecommendationsEventResponse(unittest.TestCase):
    """RecommendationsEventResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecommendationsEventResponse:
        """Test RecommendationsEventResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecommendationsEventResponse`
        """
        model = RecommendationsEventResponse()
        if include_optional:
            return RecommendationsEventResponse(
                queries = [
                    trieve_py_client.models.recommendation_event.RecommendationEvent(
                        created_at = '', 
                        dataset_id = '', 
                        id = '', 
                        negative_ids = [
                            ''
                            ], 
                        negative_tracking_ids = [
                            ''
                            ], 
                        positive_ids = [
                            ''
                            ], 
                        positive_tracking_ids = [
                            ''
                            ], 
                        recommendation_type = '', 
                        request_params = null, 
                        results = [
                            null
                            ], 
                        top_score = 1.337, 
                        user_id = '', )
                    ]
            )
        else:
            return RecommendationsEventResponse(
                queries = [
                    trieve_py_client.models.recommendation_event.RecommendationEvent(
                        created_at = '', 
                        dataset_id = '', 
                        id = '', 
                        negative_ids = [
                            ''
                            ], 
                        negative_tracking_ids = [
                            ''
                            ], 
                        positive_ids = [
                            ''
                            ], 
                        positive_tracking_ids = [
                            ''
                            ], 
                        recommendation_type = '', 
                        request_params = null, 
                        results = [
                            null
                            ], 
                        top_score = 1.337, 
                        user_id = '', )
                    ],
        )
        """

    def testRecommendationsEventResponse(self):
        """Test RecommendationsEventResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
