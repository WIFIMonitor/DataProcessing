# coding: utf-8

"""
    PRIMECORE_PRIMECORE-WS

    API Definition of primecore

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RogueAccessPointAlarmObjectRogueApAlarmDetails(object):
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
        'classification_type': 'str',
        'location': 'str',
        'rogue_clients': 'float',
        'rssi': 'float',
        'ssid': 'str',
        'state': 'str',
        'mac_address': 'str'
    }

    attribute_map = {
        'classification_type': 'classificationType',
        'location': 'location',
        'rogue_clients': 'rogueClients',
        'rssi': 'rssi',
        'ssid': 'ssid',
        'state': 'state',
        'mac_address': 'macAddress'
    }

    def __init__(self, classification_type=None, location=None, rogue_clients=None, rssi=None, ssid=None, state=None, mac_address=None):
        """
        RogueAccessPointAlarmObjectRogueApAlarmDetails - a model defined in Swagger
        """

        self._classification_type = None
        self._location = None
        self._rogue_clients = None
        self._rssi = None
        self._ssid = None
        self._state = None
        self._mac_address = None

        if classification_type is not None:
          self.classification_type = classification_type
        if location is not None:
          self.location = location
        if rogue_clients is not None:
          self.rogue_clients = rogue_clients
        if rssi is not None:
          self.rssi = rssi
        if ssid is not None:
          self.ssid = ssid
        if state is not None:
          self.state = state
        if mac_address is not None:
          self.mac_address = mac_address

    @property
    def classification_type(self):
        """
        Gets the classification_type of this RogueAccessPointAlarmObjectRogueApAlarmDetails.

        :return: The classification_type of this RogueAccessPointAlarmObjectRogueApAlarmDetails.
        :rtype: str
        """
        return self._classification_type

    @classification_type.setter
    def classification_type(self, classification_type):
        """
        Sets the classification_type of this RogueAccessPointAlarmObjectRogueApAlarmDetails.

        :param classification_type: The classification_type of this RogueAccessPointAlarmObjectRogueApAlarmDetails.
        :type: str
        """
        allowed_values = ["FRIENDLY", "MALICIOUS", "UNCLASSIFIED", "CUSTOM"]
        if classification_type not in allowed_values:
            raise ValueError(
                "Invalid value for `classification_type` ({0}), must be one of {1}"
                .format(classification_type, allowed_values)
            )

        self._classification_type = classification_type

    @property
    def location(self):
        """
        Gets the location of this RogueAccessPointAlarmObjectRogueApAlarmDetails.

        :return: The location of this RogueAccessPointAlarmObjectRogueApAlarmDetails.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this RogueAccessPointAlarmObjectRogueApAlarmDetails.

        :param location: The location of this RogueAccessPointAlarmObjectRogueApAlarmDetails.
        :type: str
        """

        self._location = location

    @property
    def rogue_clients(self):
        """
        Gets the rogue_clients of this RogueAccessPointAlarmObjectRogueApAlarmDetails.

        :return: The rogue_clients of this RogueAccessPointAlarmObjectRogueApAlarmDetails.
        :rtype: float
        """
        return self._rogue_clients

    @rogue_clients.setter
    def rogue_clients(self, rogue_clients):
        """
        Sets the rogue_clients of this RogueAccessPointAlarmObjectRogueApAlarmDetails.

        :param rogue_clients: The rogue_clients of this RogueAccessPointAlarmObjectRogueApAlarmDetails.
        :type: float
        """

        self._rogue_clients = rogue_clients

    @property
    def rssi(self):
        """
        Gets the rssi of this RogueAccessPointAlarmObjectRogueApAlarmDetails.

        :return: The rssi of this RogueAccessPointAlarmObjectRogueApAlarmDetails.
        :rtype: float
        """
        return self._rssi

    @rssi.setter
    def rssi(self, rssi):
        """
        Sets the rssi of this RogueAccessPointAlarmObjectRogueApAlarmDetails.

        :param rssi: The rssi of this RogueAccessPointAlarmObjectRogueApAlarmDetails.
        :type: float
        """

        self._rssi = rssi

    @property
    def ssid(self):
        """
        Gets the ssid of this RogueAccessPointAlarmObjectRogueApAlarmDetails.

        :return: The ssid of this RogueAccessPointAlarmObjectRogueApAlarmDetails.
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """
        Sets the ssid of this RogueAccessPointAlarmObjectRogueApAlarmDetails.

        :param ssid: The ssid of this RogueAccessPointAlarmObjectRogueApAlarmDetails.
        :type: str
        """

        self._ssid = ssid

    @property
    def state(self):
        """
        Gets the state of this RogueAccessPointAlarmObjectRogueApAlarmDetails.

        :return: The state of this RogueAccessPointAlarmObjectRogueApAlarmDetails.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this RogueAccessPointAlarmObjectRogueApAlarmDetails.

        :param state: The state of this RogueAccessPointAlarmObjectRogueApAlarmDetails.
        :type: str
        """
        allowed_values = ["INITIALIZING", "PENDING", "ALERT", "AIRESPACE_AP", "KNOWN", "ACKNOWLEDGED", "CONTAINED", "THREAT", "CONTAINED_PENDING", "KNOWN_CONTAINED", "TRUSTED_MISSING", "REMOVED", "WIRE_CONTAINED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def mac_address(self):
        """
        Gets the mac_address of this RogueAccessPointAlarmObjectRogueApAlarmDetails.

        :return: The mac_address of this RogueAccessPointAlarmObjectRogueApAlarmDetails.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this RogueAccessPointAlarmObjectRogueApAlarmDetails.

        :param mac_address: The mac_address of this RogueAccessPointAlarmObjectRogueApAlarmDetails.
        :type: str
        """

        self._mac_address = mac_address

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
        if not isinstance(other, RogueAccessPointAlarmObjectRogueApAlarmDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
