import random
from time import sleep
from locust import HttpUser
import networkx as nx
import numpy as np


def between(min_, max_):
    return min_ + random.random() * (max_ - min_)


class StateMeta(type):

    def __new__(mcs, classname, bases, class_dict):
        return type.__new__(mcs, classname, bases, class_dict)


class State(metaclass=StateMeta):

    data = {}
    children = {}

    @classmethod
    def get_next(cls):
        choices = list(cls.children.keys())
        weights = list(cls.children.values())

        if choices:
            return np.random.choice(choices, p=weights)
        return None

    def execute(self, *args, **kwargs):
        raise NotImplementedError


class TransitionMeta(type):

    def __new__(mcs, classname, bases, class_dict):
        current_state = class_dict['current_state'] or None
        transitions = class_dict['transitions'] or {}

        if current_state is not None:
            current_state.children = transitions

        return type.__new__(mcs, classname, bases, class_dict)


class Transition(metaclass=TransitionMeta):

    current_state = None
    transitions = {}


class MarkovChain(nx.MultiDiGraph):

    def __init__(self, root, **attr):
        super().__init__(**attr)

        self.root = root
        self.states = [root]
        self.add_state(root)

    def add_state(self, state):
        for next_, w in state.children.items():
            self.add_edge(state.__name__, next_.__name__, label=str(w), weight=w)

            if next_ not in self.states:
                self.states.append(next_)
                self.add_state(next_)

    def generate_chain(self):
        chain_ = [self.root]

        while True:
            next_ = chain_[-1].get_next()
            if next_ is not None:
                chain_.append(next_)
            else:
                break

        return chain_

    def run(self, *args, **kwargs):
        """
        Run through the entire MarkovChain.
        The context will be updated and passed through the chain.

        :param args:
        :param kwargs:
        """
        context = {}

        for state in self.generate_chain():
            result = state.execute(self, *args, **kwargs, **context)
            if result is not None:
                context.update(result)

products = [
    "0PUK6V6EV0",
    "1YMWWN1N4O",
    "2ZYFJ3GM2N",
    "66VCHSJNUP",
    "6E92ZMYYFZ",
    "9SIQT8TOJO",
    "L9ECAV7KIM",
    "LS4PSXUNUM",
    "OLJCESPC7Z"]


class Index(State):

    def execute(self, locust: HttpUser):
        locust.client.get("/")
        sleep(between(2, 15))


class SetCurrency(State):
    def execute(self, locust: HttpUser):
        currencies = ["EUR", "USD", "JPY", "CAD"]
        locust.client.post("/setCurrency", {"currency_code": random.choice(currencies)})
        sleep(between(2, 15))


class BrowseProduct(State):

    def execute(self, locust: HttpUser):
        locust.client.get("/product/" + random.choice(products))
        sleep(between(5, 30))


class ViewCart(State):

    def execute(self, locust: HttpUser):
        locust.client.get("/cart")
        sleep(between(5, 30))


class AddToCart(State):

    def execute(self, locust: HttpUser):
        product = random.choice(products)
        locust.client.get("/product/" + product)
        sleep(between(5, 30))
        locust.client.post("/cart", {
            "product_id": product,
            "quantity": random.choice([1, 2, 3, 4, 5, 10])})
        sleep(between(2, 15))


class Checkout(State):

    def execute(self, locust: HttpUser):
        locust.client.post("/cart/checkout", {
            "email": "someone@example.com",
            "street_address": "1600 Amphitheatre Parkway",
            "zip_code": "94043",
            "city": "Mountain View",
            "state": "CA",
            "country": "United States",
            "credit_card_number": "4432-8015-6152-0454",
            "credit_card_expiration_month": "1",
            "credit_card_expiration_year": "2039",
            "credit_card_cvv": "672",
        })
        sleep(between(2, 15))


class Close(State):

    def execute(self, locust: HttpUser):
        pass


class IndexTransition(Transition):

    current_state = Index

    transitions = {
        SetCurrency: 0.3,
        BrowseProduct: 0.6,
        Close: 0.1
    }


class SetCurrencyTransition(Transition):

    current_state = SetCurrency

    transitions = {
        BrowseProduct: 0.8,
        Close: 0.2
    }


class BrowseProductTransition(Transition):

    current_state = BrowseProduct

    transitions = {
        BrowseProduct: 0.2,
        AddToCart: 0.6,
        Close: 0.2
    }


class AddToCartTransition(Transition):

    current_state = AddToCart

    transitions = {
        BrowseProduct: 0.2,
        ViewCart: 0.6,
        Close: 0.2
    }


class ViewCartTransition(Transition):

    current_state = ViewCart

    transitions = {
        BrowseProduct: 0.3,
        Checkout: 0.7,
    }


class CheckoutTransition(Transition):

    current_state = Checkout

    transitions = {
        Close: 1
    }
