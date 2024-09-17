from abc import ABC
import math


class Stage(ABC):

    def calculate_datapoint(self, i):
        raise NotImplementedError


class Minimum(Stage):

    def __init__(self, y):
        self.y = y

    def calculate_datapoint(self, i):
        return self.y


class Peak(Stage):
    """
    Gaussian
    """

    def __init__(self, x, y, scale, ws):
        self.x = x
        self.y = y
        self.scale = scale
        self.ws = ws

        data = [self.y * math.e ** -(((self.scale * i / self.x) - self.scale) ** 2) for i in range(2 * self.ws)]
        self.data = [max(data[i], data[i + self.ws]) for i in range(self.ws)]

    def calculate_datapoint(self, i):
        # return sc.stats.norm.pdf(i, loc=self.x, scale=self.std)
        return self.data[i % self.ws]


class Dip(Peak):
    def __init__(self, x, y, std, ws):
        super().__init__(x, y, std, ws)

    def calculate_datapoint(self, i):
        return - super().calculate_datapoint(i)
