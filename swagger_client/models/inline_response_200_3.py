# coding: utf-8

"""
    primecore

    API Definition of primecore

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse2003(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'first': 'float',
        'last': 'float',
        'count': 'float',
        'rogue_access_point_alarms': 'list[RogueAccessPointAlarmObject]'
    }

    attribute_map = {
        'first': 'first',
        'last': 'last',
        'count': 'count',
        'rogue_access_point_alarms': 'rogueAccessPointAlarms'
    }

    def __init__(self, first=None, last=None, count=None, rogue_access_point_alarms=None):
        """
        InlineResponse2003 - a model defined in Swagger
        """

        self._first = None
        self._last = None
        self._count = None
        self._rogue_access_point_alarms = None

        if first is not None:
          self.first = first
        if last is not None:
          self.last = last
        if count is not None:
          self.count = count
        if rogue_access_point_alarms is not None:
          self.rogue_access_point_alarms = rogue_access_point_alarms

    @property
    def first(self):
        """
        Gets the first of this InlineResponse2003.

        :return: The first of this InlineResponse2003.
        :rtype: float
        """
        return self._first

    @first.setter
    def first(self, first):
        """
        Sets the first of this InlineResponse2003.

        :param first: The first of this InlineResponse2003.
        :type: float
        """

        self._first = first

    @property
    def last(self):
        """
        Gets the last of this InlineResponse2003.

        :return: The last of this InlineResponse2003.
        :rtype: float
        """
        return self._last

    @last.setter
    def last(self, last):
        """
        Sets the last of this InlineResponse2003.

        :param last: The last of this InlineResponse2003.
        :type: float
        """

        self._last = last

    @property
    def count(self):
        """
        Gets the count of this InlineResponse2003.

        :return: The count of this InlineResponse2003.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this InlineResponse2003.

        :param count: The count of this InlineResponse2003.
        :type: float
        """

        self._count = count

    @property
    def rogue_access_point_alarms(self):
        """
        Gets the rogue_access_point_alarms of this InlineResponse2003.

        :return: The rogue_access_point_alarms of this InlineResponse2003.
        :rtype: list[RogueAccessPointAlarmObject]
        """
        return self._rogue_access_point_alarms

    @rogue_access_point_alarms.setter
    def rogue_access_point_alarms(self, rogue_access_point_alarms):
        """
        Sets the rogue_access_point_alarms of this InlineResponse2003.

        :param rogue_access_point_alarms: The rogue_access_point_alarms of this InlineResponse2003.
        :type: list[RogueAccessPointAlarmObject]
        """

        self._rogue_access_point_alarms = rogue_access_point_alarms

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse2003):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
