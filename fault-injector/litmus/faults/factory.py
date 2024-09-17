from enum import Enum

from litmus.faults.fault import NodeCPUHog, NodeDrain, NodeMemoryHog, PodAutoscaler, PodCPUHog, PodDelete, PodMemoryHog, \
    PodNetworkLatency


class FaultType(Enum):

    # Node faults
    NodeCPUHog = "node-cpu-hog"
    NodeDrain = "node-drain"
    NodeMemoryHog = "node-memory-hog"
    # Pod faults
    PodAutoscaler = "pod-autoscaler"
    PodCPUHog = "pod-cpu-hog"
    PodDelete = "pod-delete"
    # PodMemoryHog = "pod-memory-hog"
    PodNetworkLatency = "pod-network-latency"

    @classmethod
    def reverse_lookup(cls, value):
        """Reverse lookup."""
        for _, member in cls.__members__.items():
            if member.value == value:
                return member
        raise LookupError


class FaultFactory:

    _faults = {
        # Node Faults
        FaultType.NodeCPUHog: NodeCPUHog,
        FaultType.NodeDrain: NodeDrain,
        FaultType.NodeMemoryHog: NodeMemoryHog,
        # Pod Faults
        FaultType.PodAutoscaler: PodAutoscaler,
        FaultType.PodCPUHog: PodCPUHog,
        FaultType.PodDelete: PodDelete,
        # FaultType.PodMemoryHog: PodMemoryHog
        FaultType.PodNetworkLatency: PodNetworkLatency
    }

    def get(self, type_: FaultType) -> (str, str):
        return self._faults[type_]
