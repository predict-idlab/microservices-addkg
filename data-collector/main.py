from argparse import ArgumentParser
from datetime import datetime, timedelta
import logging
from pytimeparse.timeparse import timeparse
import pytz
from time import sleep

from tasks import app, collect_data

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--host", default="http://localhost:9090", help="Prometheus host endpoint")
    parser.add_argument("--namespace", "-n", default="default", help="Kubernetes namespace")

    parser.add_argument("--output", "-o", default="/data", help="Output directory")

    parser.add_argument("--start-time", help="Start time (e.g. 2023-12-24T23:59:00)")
    parser.add_argument("--end-time", help="End time (e.g. 2023-12-25T23:59:00)")
    parser.add_argument("--interval", default="1h", help="Interval (e.g. 15s, 1m, 1h, 1d)")

    parser.add_argument("--log-level", default="INFO", help="Log level")
    parser.add_argument("--log-file", help="Log file")

    args = parser.parse_args()

    # Logging
    logger = logging.getLogger(__name__)
    logger.setLevel(args.log_level)
    formatter = logging.Formatter('[%(asctime)s] - [%(name)s] - [%(levelname)s] %(message)s')
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    if args.log_file:
        fh = logging.FileHandler(args.log_file)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    if args.start_time and args.end_time:
        start_time = datetime.fromisoformat(args.start_time)
        end_time = datetime.fromisoformat(args.end_time)

        collect_data.delay(args.host, args.namespace, start_time, end_time, args.output)
        while True:
            sleep(10)
    elif args.interval:
        end_time = datetime.now(tz=pytz.utc)
        start_time = end_time - timedelta(seconds=timeparse(args.interval))

        app.add_periodic_task(
            timeparse(args.interval),
            collect_data, args=(args.host, args.namespace, start_time, end_time, args.output,),
            name="create_graphs")
    else:
        logging.critical("Either start and end time or interval must be specified.")
        raise ValueError("Either start and end time or interval must be specified.")
