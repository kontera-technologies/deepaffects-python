# coding: utf-8

"""
    SeerNet Audio APIs

    OpenAPI Specification of SeerNet audio APIs

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import deepaffects
from deepaffects.rest import ApiException
from deepaffects.apis.ellipsis_api import EllipsisApi


class TestEllipsisApi(unittest.TestCase):
    """ EllipsisApi unit test stubs """

    def setUp(self):
        self.api = deepaffects.apis.ellipsis_api.EllipsisApi()

    def tearDown(self):
        pass

    def test_is_depressed(self):
        """
        Test case for is_depressed

        Find if a person is depressed from audio.
        """
        pass


if __name__ == '__main__':
    unittest.main()
