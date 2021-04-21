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


class V1alpha1VirtualMachineSnapshotStatus(object):
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
        'conditions': 'list[V1alpha1Condition]',
        'creation_time': 'K8sIoApimachineryPkgApisMetaV1Time',
        'error': 'V1alpha1Error',
        'indications': 'list[str]',
        'ready_to_use': 'bool',
        'source_uid': 'str',
        'virtual_machine_snapshot_content_name': 'str'
    }

    attribute_map = {
        'conditions': 'conditions',
        'creation_time': 'creationTime',
        'error': 'error',
        'indications': 'indications',
        'ready_to_use': 'readyToUse',
        'source_uid': 'sourceUID',
        'virtual_machine_snapshot_content_name': 'virtualMachineSnapshotContentName'
    }

    def __init__(self, conditions=None, creation_time=None, error=None, indications=None, ready_to_use=None, source_uid=None, virtual_machine_snapshot_content_name=None):
        """
        V1alpha1VirtualMachineSnapshotStatus - a model defined in Swagger
        """

        self._conditions = None
        self._creation_time = None
        self._error = None
        self._indications = None
        self._ready_to_use = None
        self._source_uid = None
        self._virtual_machine_snapshot_content_name = None

        if conditions is not None:
          self.conditions = conditions
        if creation_time is not None:
          self.creation_time = creation_time
        if error is not None:
          self.error = error
        if indications is not None:
          self.indications = indications
        if ready_to_use is not None:
          self.ready_to_use = ready_to_use
        if source_uid is not None:
          self.source_uid = source_uid
        if virtual_machine_snapshot_content_name is not None:
          self.virtual_machine_snapshot_content_name = virtual_machine_snapshot_content_name

    @property
    def conditions(self):
        """
        Gets the conditions of this V1alpha1VirtualMachineSnapshotStatus.

        :return: The conditions of this V1alpha1VirtualMachineSnapshotStatus.
        :rtype: list[V1alpha1Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1alpha1VirtualMachineSnapshotStatus.

        :param conditions: The conditions of this V1alpha1VirtualMachineSnapshotStatus.
        :type: list[V1alpha1Condition]
        """

        self._conditions = conditions

    @property
    def creation_time(self):
        """
        Gets the creation_time of this V1alpha1VirtualMachineSnapshotStatus.

        :return: The creation_time of this V1alpha1VirtualMachineSnapshotStatus.
        :rtype: K8sIoApimachineryPkgApisMetaV1Time
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this V1alpha1VirtualMachineSnapshotStatus.

        :param creation_time: The creation_time of this V1alpha1VirtualMachineSnapshotStatus.
        :type: K8sIoApimachineryPkgApisMetaV1Time
        """

        self._creation_time = creation_time

    @property
    def error(self):
        """
        Gets the error of this V1alpha1VirtualMachineSnapshotStatus.

        :return: The error of this V1alpha1VirtualMachineSnapshotStatus.
        :rtype: V1alpha1Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this V1alpha1VirtualMachineSnapshotStatus.

        :param error: The error of this V1alpha1VirtualMachineSnapshotStatus.
        :type: V1alpha1Error
        """

        self._error = error

    @property
    def indications(self):
        """
        Gets the indications of this V1alpha1VirtualMachineSnapshotStatus.

        :return: The indications of this V1alpha1VirtualMachineSnapshotStatus.
        :rtype: list[str]
        """
        return self._indications

    @indications.setter
    def indications(self, indications):
        """
        Sets the indications of this V1alpha1VirtualMachineSnapshotStatus.

        :param indications: The indications of this V1alpha1VirtualMachineSnapshotStatus.
        :type: list[str]
        """

        self._indications = indications

    @property
    def ready_to_use(self):
        """
        Gets the ready_to_use of this V1alpha1VirtualMachineSnapshotStatus.

        :return: The ready_to_use of this V1alpha1VirtualMachineSnapshotStatus.
        :rtype: bool
        """
        return self._ready_to_use

    @ready_to_use.setter
    def ready_to_use(self, ready_to_use):
        """
        Sets the ready_to_use of this V1alpha1VirtualMachineSnapshotStatus.

        :param ready_to_use: The ready_to_use of this V1alpha1VirtualMachineSnapshotStatus.
        :type: bool
        """

        self._ready_to_use = ready_to_use

    @property
    def source_uid(self):
        """
        Gets the source_uid of this V1alpha1VirtualMachineSnapshotStatus.

        :return: The source_uid of this V1alpha1VirtualMachineSnapshotStatus.
        :rtype: str
        """
        return self._source_uid

    @source_uid.setter
    def source_uid(self, source_uid):
        """
        Sets the source_uid of this V1alpha1VirtualMachineSnapshotStatus.

        :param source_uid: The source_uid of this V1alpha1VirtualMachineSnapshotStatus.
        :type: str
        """

        self._source_uid = source_uid

    @property
    def virtual_machine_snapshot_content_name(self):
        """
        Gets the virtual_machine_snapshot_content_name of this V1alpha1VirtualMachineSnapshotStatus.

        :return: The virtual_machine_snapshot_content_name of this V1alpha1VirtualMachineSnapshotStatus.
        :rtype: str
        """
        return self._virtual_machine_snapshot_content_name

    @virtual_machine_snapshot_content_name.setter
    def virtual_machine_snapshot_content_name(self, virtual_machine_snapshot_content_name):
        """
        Sets the virtual_machine_snapshot_content_name of this V1alpha1VirtualMachineSnapshotStatus.

        :param virtual_machine_snapshot_content_name: The virtual_machine_snapshot_content_name of this V1alpha1VirtualMachineSnapshotStatus.
        :type: str
        """

        self._virtual_machine_snapshot_content_name = virtual_machine_snapshot_content_name

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
        if not isinstance(other, V1alpha1VirtualMachineSnapshotStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
