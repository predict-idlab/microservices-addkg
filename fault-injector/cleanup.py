from argparse import ArgumentParser

from litmus import ChaosClient

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--endpoint", default="http://localhost:9002/query", help="ChaosCenter API Endpoint")
    parser.add_argument("--token", default="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjQ4NTc0NDM1NzksInJvbGUiOiJhZG1pbiIsInVpZCI6IjQwYzVjMTY3LTZlYTEtNGFiOC1hZGZhLThmMWUyN2U1YzBkMiIsInVzZXJuYW1lIjoiYWRtaW4ifQ.ioCAhS_dSUUiGhgnd_za7BvtYVDpvWrMeZpytcxAmBbeO86Lj-juOLNZWTWCAeaxExOZBuEYw4kpt8AgUbIbFQ", help="ChaosCenter API Token")
    parser.add_argument("--project-id", default="21ae8dde-f6d1-463b-b7b0-5e7a7af0c44a", help="ChaosCenter Project ID")
    parser.add_argument("--infra-id", default="e1a3fe10-c1c3-4227-ac71-5f8e0cefaab3", help="ChaosCenter Infrastructure ID")

    args = parser.parse_args()

    client = ChaosClient(args.endpoint, args.token)

    response = client.list_experiment(args.project_id)["data"]["listExperiment"]
    experiments = response["experiments"]
    print(experiments)

    while experiments:
        for experiment in experiments:
            experiment_id = experiment["experimentID"]
            success = client.delete_experiment(args.project_id, experiment_id)
            print(success)

        response = client.list_experiment(args.project_id)["data"]["listExperiment"]
        experiments = response["experiments"]
        print(experiments)
