from abc import ABC, abstractmethod
from .notification_type import NotificationType


class Notification(ABC):
    def __init__(self, recipient: str, message: str):
        self._recipient = recipient
        self._message = message

    # Getters
    def get_recipient(self) -> str:
        return self._recipient

    def get_message(self) -> str:
        return self._message

    @abstractmethod
    def notification_type(self) -> NotificationType:
        ...

    @abstractmethod
    def send_notification(self):
        ...
