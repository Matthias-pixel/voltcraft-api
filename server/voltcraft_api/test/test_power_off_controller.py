# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from voltcraft_api.test import BaseTestCase


class TestPowerOffController(BaseTestCase):
    """PowerOffController integration test stubs"""

    def test_power_off(self):
        """Test case for power_off

        turns off an outlet.
        """
        response = self.client.open(
            '/v1/off/{alias}'.format(alias='alias_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
