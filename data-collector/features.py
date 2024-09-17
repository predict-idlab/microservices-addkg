from datetime import datetime, timedelta
import pandas as pd
from prometheus_api_client import PrometheusConnect
from prometheus_api_client.utils import parse_datetime
from tqdm import tqdm


frontend = "frontend-external.onlineboutique.svc.cluster.local"

range_features = {
    "request_count": f'sum(rate(istio_requests_total{{reporter="destination", destination_service="{frontend}"}}[5m])) by (destination_service)',
    "request_count_4xx": f'sum(rate(istio_requests_total{{reporter="destination", response_code=~"4.*", destination_service="{frontend}"}}[5m])) by (destination_service)',
    "request_count_5xx": f'sum(rate(istio_requests_total{{reporter="destination", response_code=~"5.*", destination_service="{frontend}"}}[5m])) by (destination_service)',
}


aggregated_features = {
    "request_duration": f'sum(rate(istio_request_duration_milliseconds_sum{{reporter="destination", destination_service="{frontend}"}}[5m])) by (destination_service) '
                        f'/ sum(rate(istio_request_duration_milliseconds_count{{reporter="destination", destination_service="{frontend}"}}[5m])) by (destination_service)',
}

if __name__ == "__main__":
    client = PrometheusConnect()

    dates = ["2024-02-10", "2024-02-11", "2024-02-12", "2024-02-13", "2024-02-14"]
    features = {}

    for date in dates:
        start_time = datetime.strptime(date, "%Y-%m-%d")
        end_time = start_time + timedelta(days=1)

        features_day = {}

        for feature, qry in range_features.items():
            data = client.custom_query_range(
                query=qry,
                start_time=start_time,
                end_time=end_time,
                step="15"
            )

            if data:
                for timestamp, value in data[0]["values"]:
                    timestamp = datetime.fromtimestamp(timestamp)
                    if timestamp not in features_day.keys():
                        features_day[timestamp] = {}
                    features_day[timestamp][feature] = value

        for feature, qry in aggregated_features.items():
            for t in tqdm(range(0, int(timedelta(days=1).total_seconds()), 15)):
                timestamp = start_time + timedelta(seconds=t)
                data = client.get_metric_aggregation(
                    query=qry,
                    operations=["min", "max", "average",
                                "percentile_50", "percentile_90", "percentile_95",
                                "deviation", "variance"],
                    start_time=timestamp - timedelta(minutes=5),
                    end_time=timestamp
                )

                if data is not None:
                    for key, value in data.items():
                        if timestamp not in features_day.keys():
                            features_day[timestamp] = {}
                        features_day[timestamp][f"{feature}_{key}"] = value

        features_day_df = pd.DataFrame()
        features_day_df = features_day_df.from_dict(features_day, orient="index")

        features_day_df.to_pickle(f"data/{date}-features.pickle")
        features_day_df.head().to_csv(f"data/{date}-features-example.csv")
