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


class K8sIoApiCoreV1PodAffinityTerm(object):
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
        'label_selector': 'K8sIoApimachineryPkgApisMetaV1LabelSelector',
        'namespace_selector': 'K8sIoApimachineryPkgApisMetaV1LabelSelector',
        'namespaces': 'list[str]',
        'topology_key': 'str'
    }

    attribute_map = {
        'label_selector': 'labelSelector',
        'namespace_selector': 'namespaceSelector',
        'namespaces': 'namespaces',
        'topology_key': 'topologyKey'
    }

    def __init__(self, label_selector=None, namespace_selector=None, namespaces=None, topology_key=''):
        """
        K8sIoApiCoreV1PodAffinityTerm - a model defined in Swagger
        """

        self._label_selector = None
        self._namespace_selector = None
        self._namespaces = None
        self._topology_key = None

        if label_selector is not None:
          self.label_selector = label_selector
        if namespace_selector is not None:
          self.namespace_selector = namespace_selector
        if namespaces is not None:
          self.namespaces = namespaces
        self.topology_key = topology_key

    @property
    def label_selector(self):
        """
        Gets the label_selector of this K8sIoApiCoreV1PodAffinityTerm.
        A label query over a set of resources, in this case pods.

        :return: The label_selector of this K8sIoApiCoreV1PodAffinityTerm.
        :rtype: K8sIoApimachineryPkgApisMetaV1LabelSelector
        """
        return self._label_selector

    @label_selector.setter
    def label_selector(self, label_selector):
        """
        Sets the label_selector of this K8sIoApiCoreV1PodAffinityTerm.
        A label query over a set of resources, in this case pods.

        :param label_selector: The label_selector of this K8sIoApiCoreV1PodAffinityTerm.
        :type: K8sIoApimachineryPkgApisMetaV1LabelSelector
        """

        self._label_selector = label_selector

    @property
    def namespace_selector(self):
        """
        Gets the namespace_selector of this K8sIoApiCoreV1PodAffinityTerm.
        A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means \"this pod's namespace\". An empty selector ({}) matches all namespaces.

        :return: The namespace_selector of this K8sIoApiCoreV1PodAffinityTerm.
        :rtype: K8sIoApimachineryPkgApisMetaV1LabelSelector
        """
        return self._namespace_selector

    @namespace_selector.setter
    def namespace_selector(self, namespace_selector):
        """
        Sets the namespace_selector of this K8sIoApiCoreV1PodAffinityTerm.
        A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means \"this pod's namespace\". An empty selector ({}) matches all namespaces.

        :param namespace_selector: The namespace_selector of this K8sIoApiCoreV1PodAffinityTerm.
        :type: K8sIoApimachineryPkgApisMetaV1LabelSelector
        """

        self._namespace_selector = namespace_selector

    @property
    def namespaces(self):
        """
        Gets the namespaces of this K8sIoApiCoreV1PodAffinityTerm.
        namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means \"this pod's namespace\".

        :return: The namespaces of this K8sIoApiCoreV1PodAffinityTerm.
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """
        Sets the namespaces of this K8sIoApiCoreV1PodAffinityTerm.
        namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means \"this pod's namespace\".

        :param namespaces: The namespaces of this K8sIoApiCoreV1PodAffinityTerm.
        :type: list[str]
        """

        self._namespaces = namespaces

    @property
    def topology_key(self):
        """
        Gets the topology_key of this K8sIoApiCoreV1PodAffinityTerm.
        This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.

        :return: The topology_key of this K8sIoApiCoreV1PodAffinityTerm.
        :rtype: str
        """
        return self._topology_key

    @topology_key.setter
    def topology_key(self, topology_key):
        """
        Sets the topology_key of this K8sIoApiCoreV1PodAffinityTerm.
        This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.

        :param topology_key: The topology_key of this K8sIoApiCoreV1PodAffinityTerm.
        :type: str
        """
        if topology_key is None:
            raise ValueError("Invalid value for `topology_key`, must not be `None`")

        self._topology_key = topology_key

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
        if not isinstance(other, K8sIoApiCoreV1PodAffinityTerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
