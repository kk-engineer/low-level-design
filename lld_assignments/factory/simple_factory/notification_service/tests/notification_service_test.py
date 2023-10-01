import unittest
from ..src.notification_type import NotificationType
from ..src.notification_factory import NotificationFactory


class TestNotificationService(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestNotificationService, self).__init__(*args, **kwargs)
        self._sender = "Interviewbit"
        self._recipient = "Scaler"
        self._message = "Hello Friend!"
        self._notification_factory = NotificationFactory()

    def test_email(self):
        notification_type = NotificationType.EMAIL
        notification_service = self._notification_factory.create_notification(notification_type,
                                                                              self._recipient,
                                                                              self._message,
                                                                              self._sender)

        notification_service.send_notification()
        self.assertEqual(notification_service.notification_type(), NotificationType.EMAIL)

    def test_push(self):
        notification_type = NotificationType.PUSH
        notification_service = self._notification_factory.create_notification(notification_type,
                                                                              self._recipient,
                                                                              self._message,
                                                                              self._sender)

        notification_service.send_notification()
        self.assertEqual(notification_service.notification_type(), NotificationType.PUSH)

    def test_sms(self):
        notification_type = NotificationType.SMS
        notification_service = self._notification_factory.create_notification(notification_type,
                                                                              self._recipient,
                                                                              self._message,
                                                                              self._sender)

        notification_service.send_notification()
        self.assertEqual(notification_service.notification_type(), NotificationType.SMS)


if __name__ == '__main__':
    unittest.main()
