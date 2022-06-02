# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInfoController(BaseTestCase):
    """InfoController integration test stubs"""

    def test_get_info(self):
        """Test case for get_info

        Returns measurement data from an outlet.
        """
        response = self.client.open(
            '/v1/info/{alias}'.format(alias='alias_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
