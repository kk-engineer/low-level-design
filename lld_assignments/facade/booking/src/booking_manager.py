import datetime
from .services.accommodation_details_service import AccommodationDetailsService
from .services.availability_service import AvailabilityService
from .services.loyalty_service import LoyaltyService
from .services.notification_service import NotificationService
from .services.payment_service import PaymentService
from .booking_processor import BookingProcessor
from .models.booking_result import BookingResult


class BookingManager:

    def __init__(self, accommodation_details_service: AccommodationDetailsService,
                 availability_service: AvailabilityService,
                 loyalty_service: LoyaltyService,
                 notification_service: NotificationService,
                 payment_service: PaymentService):
        self._booking_processor = BookingProcessor(accommodation_details_service,
                                                   availability_service,
                                                   loyalty_service,
                                                   notification_service,
                                                   payment_service)

    def book_accommodation(self, user_id: str,
                           accommodation_id: str,
                           check_in_date: datetime,
                           check_out_date: datetime) -> BookingResult:
        return self._booking_processor.process(user_id,
                                               accommodation_id,
                                               check_in_date,
                                               check_out_date)
