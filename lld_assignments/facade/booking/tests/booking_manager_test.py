import unittest
import datetime
from ..src.services.accommodation_details_service import AccommodationDetailsService
from ..src.services.availability_service import AvailabilityService
from ..src.services.loyalty_service import LoyaltyService
from ..src.services.notification_service import NotificationService
from ..src.services.payment_service import PaymentService
from ..src.booking_manager import BookingManager


class TestBookingManager(unittest.TestCase):

    def test_booking_process(self):
        accommodation_details_service = AccommodationDetailsService()
        availability_service = AvailabilityService()
        loyalty_service = LoyaltyService()
        notification_service = NotificationService()
        payment_service = PaymentService()

        booking_manager = BookingManager(accommodation_details_service,
                                         availability_service,
                                         loyalty_service,
                                         notification_service,
                                         payment_service)
        user_id = "123"
        accommodation_id = "ABC_123"
        check_in_date = datetime.date(2023, 12, 25)
        check_out_date = datetime.date(2024, 1, 2)

        booking_manager.book_accommodation(user_id,
                                           accommodation_id,
                                           check_in_date,
                                           check_out_date)


