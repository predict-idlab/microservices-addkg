from argparse import ArgumentParser
import json
from kubernetes import config as K8sConfig, client as K8sClient

from litmus import ChaosClient
from litmus.faults.factory import FaultFactory, FaultType
from litmus.faults.fault import PodAutoscaler, PodNetworkLatency, PodCPUHog

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--endpoint", default="http://localhost:9002/query", help="ChaosCenter API Endpoint")
    parser.add_argument("--token", default="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjQ4NTc0NDM1NzksInJvbGUiOiJhZG1pbiIsInVpZCI6IjQwYzVjMTY3LTZlYTEtNGFiOC1hZGZhLThmMWUyN2U1YzBkMiIsInVzZXJuYW1lIjoiYWRtaW4ifQ.ioCAhS_dSUUiGhgnd_za7BvtYVDpvWrMeZpytcxAmBbeO86Lj-juOLNZWTWCAeaxExOZBuEYw4kpt8AgUbIbFQ", help="ChaosCenter API Token")
    parser.add_argument("--project-id", default="21ae8dde-f6d1-463b-b7b0-5e7a7af0c44a", help="ChaosCenter Project ID")
    parser.add_argument("--infra-id", default="89c5457a-e674-4669-b937-c4b462ec31ae", help="ChaosCenter Infrastructure ID")
    parser.add_argument("--output-file", default="results.json", help="Output file")

    args = parser.parse_args()

    client = ChaosClient(args.endpoint, args.token)

    fault_factory = FaultFactory()
    print([e for e in FaultType.__members__.values()])

    # results = []
    # for fault_type in FaultType.__members__.values():
    #     fault = fault_factory.get(fault_type)(app_namespace="onlineboutique")
    #     result = fault.execute(client, args.project_id, args.infra_id)
    #     results.append(result.__dict__())

    fault = PodAutoscaler(app_namespace="onlineboutique")
    result = fault.execute(client, args.project_id, args.infra_id)

    # K8sConfig.load_config()
    # k8s_client = K8sClient.CoreV1Api()
    #
    # result = k8s_client.list_namespaced_pod(label_selector="app=frontend", namespace="onlineboutique")
    # print(result)
