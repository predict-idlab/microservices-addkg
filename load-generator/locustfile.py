import time
from random import randint
from typing import Tuple, Optional, List, Type

import locust.env
from locust import User, HttpUser, events, task, LoadTestShape
from locust.exception import StopUser
from locust.runners import WorkerRunner
import locust.stats
import numpy as np
import os

from config import ConfigFactory, ConfigType
from load_distribution import Minimum, Peak
from tasks import MarkovChain, Index

locust.stats.CSV_STATS_INTERVAL_SEC = 15
locust.stats.CSV_STATS_FLUSH_INTERVAL_SEC = 300


app_settings = os.getenv('CONFIGURATION', default='development')
type_ = ConfigType.reverse_lookup(app_settings)
cfactory = ConfigFactory()
config = cfactory.get(type_)


class LoadDistribution(LoadTestShape):

    def __init__(self):
        super().__init__()

        self.min_users = config.MIN_USERS
        self.max_users = config.MAX_USERS

        seconds_per_unit = 3600
        self.window_size = 24 * seconds_per_unit

        self.stages = [
            Minimum(self.min_users),
            Peak(x=12 * seconds_per_unit, y=0.1 * self.max_users, scale=2, ws=self.window_size),
            Peak(x=8 * seconds_per_unit, y=0.5 * self.max_users, scale=5, ws=self.window_size),
            Peak(x=11 * seconds_per_unit, y=0.4 * self.max_users, scale=5, ws=self.window_size),
            Peak(x=13 * seconds_per_unit, y=0.4 * self.max_users, scale=10, ws=self.window_size),
            Peak(x=16 * seconds_per_unit, y=0.6 * self.max_users, scale=5, ws=self.window_size),
            Peak(x=21 * seconds_per_unit, y=1 * self.max_users, scale=10, ws=self.window_size)
        ]

        self.values = [
            np.sum([stage_.calculate_datapoint(i) for stage_ in self.stages]) for i in range(self.window_size)
        ]

    def tick(self) -> Tuple[int, float] | Tuple[int, float, Optional[List[Type[User]]]] | None:
        t = time.localtime()
        secs = 3600 * t.tm_hour + 60 * t.tm_min + t.tm_sec

        n_users = self.values[secs]
        n_users = randint(max(0, int(n_users - 0.1 * self.max_users)), int(n_users + 0.1 * self.max_users))

        # Limit spawn rate <= 100 for performance.
        tick_data = (n_users, max(n_users, 100))

        return tick_data


def on_user_start(environment: locust.env.Environment, msg, **kwargs):
    print('Started user', msg.data)


def on_user_stop(environment: locust.env.Environment, msg, **kwargs):
    print('Stopped user', msg.data)


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    if not isinstance(environment.runner, WorkerRunner):
        environment.runner.register_message('on_user_start', on_user_start)
        environment.runner.register_message('on_user_stop', on_user_stop)


class WebsiteUser(HttpUser):

    @task
    def sequence(self):
        task_chain = MarkovChain(root=Index)
        task_chain.run(locust=self)

        raise StopUser
