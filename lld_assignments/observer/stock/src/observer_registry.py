from abc import ABC, abstractmethod
from .observer import Observer


class ObserverRegistry(ABC):

    @abstractmethod
    def add_observer(self, observer: Observer):
        ...

    @abstractmethod
    def remove_observer(self, observer: Observer):
        ...

    @abstractmethod
    def notify_observers(self, stock_name: str, current_price: int):
        ...
