import logging
from argparse import ArgumentParser
import os
import pandas as pd
import random
import time

from litmus import ChaosClient
from litmus.faults.factory import FaultFactory, FaultType

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--endpoint", default="http://localhost:9002/query", help="ChaosCenter API Endpoint")
    parser.add_argument("--token", default="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjQ4NTc0NDM1NzksInJvbGUiOiJhZG1pbiIsInVpZCI6IjQwYzVjMTY3LTZlYTEtNGFiOC1hZGZhLThmMWUyN2U1YzBkMiIsInVzZXJuYW1lIjoiYWRtaW4ifQ.ioCAhS_dSUUiGhgnd_za7BvtYVDpvWrMeZpytcxAmBbeO86Lj-juOLNZWTWCAeaxExOZBuEYw4kpt8AgUbIbFQ", help="ChaosCenter API Token")
    parser.add_argument("--project-id", default="21ae8dde-f6d1-463b-b7b0-5e7a7af0c44a", help="ChaosCenter Project ID")
    parser.add_argument("--infra-id", default="89c5457a-e674-4669-b937-c4b462ec31ae", help="ChaosCenter Infrastructure ID")

    parser.add_argument("--max-delay", default=0, type=int, help="Max delay in seconds")

    parser.add_argument("--log-level", default="INFO", help="Log level")
    parser.add_argument("--log-file", default=None, help="Log file")

    parser.add_argument("--output-file", default="results.csv", help="Output file")

    args = parser.parse_args()

    # Logging
    logging.basicConfig(level=args.log_level)
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('[%(asctime)s] - [%(name)s] - [%(levelname)s] %(message)s')
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    if args.log_file:
        fh = logging.FileHandler(args.log_file)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    logger.info(f"Connecting to ChaosCenter at {args.endpoint}")
    logger.info(f"Project ID: {args.project_id}, Infrastructure ID: {args.infra_id}")
    client = ChaosClient(args.endpoint, args.token)

    fault_factory = FaultFactory()
    faults = [e for e in FaultType.__members__.values()]

    fault = fault_factory.get(random.choice(faults))(app_namespace="onlineboutique")
    logger.info(f"Selected fault: {fault.name}")

    # Random delay before execution to create randomness in the dataset
    delay = random.randint(0, args.max_delay)
    logger.info(f"Delaying execution for {delay} seconds.")
    time.sleep(random.randint(0, args.max_delay))

    logger.info(f"Executing fault: {fault.name}")
    result = fault.execute(client, args.project_id, args.infra_id).__dict__()

    logger.info(f"Result: {result}")
    # Store the result
    logger.info(f"Storing result in {args.output_file}.")
    df = pd.DataFrame([result])

    if os.path.exists(args.output_file):
        df = pd.read_csv(args.output_file, index_col=0)
        df = pd.concat([df, pd.DataFrame([result])], ignore_index=True)

    df.to_csv(args.output_file)
    logger.info(f"Finished fault injection.")
