import datetime
from matplotlib import pyplot as plt
from matplotlib import dates as md
import pandas as pd

from locustfile import LoadDistribution

if __name__ == '__main__':
    distribution = LoadDistribution()

    complete_range = []

    figure, ax1 = plt.subplots()
    # for stage in distribution.stages:
    #     plt.plot(
    #         range(distribution.window_size),
    #         [stage.calculate_datapoint(i % distribution.window_size) for i in range(distribution.window_size)])

    xfmt = md.DateFormatter('%H:%M:%S')
    plt.gca().xaxis.set_major_formatter(xfmt)

    timestamps = \
        [datetime.datetime(day=25, month=12, year=2023) + datetime.timedelta(seconds=x) for x in range(distribution.window_size)]
    line1, = ax1.plot(timestamps, distribution.values, label='Users', color='#E64A24', zorder=10)
    ax1.fill_between(timestamps, [max(0, i - 2) for i in distribution.values], [i + 2 for i in distribution.values], color='#E64A24', alpha=0.2, zorder=10)

    ax1.set_xlabel('Time')
    ax1.set_ylabel('Users')
    # ax1.set_ylim(0, 25)
    plt.xticks(rotation=25)

    requests = pd.read_parquet('./data/requests.parquet')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Throughput (req/s)')
    # ax2.set_ylim(0, 25)
    line2, = ax2.plot(requests['timestamp'], requests['value'], label='Throughput', color='#143057', zorder=5)

    plt.legend(handles=[line1, line2], loc='upper left')
    plt.savefig('distribution.png', dpi=600)
    plt.show()
