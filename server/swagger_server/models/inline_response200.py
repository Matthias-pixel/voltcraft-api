# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, current: int=None, frequency: int=None, active: bool=None, power: int=None, voltage: int=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param current: The current of this InlineResponse200.  # noqa: E501
        :type current: int
        :param frequency: The frequency of this InlineResponse200.  # noqa: E501
        :type frequency: int
        :param active: The active of this InlineResponse200.  # noqa: E501
        :type active: bool
        :param power: The power of this InlineResponse200.  # noqa: E501
        :type power: int
        :param voltage: The voltage of this InlineResponse200.  # noqa: E501
        :type voltage: int
        """
        self.swagger_types = {
            'current': int,
            'frequency': int,
            'active': bool,
            'power': int,
            'voltage': int
        }

        self.attribute_map = {
            'current': 'current',
            'frequency': 'frequency',
            'active': 'active',
            'power': 'power',
            'voltage': 'voltage'
        }
        self._current = current
        self._frequency = frequency
        self._active = active
        self._power = power
        self._voltage = voltage

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current(self) -> int:
        """Gets the current of this InlineResponse200.


        :return: The current of this InlineResponse200.
        :rtype: int
        """
        return self._current

    @current.setter
    def current(self, current: int):
        """Sets the current of this InlineResponse200.


        :param current: The current of this InlineResponse200.
        :type current: int
        """

        self._current = current

    @property
    def frequency(self) -> int:
        """Gets the frequency of this InlineResponse200.


        :return: The frequency of this InlineResponse200.
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency: int):
        """Sets the frequency of this InlineResponse200.


        :param frequency: The frequency of this InlineResponse200.
        :type frequency: int
        """

        self._frequency = frequency

    @property
    def active(self) -> bool:
        """Gets the active of this InlineResponse200.


        :return: The active of this InlineResponse200.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active: bool):
        """Sets the active of this InlineResponse200.


        :param active: The active of this InlineResponse200.
        :type active: bool
        """

        self._active = active

    @property
    def power(self) -> int:
        """Gets the power of this InlineResponse200.


        :return: The power of this InlineResponse200.
        :rtype: int
        """
        return self._power

    @power.setter
    def power(self, power: int):
        """Sets the power of this InlineResponse200.


        :param power: The power of this InlineResponse200.
        :type power: int
        """

        self._power = power

    @property
    def voltage(self) -> int:
        """Gets the voltage of this InlineResponse200.


        :return: The voltage of this InlineResponse200.
        :rtype: int
        """
        return self._voltage

    @voltage.setter
    def voltage(self, voltage: int):
        """Sets the voltage of this InlineResponse200.


        :param voltage: The voltage of this InlineResponse200.
        :type voltage: int
        """

        self._voltage = voltage