from datetime import datetime

from rocketry import Rocketry

import collector
from main import DataCollector

app = Rocketry()


@app.task("every 15 seconds")
def fetch_graph(host: str = "http://localhost:9090", namespace: str = "onlineboutique"):
    timestamp = datetime.datetime.now()
    end_time = timestamp
    start_time = end_time - datetime.timedelta(minutes=5)

    client = DataCollector(host=host)

    graph = collector.fetch_infrastructure_topology(namespace=namespace)
    client.fetch_monitoring_data(graph, start_time, end_time)

    graph.serialize(f'./data/graph_{end_time}', format="ttl")
