from ..models.payment_status import PaymentStatus


class PaymentService:

    def make_payment(self, user_id: str,
                     accommodation_id: str) -> PaymentStatus:
        # Logic to process payment
        print("Processing payment for user: ", user_id)
        return PaymentStatus.SUCCESS  # Placeholder

    def calculate_payment_amount(self, accommodation_id: str) -> float:
        # Logic to calculate payment amount
        return 10000    # Placeholder
