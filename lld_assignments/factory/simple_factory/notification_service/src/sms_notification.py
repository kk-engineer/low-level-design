from .notification import Notification
from .notification_type import NotificationType


class SmsNotification(Notification):

    def __init__(self, recipient: str, message: str):
        super(SmsNotification, self).__init__(recipient, message)

    # Abstract functions implementation
    def notification_type(self) -> NotificationType:
        return NotificationType.SMS

    def send_notification(self):
        # Logic to send SMS notification goes here
        print("SMS notification sent to: ", self.get_recipient())
        print("Message: ", self.get_message())