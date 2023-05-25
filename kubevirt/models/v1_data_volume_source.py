# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1DataVolumeSource(object):
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
        'hotpluggable': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'hotpluggable': 'hotpluggable',
        'name': 'name'
    }

    def __init__(self, hotpluggable=None, name=''):
        """
        V1DataVolumeSource - a model defined in Swagger
        """

        self._hotpluggable = None
        self._name = None

        if hotpluggable is not None:
          self.hotpluggable = hotpluggable
        self.name = name

    @property
    def hotpluggable(self):
        """
        Gets the hotpluggable of this V1DataVolumeSource.
        Hotpluggable indicates whether the volume can be hotplugged and hotunplugged.

        :return: The hotpluggable of this V1DataVolumeSource.
        :rtype: bool
        """
        return self._hotpluggable

    @hotpluggable.setter
    def hotpluggable(self, hotpluggable):
        """
        Sets the hotpluggable of this V1DataVolumeSource.
        Hotpluggable indicates whether the volume can be hotplugged and hotunplugged.

        :param hotpluggable: The hotpluggable of this V1DataVolumeSource.
        :type: bool
        """

        self._hotpluggable = hotpluggable

    @property
    def name(self):
        """
        Gets the name of this V1DataVolumeSource.
        Name of both the DataVolume and the PVC in the same namespace. After PVC population the DataVolume is garbage collected by default.

        :return: The name of this V1DataVolumeSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1DataVolumeSource.
        Name of both the DataVolume and the PVC in the same namespace. After PVC population the DataVolume is garbage collected by default.

        :param name: The name of this V1DataVolumeSource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

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
        if not isinstance(other, V1DataVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
