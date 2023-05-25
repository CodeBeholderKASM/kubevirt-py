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


class V1alpha2CPUInstancetype(object):
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
        'dedicated_cpu_placement': 'bool',
        'guest': 'int',
        'isolate_emulator_thread': 'bool',
        'model': 'str',
        'numa': 'V1NUMA',
        'realtime': 'V1Realtime'
    }

    attribute_map = {
        'dedicated_cpu_placement': 'dedicatedCPUPlacement',
        'guest': 'guest',
        'isolate_emulator_thread': 'isolateEmulatorThread',
        'model': 'model',
        'numa': 'numa',
        'realtime': 'realtime'
    }

    def __init__(self, dedicated_cpu_placement=None, guest=0, isolate_emulator_thread=None, model=None, numa=None, realtime=None):
        """
        V1alpha2CPUInstancetype - a model defined in Swagger
        """

        self._dedicated_cpu_placement = None
        self._guest = None
        self._isolate_emulator_thread = None
        self._model = None
        self._numa = None
        self._realtime = None

        if dedicated_cpu_placement is not None:
          self.dedicated_cpu_placement = dedicated_cpu_placement
        self.guest = guest
        if isolate_emulator_thread is not None:
          self.isolate_emulator_thread = isolate_emulator_thread
        if model is not None:
          self.model = model
        if numa is not None:
          self.numa = numa
        if realtime is not None:
          self.realtime = realtime

    @property
    def dedicated_cpu_placement(self):
        """
        Gets the dedicated_cpu_placement of this V1alpha2CPUInstancetype.
        DedicatedCPUPlacement requests the scheduler to place the VirtualMachineInstance on a node with enough dedicated pCPUs and pin the vCPUs to it.

        :return: The dedicated_cpu_placement of this V1alpha2CPUInstancetype.
        :rtype: bool
        """
        return self._dedicated_cpu_placement

    @dedicated_cpu_placement.setter
    def dedicated_cpu_placement(self, dedicated_cpu_placement):
        """
        Sets the dedicated_cpu_placement of this V1alpha2CPUInstancetype.
        DedicatedCPUPlacement requests the scheduler to place the VirtualMachineInstance on a node with enough dedicated pCPUs and pin the vCPUs to it.

        :param dedicated_cpu_placement: The dedicated_cpu_placement of this V1alpha2CPUInstancetype.
        :type: bool
        """

        self._dedicated_cpu_placement = dedicated_cpu_placement

    @property
    def guest(self):
        """
        Gets the guest of this V1alpha2CPUInstancetype.
        Required number of vCPUs to expose to the guest.  The resulting CPU topology being derived from the optional PreferredCPUTopology attribute of CPUPreferences that itself defaults to PreferCores.

        :return: The guest of this V1alpha2CPUInstancetype.
        :rtype: int
        """
        return self._guest

    @guest.setter
    def guest(self, guest):
        """
        Sets the guest of this V1alpha2CPUInstancetype.
        Required number of vCPUs to expose to the guest.  The resulting CPU topology being derived from the optional PreferredCPUTopology attribute of CPUPreferences that itself defaults to PreferCores.

        :param guest: The guest of this V1alpha2CPUInstancetype.
        :type: int
        """
        if guest is None:
            raise ValueError("Invalid value for `guest`, must not be `None`")

        self._guest = guest

    @property
    def isolate_emulator_thread(self):
        """
        Gets the isolate_emulator_thread of this V1alpha2CPUInstancetype.
        IsolateEmulatorThread requests one more dedicated pCPU to be allocated for the VMI to place the emulator thread on it.

        :return: The isolate_emulator_thread of this V1alpha2CPUInstancetype.
        :rtype: bool
        """
        return self._isolate_emulator_thread

    @isolate_emulator_thread.setter
    def isolate_emulator_thread(self, isolate_emulator_thread):
        """
        Sets the isolate_emulator_thread of this V1alpha2CPUInstancetype.
        IsolateEmulatorThread requests one more dedicated pCPU to be allocated for the VMI to place the emulator thread on it.

        :param isolate_emulator_thread: The isolate_emulator_thread of this V1alpha2CPUInstancetype.
        :type: bool
        """

        self._isolate_emulator_thread = isolate_emulator_thread

    @property
    def model(self):
        """
        Gets the model of this V1alpha2CPUInstancetype.
        Model specifies the CPU model inside the VMI. List of available models https://github.com/libvirt/libvirt/tree/master/src/cpu_map. It is possible to specify special cases like \"host-passthrough\" to get the same CPU as the node and \"host-model\" to get CPU closest to the node one. Defaults to host-model.

        :return: The model of this V1alpha2CPUInstancetype.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this V1alpha2CPUInstancetype.
        Model specifies the CPU model inside the VMI. List of available models https://github.com/libvirt/libvirt/tree/master/src/cpu_map. It is possible to specify special cases like \"host-passthrough\" to get the same CPU as the node and \"host-model\" to get CPU closest to the node one. Defaults to host-model.

        :param model: The model of this V1alpha2CPUInstancetype.
        :type: str
        """

        self._model = model

    @property
    def numa(self):
        """
        Gets the numa of this V1alpha2CPUInstancetype.
        NUMA allows specifying settings for the guest NUMA topology

        :return: The numa of this V1alpha2CPUInstancetype.
        :rtype: V1NUMA
        """
        return self._numa

    @numa.setter
    def numa(self, numa):
        """
        Sets the numa of this V1alpha2CPUInstancetype.
        NUMA allows specifying settings for the guest NUMA topology

        :param numa: The numa of this V1alpha2CPUInstancetype.
        :type: V1NUMA
        """

        self._numa = numa

    @property
    def realtime(self):
        """
        Gets the realtime of this V1alpha2CPUInstancetype.
        Realtime instructs the virt-launcher to tune the VMI for lower latency, optional for real time workloads

        :return: The realtime of this V1alpha2CPUInstancetype.
        :rtype: V1Realtime
        """
        return self._realtime

    @realtime.setter
    def realtime(self, realtime):
        """
        Sets the realtime of this V1alpha2CPUInstancetype.
        Realtime instructs the virt-launcher to tune the VMI for lower latency, optional for real time workloads

        :param realtime: The realtime of this V1alpha2CPUInstancetype.
        :type: V1Realtime
        """

        self._realtime = realtime

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
        if not isinstance(other, V1alpha2CPUInstancetype):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
