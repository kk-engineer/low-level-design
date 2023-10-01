from .notification_type import NotificationType
from .notification import Notification
from .email_notification import EmailNotification
from .push_notification import PushNotification
from .sms_notification import SmsNotification


class NotificationFactory:

    @staticmethod
    def create_notification(notification_type: NotificationType, recipient: str, message: str,
                            sender: str) -> Notification:
        if notification_type == NotificationType.EMAIL:
            return EmailNotification(sender, recipient, message)
        elif notification_type == NotificationType.PUSH:
            return PushNotification(recipient, message)
        elif notification_type == NotificationType.SMS:
            return SmsNotification(recipient, message)
        else:
            raise Exception("Invalid notification type")
