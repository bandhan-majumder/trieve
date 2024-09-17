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

from trieve_py_client.models.low_confidence_recommendations import LowConfidenceRecommendations

class TestLowConfidenceRecommendations(unittest.TestCase):
    """LowConfidenceRecommendations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LowConfidenceRecommendations:
        """Test LowConfidenceRecommendations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LowConfidenceRecommendations`
        """
        model = LowConfidenceRecommendations()
        if include_optional:
            return LowConfidenceRecommendations(
                filter = trieve_py_client.models.recommendation_analytics_filter.RecommendationAnalyticsFilter(
                    date_range = null, 
                    recommendation_type = null, ),
                page = 0,
                threshold = 1.337,
                type = 'low_confidence_recommendations'
            )
        else:
            return LowConfidenceRecommendations(
                type = 'low_confidence_recommendations',
        )
        """

    def testLowConfidenceRecommendations(self):
        """Test LowConfidenceRecommendations"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
