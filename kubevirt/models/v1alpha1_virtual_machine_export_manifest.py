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


class V1alpha1VirtualMachineExportManifest(object):
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
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, type='', url=''):
        """
        V1alpha1VirtualMachineExportManifest - a model defined in Swagger
        """

        self._type = None
        self._url = None

        self.type = type
        self.url = url

    @property
    def type(self):
        """
        Gets the type of this V1alpha1VirtualMachineExportManifest.
        Type is the type of manifest returned

        :return: The type of this V1alpha1VirtualMachineExportManifest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1alpha1VirtualMachineExportManifest.
        Type is the type of manifest returned

        :param type: The type of this V1alpha1VirtualMachineExportManifest.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def url(self):
        """
        Gets the url of this V1alpha1VirtualMachineExportManifest.
        Url is the url of the endpoint that returns the manifest

        :return: The url of this V1alpha1VirtualMachineExportManifest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this V1alpha1VirtualMachineExportManifest.
        Url is the url of the endpoint that returns the manifest

        :param url: The url of this V1alpha1VirtualMachineExportManifest.
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url

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
        if not isinstance(other, V1alpha1VirtualMachineExportManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
