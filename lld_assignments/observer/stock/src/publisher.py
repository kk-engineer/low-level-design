from abc import ABC
from .observer_registry import ObserverRegistry
from .observer import Observer


class Publisher(ObserverRegistry, ABC):

    def __init__(self):
        self._observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, stock_name: str, current_price: int):
        for observer in self._observers:
            observer.notify_observer(stock_name, current_price)



