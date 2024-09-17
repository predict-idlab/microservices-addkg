import json
from argparse import ArgumentParser

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--endpoint", default="http://localhost:9002/query", help="Litmus API Endpoint")
    parser.add_argument("--token", default="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjQ4NTc0NDM1NzksInJvbGUiOiJhZG1pbiIsInVpZCI6IjQwYzVjMTY3LTZlYTEtNGFiOC1hZGZhLThmMWUyN2U1YzBkMiIsInVzZXJuYW1lIjoiYWRtaW4ifQ.ioCAhS_dSUUiGhgnd_za7BvtYVDpvWrMeZpytcxAmBbeO86Lj-juOLNZWTWCAeaxExOZBuEYw4kpt8AgUbIbFQ", help="Litmus API Token")

    args = parser.parse_args()

    transport = AIOHTTPTransport(url=args.endpoint, headers={"Authorization": args.token})

    client = Client(transport=transport, fetch_schema_from_transport=True)

    query = gql(
        """
            query listInfras($project_id: ID!){
              listInfras(projectID: $project_id){
                infras {
                  projectID
                    infraID
                    name
                }
              }
            }
        """
    )
    variables = {"project_id": "21ae8dde-f6d1-463b-b7b0-5e7a7af0c44a"}
    result = client.execute(query, variables)
    print(result)

    query = gql(
        """
            query listExperiment($project_id: ID!, $request: ListExperimentRequest!){
              listExperiment(projectID: $project_id, request: $request){
                experiments {
                    experimentID
                    name
                }
              }
            }
        """
    )
    variables = {"project_id": "21ae8dde-f6d1-463b-b7b0-5e7a7af0c44a", "request": {}}
    result = client.execute(query, variables)
    print(result)

    mutation = gql(
        """
mutation createChaosExperiment($project_id: ID!, $request: ChaosExperimentRequest!){
  createChaosExperiment(request: $request, projectID: $project_id){
    experimentID
    experimentName
  }
}
        """
    )
    variables = {
        "request": {"infraID": "89c5457a-e674-4669-b937-c4b462ec31ae",
                    "runExperiment": False,
                    "experimentName": "ob-cartservice-pod-cpu-hog",
                    "experimentDescription": "",
                    "experimentManifest": json.dumps(
                        {
                            "kind": "Workflow",
                            "apiVersion": "argoproj.io/v1alpha1",
                            "metadata": {
                                "name": "ob-cartservice-pod-cpu-hog",
                                "namespace": "litmus",
                                "creationTimestamp": None,
                                "labels": {
                                    "infra_id": "89c5457a-e674-4669-b937-c4b462ec31ae",
                                    "subject": "onlineboutique_cartservice",
                                    "workflows.argoproj.io/controller-instanceid": "89c5457a-e674-4669-b937-c4b462ec31ae"
                                }
                            },
                            "spec": {
                                "templates": [
                                    {
                                        "name": "argowf-chaos",
                                        "inputs": {},
                                        "outputs": {},
                                        "metadata": {},
                                        "steps": [
                                            [
                                                {
                                                    "name": "install-chaos-faults",
                                                    "template": "install-chaos-faults",
                                                    "arguments": {}
                                                }
                                            ],
                                            [
                                                {
                                                    "name": "run-chaos",
                                                    "template": "run-chaos",
                                                    "arguments": {}
                                                }
                                            ],
                                            [
                                                {
                                                    "name": "cleanup-chaos-resources",
                                                    "template": "cleanup-chaos-resources",
                                                    "arguments": {}
                                                }
                                            ]
                                        ]
                                    },
                                    {
                                        "name": "install-chaos-faults",
                                        "inputs": {
                                            "artifacts": [
                                                {
                                                    "name": "install-chaos-faults",
                                                    "path": "/tmp/pod-cpu-hog.yaml",
                                                    "raw": {
                                                        "data": "apiVersion: litmuschaos.io/v1alpha1\ndescription:\n  message: |\n    Injects cpu consumption on pods belonging to an app deployment\nkind: ChaosExperiment\nmetadata:\n  name: pod-cpu-hog\nspec:\n  definition:\n    scope: Namespaced\n    permissions:\n      - apiGroups:\n          - \"\"\n          - \"batch\"\n          - \"litmuschaos.io\"\n        resources:\n          - \"jobs\"\n          - \"pods\"\n          - \"pods/log\"\n          - \"events\"\n          - \"chaosengines\"\n          - \"chaosexperiments\"\n          - \"chaosresults\"\n        verbs:\n          - \"create\"\n          - \"list\"\n          - \"get\"\n          - \"patch\"\n          - \"update\"\n          - \"delete\"\n    image: \"litmuschaos/go-runner:3.1.0\"\n    imagePullPolicy: Always\n    args:\n    - -c\n    - ./experiments -name pod-cpu-hog\n    command:\n    - /bin/bash\n    env:\n    - name: TOTAL_CHAOS_DURATION\n      value: '30'\n\n    - name: CHAOS_INTERVAL\n      value: '10'\n\n    ## Number of CPU cores to stress\n    - name: CPU_CORES\n      value: '1'\n\n    ## Percentage of total pods to target\n    - name: PODS_AFFECTED_PERC\n      value: ''\n\n    ## Period to wait before and after injection of chaos in sec\n    - name: RAMP_TIME\n      value: ''\n\n    - name: TARGET_POD\n      value: ''\n\n    labels:\n      name: pod-cpu-hog\n"
                                                    }
                                                }
                                            ]
                                        },
                                        "outputs": {},
                                        "metadata": {},
                                        "container": {
                                            "name": "",
                                            "image": "litmuschaos/k8s:latest",
                                            "command": [
                                                "sh",
                                                "-c"
                                            ],
                                            "args": [
                                                "kubectl apply -f /tmp/pod-cpu-hog.yaml -n {{workflow.parameters.adminModeNamespace}}"
                                            ],
                                            "resources": {}
                                        }
                                    },
                                    {
                                        "name": "run-chaos",
                                        "inputs": {
                                            "artifacts": [
                                                {
                                                    "name": "run-chaos",
                                                    "path": "/tmp/chaosengine-run-chaos.yaml",
                                                    "raw": {
                                                        "data": "apiVersion: litmuschaos.io/v1alpha1\nkind: ChaosEngine\nmetadata:\n  namespace: \"{{workflow.parameters.adminModeNamespace}}\"\n  labels:\n    context: onlineboutique_cartservice\n    workflow_run_id: \"{{ workflow.uid }}\"\n    workflow_name: ob-cartservice-chaos-pod-cpu-hog\n  annotations:\n    probeRef: '[{\"name\":\"onlineboutique\",\"mode\":\"EOT\"}]'\n  generateName: run-chaos\nspec:\n  appinfo:\n    appns: onlineboutique\n    applabel: app=cartservice\n    appkind: deployment\n  jobCleanUpPolicy: delete\n  engineState: active\n  chaosServiceAccount: litmus-admin\n  experiments:\n    - name: pod-cpu-hog\n      spec:\n        components:\n          env:\n            - name: TARGET_CONTAINER\n              value: server\n            - name: CPU_CORES\n              value: \"1\"\n            - name: TOTAL_CHAOS_DURATION\n              value: \"60\"\n            - name: CHAOS_KILL_COMMAND\n              value: >-\n                kill -9 $(ps afx | grep \"[md5sum] /dev/zero\" | awk '{print$1}' | tr '\n\n                ' ' ')\n"
                                                    }
                                                }
                                            ]
                                        },
                                        "outputs": {},
                                        "metadata": {
                                            "labels": {
                                                "weight": "10"
                                            }
                                        },
                                        "container": {
                                            "name": "",
                                            "image": "docker.io/litmuschaos/litmus-checker:2.11.0",
                                            "args": [
                                                "-file=/tmp/chaosengine-run-chaos.yaml",
                                                "-saveName=/tmp/engine-name"
                                            ],
                                            "resources": {}
                                        }
                                    },
                                    {
                                        "name": "cleanup-chaos-resources",
                                        "inputs": {},
                                        "outputs": {},
                                        "metadata": {},
                                        "container": {
                                            "name": "",
                                            "image": "litmuschaos/k8s:latest",
                                            "command": [
                                                "sh",
                                                "-c"
                                            ],
                                            "args": [
                                                "kubectl delete chaosengine -l workflow_run_id={{workflow.uid}} -n {{workflow.parameters.adminModeNamespace}}"
                                            ],
                                            "resources": {}
                                        }
                                    }
                                ],
                                "entrypoint": "argowf-chaos",
                                "arguments": {
                                    "parameters": [
                                        {
                                            "name": "adminModeNamespace",
                                            "value": "litmus"
                                        },
                                        {
                                            "name": "appNamespace",
                                            "value": "onlineboutique"
                                        }
                                    ]
                                },
                                "serviceAccountName": "argo-chaos",
                                "securityContext": {
                                    "runAsUser": 1000,
                                    "runAsNonRoot": True
                                }
                            },
                            "status": {
                                "startedAt": None,
                                "finishedAt": None
                            }
                        }
                    ),
                    "cronSyntax": "",
                    "weightages": [],
                    "tags": ["heroic", "onlineboutique", "cartservice", "pod-cpu-hog"],
                    "isCustomExperiment": True
                    },
        "project_id": "21ae8dde-f6d1-463b-b7b0-5e7a7af0c44a"
    }
    result = client.execute(mutation, variables)
    print(result)