# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.outlet import Outlet  # noqa: E501
from swagger_server.test import BaseTestCase


class TestListController(BaseTestCase):
    """ListController integration test stubs"""

    def test_list_outlets(self):
        """Test case for list_outlets

        Returns a list of all outlets.
        """
        response = self.client.open(
            '/v1/list',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
