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


class V1alpha1VolumeSnapshotStatus(object):
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
        'creation_time': 'K8sIoApimachineryPkgApisMetaV1Time',
        'error': 'V1alpha1Error',
        'ready_to_use': 'bool',
        'volume_snapshot_name': 'str'
    }

    attribute_map = {
        'creation_time': 'creationTime',
        'error': 'error',
        'ready_to_use': 'readyToUse',
        'volume_snapshot_name': 'volumeSnapshotName'
    }

    def __init__(self, creation_time=None, error=None, ready_to_use=None, volume_snapshot_name=''):
        """
        V1alpha1VolumeSnapshotStatus - a model defined in Swagger
        """

        self._creation_time = None
        self._error = None
        self._ready_to_use = None
        self._volume_snapshot_name = None

        if creation_time is not None:
          self.creation_time = creation_time
        if error is not None:
          self.error = error
        if ready_to_use is not None:
          self.ready_to_use = ready_to_use
        self.volume_snapshot_name = volume_snapshot_name

    @property
    def creation_time(self):
        """
        Gets the creation_time of this V1alpha1VolumeSnapshotStatus.

        :return: The creation_time of this V1alpha1VolumeSnapshotStatus.
        :rtype: K8sIoApimachineryPkgApisMetaV1Time
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this V1alpha1VolumeSnapshotStatus.

        :param creation_time: The creation_time of this V1alpha1VolumeSnapshotStatus.
        :type: K8sIoApimachineryPkgApisMetaV1Time
        """

        self._creation_time = creation_time

    @property
    def error(self):
        """
        Gets the error of this V1alpha1VolumeSnapshotStatus.

        :return: The error of this V1alpha1VolumeSnapshotStatus.
        :rtype: V1alpha1Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this V1alpha1VolumeSnapshotStatus.

        :param error: The error of this V1alpha1VolumeSnapshotStatus.
        :type: V1alpha1Error
        """

        self._error = error

    @property
    def ready_to_use(self):
        """
        Gets the ready_to_use of this V1alpha1VolumeSnapshotStatus.

        :return: The ready_to_use of this V1alpha1VolumeSnapshotStatus.
        :rtype: bool
        """
        return self._ready_to_use

    @ready_to_use.setter
    def ready_to_use(self, ready_to_use):
        """
        Sets the ready_to_use of this V1alpha1VolumeSnapshotStatus.

        :param ready_to_use: The ready_to_use of this V1alpha1VolumeSnapshotStatus.
        :type: bool
        """

        self._ready_to_use = ready_to_use

    @property
    def volume_snapshot_name(self):
        """
        Gets the volume_snapshot_name of this V1alpha1VolumeSnapshotStatus.

        :return: The volume_snapshot_name of this V1alpha1VolumeSnapshotStatus.
        :rtype: str
        """
        return self._volume_snapshot_name

    @volume_snapshot_name.setter
    def volume_snapshot_name(self, volume_snapshot_name):
        """
        Sets the volume_snapshot_name of this V1alpha1VolumeSnapshotStatus.

        :param volume_snapshot_name: The volume_snapshot_name of this V1alpha1VolumeSnapshotStatus.
        :type: str
        """
        if volume_snapshot_name is None:
            raise ValueError("Invalid value for `volume_snapshot_name`, must not be `None`")

        self._volume_snapshot_name = volume_snapshot_name

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
        if not isinstance(other, V1alpha1VolumeSnapshotStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
