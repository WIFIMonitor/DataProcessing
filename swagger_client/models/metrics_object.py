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


class MetricsObject(object):
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
        'metrics_data': 'MetricsObjectMetricsData'
    }

    attribute_map = {
        'metrics_data': 'metricsData'
    }

    def __init__(self, metrics_data=None):
        """
        MetricsObject - a model defined in Swagger
        """

        self._metrics_data = None

        if metrics_data is not None:
          self.metrics_data = metrics_data

    @property
    def metrics_data(self):
        """
        Gets the metrics_data of this MetricsObject.

        :return: The metrics_data of this MetricsObject.
        :rtype: MetricsObjectMetricsData
        """
        return self._metrics_data

    @metrics_data.setter
    def metrics_data(self, metrics_data):
        """
        Sets the metrics_data of this MetricsObject.

        :param metrics_data: The metrics_data of this MetricsObject.
        :type: MetricsObjectMetricsData
        """

        self._metrics_data = metrics_data

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
        if not isinstance(other, MetricsObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
