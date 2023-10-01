from .booking_status import BookingStatus
from .booking_confirmation import BookingConfirmation


class BookingResult:

    def __init__(self, status: BookingStatus,
                 confirmation: BookingConfirmation,
                 error_message: str):
        self._status = status
        self._confirmation = confirmation
        self._error_message = error_message

    # Getters
    def get_status(self) -> BookingStatus:
        return self._status

    def get_confirmation(self) -> BookingConfirmation:
        return self._confirmation

    def get_error_message(self) -> str:
        return self._error_message

    # Utility methods

    @staticmethod
    def success(confirmation: BookingConfirmation):
        return BookingResult(BookingStatus.SUCCESS, confirmation, None)

    @staticmethod
    def not_available(error_message: str):
        return BookingResult(BookingStatus.NOT_AVAILABLE, None, error_message)

    @staticmethod
    def payment_failed(error_message):
        return BookingResult(BookingStatus.PAYMENT_FAILED, None, error_message)