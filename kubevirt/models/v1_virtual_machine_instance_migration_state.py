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


class V1VirtualMachineInstanceMigrationState(object):
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
        'abort_requested': 'bool',
        'abort_status': 'str',
        'completed': 'bool',
        'end_timestamp': 'K8sIoApimachineryPkgApisMetaV1Time',
        'failed': 'bool',
        'migration_configuration': 'V1MigrationConfiguration',
        'migration_policy_name': 'str',
        'migration_uid': 'str',
        'mode': 'str',
        'source_node': 'str',
        'start_timestamp': 'K8sIoApimachineryPkgApisMetaV1Time',
        'target_attachment_pod_uid': 'str',
        'target_cpu_set': 'list[int]',
        'target_direct_migration_node_ports': 'dict(str, int)',
        'target_node': 'str',
        'target_node_address': 'str',
        'target_node_domain_detected': 'bool',
        'target_node_domain_ready_timestamp': 'K8sIoApimachineryPkgApisMetaV1Time',
        'target_node_topology': 'str',
        'target_pod': 'str'
    }

    attribute_map = {
        'abort_requested': 'abortRequested',
        'abort_status': 'abortStatus',
        'completed': 'completed',
        'end_timestamp': 'endTimestamp',
        'failed': 'failed',
        'migration_configuration': 'migrationConfiguration',
        'migration_policy_name': 'migrationPolicyName',
        'migration_uid': 'migrationUid',
        'mode': 'mode',
        'source_node': 'sourceNode',
        'start_timestamp': 'startTimestamp',
        'target_attachment_pod_uid': 'targetAttachmentPodUID',
        'target_cpu_set': 'targetCPUSet',
        'target_direct_migration_node_ports': 'targetDirectMigrationNodePorts',
        'target_node': 'targetNode',
        'target_node_address': 'targetNodeAddress',
        'target_node_domain_detected': 'targetNodeDomainDetected',
        'target_node_domain_ready_timestamp': 'targetNodeDomainReadyTimestamp',
        'target_node_topology': 'targetNodeTopology',
        'target_pod': 'targetPod'
    }

    def __init__(self, abort_requested=None, abort_status=None, completed=None, end_timestamp=None, failed=None, migration_configuration=None, migration_policy_name=None, migration_uid=None, mode=None, source_node=None, start_timestamp=None, target_attachment_pod_uid=None, target_cpu_set=None, target_direct_migration_node_ports=None, target_node=None, target_node_address=None, target_node_domain_detected=None, target_node_domain_ready_timestamp=None, target_node_topology=None, target_pod=None):
        """
        V1VirtualMachineInstanceMigrationState - a model defined in Swagger
        """

        self._abort_requested = None
        self._abort_status = None
        self._completed = None
        self._end_timestamp = None
        self._failed = None
        self._migration_configuration = None
        self._migration_policy_name = None
        self._migration_uid = None
        self._mode = None
        self._source_node = None
        self._start_timestamp = None
        self._target_attachment_pod_uid = None
        self._target_cpu_set = None
        self._target_direct_migration_node_ports = None
        self._target_node = None
        self._target_node_address = None
        self._target_node_domain_detected = None
        self._target_node_domain_ready_timestamp = None
        self._target_node_topology = None
        self._target_pod = None

        if abort_requested is not None:
          self.abort_requested = abort_requested
        if abort_status is not None:
          self.abort_status = abort_status
        if completed is not None:
          self.completed = completed
        if end_timestamp is not None:
          self.end_timestamp = end_timestamp
        if failed is not None:
          self.failed = failed
        if migration_configuration is not None:
          self.migration_configuration = migration_configuration
        if migration_policy_name is not None:
          self.migration_policy_name = migration_policy_name
        if migration_uid is not None:
          self.migration_uid = migration_uid
        if mode is not None:
          self.mode = mode
        if source_node is not None:
          self.source_node = source_node
        if start_timestamp is not None:
          self.start_timestamp = start_timestamp
        if target_attachment_pod_uid is not None:
          self.target_attachment_pod_uid = target_attachment_pod_uid
        if target_cpu_set is not None:
          self.target_cpu_set = target_cpu_set
        if target_direct_migration_node_ports is not None:
          self.target_direct_migration_node_ports = target_direct_migration_node_ports
        if target_node is not None:
          self.target_node = target_node
        if target_node_address is not None:
          self.target_node_address = target_node_address
        if target_node_domain_detected is not None:
          self.target_node_domain_detected = target_node_domain_detected
        if target_node_domain_ready_timestamp is not None:
          self.target_node_domain_ready_timestamp = target_node_domain_ready_timestamp
        if target_node_topology is not None:
          self.target_node_topology = target_node_topology
        if target_pod is not None:
          self.target_pod = target_pod

    @property
    def abort_requested(self):
        """
        Gets the abort_requested of this V1VirtualMachineInstanceMigrationState.
        Indicates that the migration has been requested to abort

        :return: The abort_requested of this V1VirtualMachineInstanceMigrationState.
        :rtype: bool
        """
        return self._abort_requested

    @abort_requested.setter
    def abort_requested(self, abort_requested):
        """
        Sets the abort_requested of this V1VirtualMachineInstanceMigrationState.
        Indicates that the migration has been requested to abort

        :param abort_requested: The abort_requested of this V1VirtualMachineInstanceMigrationState.
        :type: bool
        """

        self._abort_requested = abort_requested

    @property
    def abort_status(self):
        """
        Gets the abort_status of this V1VirtualMachineInstanceMigrationState.
        Indicates the final status of the live migration abortion

        :return: The abort_status of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._abort_status

    @abort_status.setter
    def abort_status(self, abort_status):
        """
        Sets the abort_status of this V1VirtualMachineInstanceMigrationState.
        Indicates the final status of the live migration abortion

        :param abort_status: The abort_status of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._abort_status = abort_status

    @property
    def completed(self):
        """
        Gets the completed of this V1VirtualMachineInstanceMigrationState.
        Indicates the migration completed

        :return: The completed of this V1VirtualMachineInstanceMigrationState.
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """
        Sets the completed of this V1VirtualMachineInstanceMigrationState.
        Indicates the migration completed

        :param completed: The completed of this V1VirtualMachineInstanceMigrationState.
        :type: bool
        """

        self._completed = completed

    @property
    def end_timestamp(self):
        """
        Gets the end_timestamp of this V1VirtualMachineInstanceMigrationState.
        The time the migration action ended

        :return: The end_timestamp of this V1VirtualMachineInstanceMigrationState.
        :rtype: K8sIoApimachineryPkgApisMetaV1Time
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """
        Sets the end_timestamp of this V1VirtualMachineInstanceMigrationState.
        The time the migration action ended

        :param end_timestamp: The end_timestamp of this V1VirtualMachineInstanceMigrationState.
        :type: K8sIoApimachineryPkgApisMetaV1Time
        """

        self._end_timestamp = end_timestamp

    @property
    def failed(self):
        """
        Gets the failed of this V1VirtualMachineInstanceMigrationState.
        Indicates that the migration failed

        :return: The failed of this V1VirtualMachineInstanceMigrationState.
        :rtype: bool
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """
        Sets the failed of this V1VirtualMachineInstanceMigrationState.
        Indicates that the migration failed

        :param failed: The failed of this V1VirtualMachineInstanceMigrationState.
        :type: bool
        """

        self._failed = failed

    @property
    def migration_configuration(self):
        """
        Gets the migration_configuration of this V1VirtualMachineInstanceMigrationState.
        Migration configurations to apply

        :return: The migration_configuration of this V1VirtualMachineInstanceMigrationState.
        :rtype: V1MigrationConfiguration
        """
        return self._migration_configuration

    @migration_configuration.setter
    def migration_configuration(self, migration_configuration):
        """
        Sets the migration_configuration of this V1VirtualMachineInstanceMigrationState.
        Migration configurations to apply

        :param migration_configuration: The migration_configuration of this V1VirtualMachineInstanceMigrationState.
        :type: V1MigrationConfiguration
        """

        self._migration_configuration = migration_configuration

    @property
    def migration_policy_name(self):
        """
        Gets the migration_policy_name of this V1VirtualMachineInstanceMigrationState.
        Name of the migration policy. If string is empty, no policy is matched

        :return: The migration_policy_name of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._migration_policy_name

    @migration_policy_name.setter
    def migration_policy_name(self, migration_policy_name):
        """
        Sets the migration_policy_name of this V1VirtualMachineInstanceMigrationState.
        Name of the migration policy. If string is empty, no policy is matched

        :param migration_policy_name: The migration_policy_name of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._migration_policy_name = migration_policy_name

    @property
    def migration_uid(self):
        """
        Gets the migration_uid of this V1VirtualMachineInstanceMigrationState.
        The VirtualMachineInstanceMigration object associated with this migration

        :return: The migration_uid of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._migration_uid

    @migration_uid.setter
    def migration_uid(self, migration_uid):
        """
        Sets the migration_uid of this V1VirtualMachineInstanceMigrationState.
        The VirtualMachineInstanceMigration object associated with this migration

        :param migration_uid: The migration_uid of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._migration_uid = migration_uid

    @property
    def mode(self):
        """
        Gets the mode of this V1VirtualMachineInstanceMigrationState.
        Lets us know if the vmi is currently running pre or post copy migration

        :return: The mode of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this V1VirtualMachineInstanceMigrationState.
        Lets us know if the vmi is currently running pre or post copy migration

        :param mode: The mode of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._mode = mode

    @property
    def source_node(self):
        """
        Gets the source_node of this V1VirtualMachineInstanceMigrationState.
        The source node that the VMI originated on

        :return: The source_node of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._source_node

    @source_node.setter
    def source_node(self, source_node):
        """
        Sets the source_node of this V1VirtualMachineInstanceMigrationState.
        The source node that the VMI originated on

        :param source_node: The source_node of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._source_node = source_node

    @property
    def start_timestamp(self):
        """
        Gets the start_timestamp of this V1VirtualMachineInstanceMigrationState.
        The time the migration action began

        :return: The start_timestamp of this V1VirtualMachineInstanceMigrationState.
        :rtype: K8sIoApimachineryPkgApisMetaV1Time
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """
        Sets the start_timestamp of this V1VirtualMachineInstanceMigrationState.
        The time the migration action began

        :param start_timestamp: The start_timestamp of this V1VirtualMachineInstanceMigrationState.
        :type: K8sIoApimachineryPkgApisMetaV1Time
        """

        self._start_timestamp = start_timestamp

    @property
    def target_attachment_pod_uid(self):
        """
        Gets the target_attachment_pod_uid of this V1VirtualMachineInstanceMigrationState.
        The UID of the target attachment pod for hotplug volumes

        :return: The target_attachment_pod_uid of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._target_attachment_pod_uid

    @target_attachment_pod_uid.setter
    def target_attachment_pod_uid(self, target_attachment_pod_uid):
        """
        Sets the target_attachment_pod_uid of this V1VirtualMachineInstanceMigrationState.
        The UID of the target attachment pod for hotplug volumes

        :param target_attachment_pod_uid: The target_attachment_pod_uid of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._target_attachment_pod_uid = target_attachment_pod_uid

    @property
    def target_cpu_set(self):
        """
        Gets the target_cpu_set of this V1VirtualMachineInstanceMigrationState.
        If the VMI requires dedicated CPUs, this field will hold the dedicated CPU set on the target node

        :return: The target_cpu_set of this V1VirtualMachineInstanceMigrationState.
        :rtype: list[int]
        """
        return self._target_cpu_set

    @target_cpu_set.setter
    def target_cpu_set(self, target_cpu_set):
        """
        Sets the target_cpu_set of this V1VirtualMachineInstanceMigrationState.
        If the VMI requires dedicated CPUs, this field will hold the dedicated CPU set on the target node

        :param target_cpu_set: The target_cpu_set of this V1VirtualMachineInstanceMigrationState.
        :type: list[int]
        """

        self._target_cpu_set = target_cpu_set

    @property
    def target_direct_migration_node_ports(self):
        """
        Gets the target_direct_migration_node_ports of this V1VirtualMachineInstanceMigrationState.
        The list of ports opened for live migration on the destination node

        :return: The target_direct_migration_node_ports of this V1VirtualMachineInstanceMigrationState.
        :rtype: dict(str, int)
        """
        return self._target_direct_migration_node_ports

    @target_direct_migration_node_ports.setter
    def target_direct_migration_node_ports(self, target_direct_migration_node_ports):
        """
        Sets the target_direct_migration_node_ports of this V1VirtualMachineInstanceMigrationState.
        The list of ports opened for live migration on the destination node

        :param target_direct_migration_node_ports: The target_direct_migration_node_ports of this V1VirtualMachineInstanceMigrationState.
        :type: dict(str, int)
        """

        self._target_direct_migration_node_ports = target_direct_migration_node_ports

    @property
    def target_node(self):
        """
        Gets the target_node of this V1VirtualMachineInstanceMigrationState.
        The target node that the VMI is moving to

        :return: The target_node of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._target_node

    @target_node.setter
    def target_node(self, target_node):
        """
        Sets the target_node of this V1VirtualMachineInstanceMigrationState.
        The target node that the VMI is moving to

        :param target_node: The target_node of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._target_node = target_node

    @property
    def target_node_address(self):
        """
        Gets the target_node_address of this V1VirtualMachineInstanceMigrationState.
        The address of the target node to use for the migration

        :return: The target_node_address of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._target_node_address

    @target_node_address.setter
    def target_node_address(self, target_node_address):
        """
        Sets the target_node_address of this V1VirtualMachineInstanceMigrationState.
        The address of the target node to use for the migration

        :param target_node_address: The target_node_address of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._target_node_address = target_node_address

    @property
    def target_node_domain_detected(self):
        """
        Gets the target_node_domain_detected of this V1VirtualMachineInstanceMigrationState.
        The Target Node has seen the Domain Start Event

        :return: The target_node_domain_detected of this V1VirtualMachineInstanceMigrationState.
        :rtype: bool
        """
        return self._target_node_domain_detected

    @target_node_domain_detected.setter
    def target_node_domain_detected(self, target_node_domain_detected):
        """
        Sets the target_node_domain_detected of this V1VirtualMachineInstanceMigrationState.
        The Target Node has seen the Domain Start Event

        :param target_node_domain_detected: The target_node_domain_detected of this V1VirtualMachineInstanceMigrationState.
        :type: bool
        """

        self._target_node_domain_detected = target_node_domain_detected

    @property
    def target_node_domain_ready_timestamp(self):
        """
        Gets the target_node_domain_ready_timestamp of this V1VirtualMachineInstanceMigrationState.
        The timestamp at which the target node detects the domain is active

        :return: The target_node_domain_ready_timestamp of this V1VirtualMachineInstanceMigrationState.
        :rtype: K8sIoApimachineryPkgApisMetaV1Time
        """
        return self._target_node_domain_ready_timestamp

    @target_node_domain_ready_timestamp.setter
    def target_node_domain_ready_timestamp(self, target_node_domain_ready_timestamp):
        """
        Sets the target_node_domain_ready_timestamp of this V1VirtualMachineInstanceMigrationState.
        The timestamp at which the target node detects the domain is active

        :param target_node_domain_ready_timestamp: The target_node_domain_ready_timestamp of this V1VirtualMachineInstanceMigrationState.
        :type: K8sIoApimachineryPkgApisMetaV1Time
        """

        self._target_node_domain_ready_timestamp = target_node_domain_ready_timestamp

    @property
    def target_node_topology(self):
        """
        Gets the target_node_topology of this V1VirtualMachineInstanceMigrationState.
        If the VMI requires dedicated CPUs, this field will hold the numa topology on the target node

        :return: The target_node_topology of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._target_node_topology

    @target_node_topology.setter
    def target_node_topology(self, target_node_topology):
        """
        Sets the target_node_topology of this V1VirtualMachineInstanceMigrationState.
        If the VMI requires dedicated CPUs, this field will hold the numa topology on the target node

        :param target_node_topology: The target_node_topology of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._target_node_topology = target_node_topology

    @property
    def target_pod(self):
        """
        Gets the target_pod of this V1VirtualMachineInstanceMigrationState.
        The target pod that the VMI is moving to

        :return: The target_pod of this V1VirtualMachineInstanceMigrationState.
        :rtype: str
        """
        return self._target_pod

    @target_pod.setter
    def target_pod(self, target_pod):
        """
        Sets the target_pod of this V1VirtualMachineInstanceMigrationState.
        The target pod that the VMI is moving to

        :param target_pod: The target_pod of this V1VirtualMachineInstanceMigrationState.
        :type: str
        """

        self._target_pod = target_pod

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
        if not isinstance(other, V1VirtualMachineInstanceMigrationState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
