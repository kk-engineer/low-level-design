import datetime

from .services.accommodation_details_service import AccommodationDetailsService
from .services.availability_service import AvailabilityService
from .services.loyalty_service import LoyaltyService
from .services.notification_service import NotificationService
from .services.payment_service import PaymentService
from .models.booking_result import BookingResult
from .models.booking_confirmation import BookingConfirmation
from .models.payment_status import PaymentStatus


class BookingProcessor:

    def __init__(self, accommodation_details_service: AccommodationDetailsService,
                 availability_service: AvailabilityService,
                 loyalty_service: LoyaltyService,
                 notification_service: NotificationService,
                 payment_service: PaymentService):
        self._accommodation_details_service = accommodation_details_service
        self._availability_service = availability_service
        self._loyalty_service = loyalty_service
        self._notification_service = notification_service
        self._payment_service = payment_service

    def process(self, user_id: str,
                accommodation_id: str,
                check_in_date: datetime,
                check_out_date: datetime) -> BookingResult:
        is_available = self._availability_service.check_availability(accommodation_id,
                                                                     check_in_date,
                                                                     check_out_date)
        if not is_available:
            return BookingResult.not_available("Accommodation not available for the given dates")

        payment_status = self._payment_service.make_payment(user_id, accommodation_id)
        if payment_status != PaymentStatus.SUCCESS:
            return BookingResult.payment_failed("Payment failed with status:" +
                                                str(payment_status))

        confirmation = BookingConfirmation(user_id,
                                           accommodation_id,
                                           check_in_date,
                                           check_out_date)

        self._notification_service.send_booking_confirmation(confirmation)
        self._loyalty_service.update_loyalty_points(user_id,
                                                    self._payment_service.calculate_payment_amount(accommodation_id))
        self._accommodation_details_service.update_accommodation_details(accommodation_id,
                                                                         check_in_date,
                                                                         check_out_date)
        return BookingResult.success(confirmation)