# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubevirt
from kubevirt.rest import ApiException
from kubevirt.apis.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """ DefaultApi unit test stubs """

    def setUp(self):
        self.api = kubevirt.apis.default_api.DefaultApi()

    def tearDown(self):
        pass

    def test_check_health(self):
        """
        Test case for check_health

        Health endpoint
        """
        pass

    def test_console(self):
        """
        Test case for console

        Open a websocket connection to a serial console on the specified VM.
        """
        pass

    def test_create_namespaced_offline_virtual_machine(self):
        """
        Test case for create_namespaced_offline_virtual_machine

        Create a OfflineVirtualMachine object.
        """
        pass

    def test_create_namespaced_virtual_machine(self):
        """
        Test case for create_namespaced_virtual_machine

        Create a VirtualMachine object.
        """
        pass

    def test_create_namespaced_virtual_machine_0(self):
        """
        Test case for create_namespaced_virtual_machine_0

        Create a VirtualMachine object.
        """
        pass

    def test_create_namespaced_virtual_machine_replica_set(self):
        """
        Test case for create_namespaced_virtual_machine_replica_set

        Create a VirtualMachineReplicaSet object.
        """
        pass

    def test_delete_collection_namespaced_offline_virtual_machine(self):
        """
        Test case for delete_collection_namespaced_offline_virtual_machine

        Delete a collection of OfflineVirtualMachine objects.
        """
        pass

    def test_delete_collection_namespaced_virtual_machine(self):
        """
        Test case for delete_collection_namespaced_virtual_machine

        Delete a collection of VirtualMachine objects.
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_0(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_0

        Delete a collection of VirtualMachine objects.
        """
        pass

    def test_delete_collection_namespaced_virtual_machine_replica_set(self):
        """
        Test case for delete_collection_namespaced_virtual_machine_replica_set

        Delete a collection of VirtualMachineReplicaSet objects.
        """
        pass

    def test_delete_namespaced_offline_virtual_machine(self):
        """
        Test case for delete_namespaced_offline_virtual_machine

        Delete a OfflineVirtualMachine object.
        """
        pass

    def test_delete_namespaced_virtual_machine(self):
        """
        Test case for delete_namespaced_virtual_machine

        Delete a VirtualMachine object.
        """
        pass

    def test_delete_namespaced_virtual_machine_0(self):
        """
        Test case for delete_namespaced_virtual_machine_0

        Delete a VirtualMachine object.
        """
        pass

    def test_delete_namespaced_virtual_machine_replica_set(self):
        """
        Test case for delete_namespaced_virtual_machine_replica_set

        Delete a VirtualMachineReplicaSet object.
        """
        pass

    def test_get_api_group(self):
        """
        Test case for get_api_group

        Get a KubeVirt API GroupList
        """
        pass

    def test_get_api_group_0(self):
        """
        Test case for get_api_group_0

        Get a KubeVirt API group
        """
        pass

    def test_get_api_group_1(self):
        """
        Test case for get_api_group_1

        Get a KubeVirt API Group
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        Get KubeVirt API Resources
        """
        pass

    def test_get_api_resources_0(self):
        """
        Test case for get_api_resources_0

        Get a KubeVirt API resources
        """
        pass

    def test_list_namespaced_offline_virtual_machine(self):
        """
        Test case for list_namespaced_offline_virtual_machine

        Get a list of OfflineVirtualMachine objects.
        """
        pass

    def test_list_namespaced_virtual_machine(self):
        """
        Test case for list_namespaced_virtual_machine

        Get a list of VirtualMachine objects.
        """
        pass

    def test_list_namespaced_virtual_machine_0(self):
        """
        Test case for list_namespaced_virtual_machine_0

        Get a list of VirtualMachine objects.
        """
        pass

    def test_list_namespaced_virtual_machine_replica_set(self):
        """
        Test case for list_namespaced_virtual_machine_replica_set

        Get a list of VirtualMachineReplicaSet objects.
        """
        pass

    def test_list_offline_virtual_machine_for_all_namespaces(self):
        """
        Test case for list_offline_virtual_machine_for_all_namespaces

        Get a list of all OfflineVirtualMachine objects.
        """
        pass

    def test_list_virtual_machine_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_for_all_namespaces

        Get a list of all VirtualMachine objects.
        """
        pass

    def test_list_virtual_machine_for_all_namespaces_0(self):
        """
        Test case for list_virtual_machine_for_all_namespaces_0

        Get a list of all VirtualMachine objects.
        """
        pass

    def test_list_virtual_machine_replica_set_for_all_namespaces(self):
        """
        Test case for list_virtual_machine_replica_set_for_all_namespaces

        Get a list of all VirtualMachineReplicaSet objects.
        """
        pass

    def test_patch_namespaced_offline_virtual_machine(self):
        """
        Test case for patch_namespaced_offline_virtual_machine

        Patch a OfflineVirtualMachine object.
        """
        pass

    def test_patch_namespaced_virtual_machine(self):
        """
        Test case for patch_namespaced_virtual_machine

        Patch a VirtualMachine object.
        """
        pass

    def test_patch_namespaced_virtual_machine_0(self):
        """
        Test case for patch_namespaced_virtual_machine_0

        Patch a VirtualMachine object.
        """
        pass

    def test_patch_namespaced_virtual_machine_replica_set(self):
        """
        Test case for patch_namespaced_virtual_machine_replica_set

        Patch a VirtualMachineReplicaSet object.
        """
        pass

    def test_read_namespaced_offline_virtual_machine(self):
        """
        Test case for read_namespaced_offline_virtual_machine

        Get a OfflineVirtualMachine object.
        """
        pass

    def test_read_namespaced_virtual_machine(self):
        """
        Test case for read_namespaced_virtual_machine

        Get a VirtualMachine object.
        """
        pass

    def test_read_namespaced_virtual_machine_0(self):
        """
        Test case for read_namespaced_virtual_machine_0

        Get a VirtualMachine object.
        """
        pass

    def test_read_namespaced_virtual_machine_replica_set(self):
        """
        Test case for read_namespaced_virtual_machine_replica_set

        Get a VirtualMachineReplicaSet object.
        """
        pass

    def test_replace_namespaced_offline_virtual_machine(self):
        """
        Test case for replace_namespaced_offline_virtual_machine

        Update a OfflineVirtualMachine object.
        """
        pass

    def test_replace_namespaced_virtual_machine(self):
        """
        Test case for replace_namespaced_virtual_machine

        Update a VirtualMachine object.
        """
        pass

    def test_replace_namespaced_virtual_machine_0(self):
        """
        Test case for replace_namespaced_virtual_machine_0

        Update a VirtualMachine object.
        """
        pass

    def test_replace_namespaced_virtual_machine_replica_set(self):
        """
        Test case for replace_namespaced_virtual_machine_replica_set

        Update a VirtualMachineReplicaSet object.
        """
        pass

    def test_test(self):
        """
        Test case for test

        Test endpoint verifying apiserver connectivity.
        """
        pass

    def test_vnc(self):
        """
        Test case for vnc

        Open a websocket connection to connect to VNC on the specified VM.
        """
        pass

    def test_watch_namespaced_offline_virtual_machine(self):
        """
        Test case for watch_namespaced_offline_virtual_machine

        Watch a OfflineVirtualMachine object.
        """
        pass

    def test_watch_namespaced_virtual_machine(self):
        """
        Test case for watch_namespaced_virtual_machine

        Watch a VirtualMachine object.
        """
        pass

    def test_watch_namespaced_virtual_machine_0(self):
        """
        Test case for watch_namespaced_virtual_machine_0

        Watch a VirtualMachine object.
        """
        pass

    def test_watch_namespaced_virtual_machine_replica_set(self):
        """
        Test case for watch_namespaced_virtual_machine_replica_set

        Watch a VirtualMachineReplicaSet object.
        """
        pass

    def test_watch_offline_virtual_machine_list_for_all_namespaces(self):
        """
        Test case for watch_offline_virtual_machine_list_for_all_namespaces

        Watch a OfflineVirtualMachineList object.
        """
        pass

    def test_watch_virtual_machine_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_list_for_all_namespaces

        Watch a VirtualMachineList object.
        """
        pass

    def test_watch_virtual_machine_list_for_all_namespaces_0(self):
        """
        Test case for watch_virtual_machine_list_for_all_namespaces_0

        Watch a VirtualMachineList object.
        """
        pass

    def test_watch_virtual_machine_replica_set_list_for_all_namespaces(self):
        """
        Test case for watch_virtual_machine_replica_set_list_for_all_namespaces

        Watch a VirtualMachineReplicaSetList object.
        """
        pass


if __name__ == '__main__':
    unittest.main()
