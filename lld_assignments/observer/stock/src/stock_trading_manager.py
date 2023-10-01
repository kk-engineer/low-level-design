from abc import ABC

from .publisher import Publisher


class StockTradingManager(Publisher):

    def __init__(self, stock_name: str,
                 initial_price: int,
                 notification_threshold: int):
        super().__init__()
        self._stock_name = stock_name
        self._current_price = initial_price
        self._notification_threshold = notification_threshold

    def update_stock_price(self, new_price: int):
        self._current_price = new_price
        if self._current_price > self._notification_threshold:
            self.notify_observers(self._stock_name, self._current_price)



