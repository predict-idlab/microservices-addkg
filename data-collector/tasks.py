import pickle

from celery import Celery
from datetime import datetime, timedelta
import os
import pandas as pd
from pytimeparse.timeparse import timeparse
import pytz
from tqdm import tqdm
from typing import List

from collector import DataCollector
from config import BaseConfig
from ink.base.connectors import RDFLibConnector
from ink.base.structure import InkExtractor

app = Celery("tasks", broker=BaseConfig.CELERY_BROKER_URL, backend=BaseConfig.CELERY_RESULT_BACKEND, broker_connection_retry_on_startup=True)
app.config_from_object(BaseConfig)

if BaseConfig.COLLECTOR_INTERVAL:
    app.conf.beat_schedule = {
        "trigger-data-collector": {
            "task": "collector.collect_data",
            "schedule": timeparse(BaseConfig.COLLECTOR_INTERVAL)  # in seconds
        }
    }


@app.task(name="collector.collect_data")
def collect_data(host: str = BaseConfig.TARGET_PROMETHEUS_URL,
                 namespace: str = BaseConfig.TARGET_K8S_NAMESPACE,
                 start_time: str = BaseConfig.COLLECTOR_START_TIME,
                 end_time: str = BaseConfig.COLLECTOR_END_TIME,
                 interval: str = BaseConfig.COLLECTOR_INTERVAL,
                 output: str = BaseConfig.COLLECTOR_OUTPUT):

    client = DataCollector(host=host, namespace=namespace)

    if start_time and end_time:
        start_time = datetime.fromisoformat(start_time)
        end_time = datetime.fromisoformat(end_time)
    elif interval:
        end_time = datetime.now(tz=pytz.utc)
        start_time = end_time - timedelta(seconds=timeparse(interval))

    ranges = []
    timestamp = start_time
    while timestamp < end_time:
        ranges.append((timestamp - timedelta(minutes=5), timestamp))
        timestamp = timestamp + timedelta(seconds=15)

    for start, end in tqdm(ranges):
        print(f"Fetching data from {start} to {end}")
        graph = client.fetch_monitoring_data(start, end)
        graph_id = int(end.timestamp())

        day = end.strftime("%Y-%m-%d")
        output_path = os.path.join(output, day, "graphs")
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        graph_file = os.path.join(output_path, f"{graph_id}.ttl")
        graph.serialize(graph_file, format="ttl")

        # Start embedding task
        # calculate_embedding.delay(f"graph_{int(end.timestamp())}", ["https://github.com/predict/deucalion#cluster.local"], depth=5)

        # Generate embedding
        print(f"Generating embedding for {graph_id}")
        connector = RDFLibConnector(graph_file, dataformat="ttl")

        # nodes = ["https://github.com/predict/deucalion#cluster.local"]
        extractor = InkExtractor(connector, verbose=False)
        X_train, _ = extractor.create_dataset(depth=5, pos=set(list( ["https://github.com/predict/deucalion#cluster.local"])), neg=set(), skip_list=[], jobs=1)

        # Counts: Edge features (incoming/outgoing)
        # Levels: Binding quants for rules (e.g. CPU > 90%)
        # Float RPR: Numerical literals
        extracted_data = extractor.fit_transform(X_train, counts=True, levels=False, float_rpr=True)
        data = pd.DataFrame.sparse.from_spmatrix(extracted_data[0], index=extracted_data[1], columns=extracted_data[2])
        data = data.sparse.to_dense()
        data["timestamp"] = pd.Timestamp(graph_id, unit="s")

        print(f"Saving embedding for {graph_id}")
        output_path = os.path.join(output, day, "embeddings")
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        data.to_pickle(os.path.join(output_path, f"{int(end.timestamp())}.pickle"))

@app.task(name="collector.calculate_embedding")
def calculate_embedding(file_name, nodes: List[str], depth: int = 4,
                        output: str = BaseConfig.COLLECTOR_OUTPUT):
    graph_file = os.path.join(output, f"{file_name}.ttl")
    connector = RDFLibConnector(graph_file, dataformat="ttl")
    
    # nodes = ["https://github.com/predict/deucalion#cluster.local"]
    extractor = InkExtractor(connector, verbose=False)
    X_train, _ = extractor.create_dataset(depth=depth, pos=set(list(nodes)), neg=set(), skip_list=[], jobs=1)

    # Counts: Edge features (incoming/outgoing)
    # Levels: Binding quants for rules (e.g. CPU > 90%)
    # Float RPR: Numerical literals
    extracted_data = extractor.fit_transform(X_train, counts=True, levels=False, float_rpr=True)
    data = pd.DataFrame.sparse.from_spmatrix(extracted_data[0], index=extracted_data[1], columns=extracted_data[2])
    data = data.sparse.to_dense()
    data["timestamp"] = pd.Timestamp(int(file_name.split("_")[-1].split(".")[0]), unit="s")

    data.to_pickle(os.path.join(output, f"{file_name}.pickle"))
