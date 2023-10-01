from enum import Enum


class BookingStatus(Enum):
    NOT_AVAILABLE = 1
    PAYMENT_FAILED = 2
    SUCCESS = 3