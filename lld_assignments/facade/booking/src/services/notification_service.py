from ..models.booking_confirmation import BookingConfirmation


class NotificationService:

    def send_booking_confirmation(self, confirmation: BookingConfirmation):
        # Logic to send booking confirmation notification
        print("Sending booking confirmation for user: ", confirmation.get_user_id())
        print("Accomodation id: ", confirmation.get_accommodation_id())
        print("Check in date: ", confirmation.get_check_in_date())
        print("Check out date: ", confirmation.get_check_out_date())