import unittest

from ..src.stock_trading_manager import StockTradingManager
from ..src.services.email_service import EmailService
from ..src.services.app_service import AppService
from ..src.services.sms_service import SmsService


class TestStockTradingManager(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestStockTradingManager, self).__init__(*args, **kwargs)
        self._stock_trading_manager = StockTradingManager("ABC", 100, 150)

    def test_send_notification(self):
        self._stock_trading_manager.add_observer(EmailService())
        self._stock_trading_manager.add_observer(AppService())
        self._stock_trading_manager.add_observer(SmsService())
        self._stock_trading_manager.update_stock_price(160)


if __name__ == '__main__':
    unittest.main()
