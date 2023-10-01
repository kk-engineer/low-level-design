from ..observer import Observer
from ..utils.notification_utils import NotificationUtils


class EmailService(Observer):

    def notify_observer(self, stock_name: str, current_price: int):
        subject = "Price update for " + stock_name
        message = "New price is " + str(current_price)
        NotificationUtils.send_email(subject, message)