from .notification import Notification
from .notification_type import NotificationType


class EmailNotification(Notification):

    def __init__(self, sender: str, recipient: str, message: str):
        self._sender = sender
        super(EmailNotification, self).__init__(recipient, message)

    # Getter
    def get_sender(self):
        return self._sender

    # Abstract functions implementation
    def notification_type(self) -> NotificationType:
        return NotificationType.EMAIL

    def send_notification(self):
        # Logic to send email goes here
        print("Email sent from: ", self.get_sender(), " -> to: ", self.get_recipient())
        print("Message: ", self.get_message())