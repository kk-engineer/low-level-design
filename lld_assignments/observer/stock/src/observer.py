from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def notify_observer(self, stock_name: str, current_price: int):
        ...
