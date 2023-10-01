from .notification import Notification
from .notification_type import NotificationType


class PushNotification(Notification):

    def __init__(self, recipient: str, message: str):
        super(PushNotification, self).__init__(recipient, message)

    # Abstract functions implementation
    def notification_type(self) -> NotificationType:
        return NotificationType.PUSH

    def send_notification(self):
        # Logic to send push notification goes here
        print("Push notification sent to device: ", self.get_recipient())
        print("Message: ", self.get_message())