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


class V1Interface(object):
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
        'acpi_index': 'int',
        'boot_order': 'int',
        'bridge': 'V1InterfaceBridge',
        'dhcp_options': 'V1DHCPOptions',
        'mac_address': 'str',
        'macvtap': 'V1InterfaceMacvtap',
        'masquerade': 'V1InterfaceMasquerade',
        'model': 'str',
        'name': 'str',
        'passt': 'V1InterfacePasst',
        'pci_address': 'str',
        'ports': 'list[V1Port]',
        'slirp': 'V1InterfaceSlirp',
        'sriov': 'V1InterfaceSRIOV',
        'tag': 'str'
    }

    attribute_map = {
        'acpi_index': 'acpiIndex',
        'boot_order': 'bootOrder',
        'bridge': 'bridge',
        'dhcp_options': 'dhcpOptions',
        'mac_address': 'macAddress',
        'macvtap': 'macvtap',
        'masquerade': 'masquerade',
        'model': 'model',
        'name': 'name',
        'passt': 'passt',
        'pci_address': 'pciAddress',
        'ports': 'ports',
        'slirp': 'slirp',
        'sriov': 'sriov',
        'tag': 'tag'
    }

    def __init__(self, acpi_index=None, boot_order=None, bridge=None, dhcp_options=None, mac_address=None, macvtap=None, masquerade=None, model=None, name='', passt=None, pci_address=None, ports=None, slirp=None, sriov=None, tag=None):
        """
        V1Interface - a model defined in Swagger
        """

        self._acpi_index = None
        self._boot_order = None
        self._bridge = None
        self._dhcp_options = None
        self._mac_address = None
        self._macvtap = None
        self._masquerade = None
        self._model = None
        self._name = None
        self._passt = None
        self._pci_address = None
        self._ports = None
        self._slirp = None
        self._sriov = None
        self._tag = None

        if acpi_index is not None:
          self.acpi_index = acpi_index
        if boot_order is not None:
          self.boot_order = boot_order
        if bridge is not None:
          self.bridge = bridge
        if dhcp_options is not None:
          self.dhcp_options = dhcp_options
        if mac_address is not None:
          self.mac_address = mac_address
        if macvtap is not None:
          self.macvtap = macvtap
        if masquerade is not None:
          self.masquerade = masquerade
        if model is not None:
          self.model = model
        self.name = name
        if passt is not None:
          self.passt = passt
        if pci_address is not None:
          self.pci_address = pci_address
        if ports is not None:
          self.ports = ports
        if slirp is not None:
          self.slirp = slirp
        if sriov is not None:
          self.sriov = sriov
        if tag is not None:
          self.tag = tag

    @property
    def acpi_index(self):
        """
        Gets the acpi_index of this V1Interface.
        If specified, the ACPI index is used to provide network interface device naming, that is stable across changes in PCI addresses assigned to the device. This value is required to be unique across all devices and be between 1 and (16*1024-1).

        :return: The acpi_index of this V1Interface.
        :rtype: int
        """
        return self._acpi_index

    @acpi_index.setter
    def acpi_index(self, acpi_index):
        """
        Sets the acpi_index of this V1Interface.
        If specified, the ACPI index is used to provide network interface device naming, that is stable across changes in PCI addresses assigned to the device. This value is required to be unique across all devices and be between 1 and (16*1024-1).

        :param acpi_index: The acpi_index of this V1Interface.
        :type: int
        """

        self._acpi_index = acpi_index

    @property
    def boot_order(self):
        """
        Gets the boot_order of this V1Interface.
        BootOrder is an integer value > 0, used to determine ordering of boot devices. Lower values take precedence. Each interface or disk that has a boot order must have a unique value. Interfaces without a boot order are not tried.

        :return: The boot_order of this V1Interface.
        :rtype: int
        """
        return self._boot_order

    @boot_order.setter
    def boot_order(self, boot_order):
        """
        Sets the boot_order of this V1Interface.
        BootOrder is an integer value > 0, used to determine ordering of boot devices. Lower values take precedence. Each interface or disk that has a boot order must have a unique value. Interfaces without a boot order are not tried.

        :param boot_order: The boot_order of this V1Interface.
        :type: int
        """

        self._boot_order = boot_order

    @property
    def bridge(self):
        """
        Gets the bridge of this V1Interface.

        :return: The bridge of this V1Interface.
        :rtype: V1InterfaceBridge
        """
        return self._bridge

    @bridge.setter
    def bridge(self, bridge):
        """
        Sets the bridge of this V1Interface.

        :param bridge: The bridge of this V1Interface.
        :type: V1InterfaceBridge
        """

        self._bridge = bridge

    @property
    def dhcp_options(self):
        """
        Gets the dhcp_options of this V1Interface.
        If specified the network interface will pass additional DHCP options to the VMI

        :return: The dhcp_options of this V1Interface.
        :rtype: V1DHCPOptions
        """
        return self._dhcp_options

    @dhcp_options.setter
    def dhcp_options(self, dhcp_options):
        """
        Sets the dhcp_options of this V1Interface.
        If specified the network interface will pass additional DHCP options to the VMI

        :param dhcp_options: The dhcp_options of this V1Interface.
        :type: V1DHCPOptions
        """

        self._dhcp_options = dhcp_options

    @property
    def mac_address(self):
        """
        Gets the mac_address of this V1Interface.
        Interface MAC address. For example: de:ad:00:00:be:af or DE-AD-00-00-BE-AF.

        :return: The mac_address of this V1Interface.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this V1Interface.
        Interface MAC address. For example: de:ad:00:00:be:af or DE-AD-00-00-BE-AF.

        :param mac_address: The mac_address of this V1Interface.
        :type: str
        """

        self._mac_address = mac_address

    @property
    def macvtap(self):
        """
        Gets the macvtap of this V1Interface.

        :return: The macvtap of this V1Interface.
        :rtype: V1InterfaceMacvtap
        """
        return self._macvtap

    @macvtap.setter
    def macvtap(self, macvtap):
        """
        Sets the macvtap of this V1Interface.

        :param macvtap: The macvtap of this V1Interface.
        :type: V1InterfaceMacvtap
        """

        self._macvtap = macvtap

    @property
    def masquerade(self):
        """
        Gets the masquerade of this V1Interface.

        :return: The masquerade of this V1Interface.
        :rtype: V1InterfaceMasquerade
        """
        return self._masquerade

    @masquerade.setter
    def masquerade(self, masquerade):
        """
        Sets the masquerade of this V1Interface.

        :param masquerade: The masquerade of this V1Interface.
        :type: V1InterfaceMasquerade
        """

        self._masquerade = masquerade

    @property
    def model(self):
        """
        Gets the model of this V1Interface.
        Interface model. One of: e1000, e1000e, ne2k_pci, pcnet, rtl8139, virtio. Defaults to virtio.

        :return: The model of this V1Interface.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this V1Interface.
        Interface model. One of: e1000, e1000e, ne2k_pci, pcnet, rtl8139, virtio. Defaults to virtio.

        :param model: The model of this V1Interface.
        :type: str
        """

        self._model = model

    @property
    def name(self):
        """
        Gets the name of this V1Interface.
        Logical name of the interface as well as a reference to the associated networks. Must match the Name of a Network.

        :return: The name of this V1Interface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1Interface.
        Logical name of the interface as well as a reference to the associated networks. Must match the Name of a Network.

        :param name: The name of this V1Interface.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def passt(self):
        """
        Gets the passt of this V1Interface.

        :return: The passt of this V1Interface.
        :rtype: V1InterfacePasst
        """
        return self._passt

    @passt.setter
    def passt(self, passt):
        """
        Sets the passt of this V1Interface.

        :param passt: The passt of this V1Interface.
        :type: V1InterfacePasst
        """

        self._passt = passt

    @property
    def pci_address(self):
        """
        Gets the pci_address of this V1Interface.
        If specified, the virtual network interface will be placed on the guests pci address with the specified PCI address. For example: 0000:81:01.10

        :return: The pci_address of this V1Interface.
        :rtype: str
        """
        return self._pci_address

    @pci_address.setter
    def pci_address(self, pci_address):
        """
        Sets the pci_address of this V1Interface.
        If specified, the virtual network interface will be placed on the guests pci address with the specified PCI address. For example: 0000:81:01.10

        :param pci_address: The pci_address of this V1Interface.
        :type: str
        """

        self._pci_address = pci_address

    @property
    def ports(self):
        """
        Gets the ports of this V1Interface.
        List of ports to be forwarded to the virtual machine.

        :return: The ports of this V1Interface.
        :rtype: list[V1Port]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """
        Sets the ports of this V1Interface.
        List of ports to be forwarded to the virtual machine.

        :param ports: The ports of this V1Interface.
        :type: list[V1Port]
        """

        self._ports = ports

    @property
    def slirp(self):
        """
        Gets the slirp of this V1Interface.

        :return: The slirp of this V1Interface.
        :rtype: V1InterfaceSlirp
        """
        return self._slirp

    @slirp.setter
    def slirp(self, slirp):
        """
        Sets the slirp of this V1Interface.

        :param slirp: The slirp of this V1Interface.
        :type: V1InterfaceSlirp
        """

        self._slirp = slirp

    @property
    def sriov(self):
        """
        Gets the sriov of this V1Interface.

        :return: The sriov of this V1Interface.
        :rtype: V1InterfaceSRIOV
        """
        return self._sriov

    @sriov.setter
    def sriov(self, sriov):
        """
        Sets the sriov of this V1Interface.

        :param sriov: The sriov of this V1Interface.
        :type: V1InterfaceSRIOV
        """

        self._sriov = sriov

    @property
    def tag(self):
        """
        Gets the tag of this V1Interface.
        If specified, the virtual network interface address and its tag will be provided to the guest via config drive

        :return: The tag of this V1Interface.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this V1Interface.
        If specified, the virtual network interface address and its tag will be provided to the guest via config drive

        :param tag: The tag of this V1Interface.
        :type: str
        """

        self._tag = tag

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
        if not isinstance(other, V1Interface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
