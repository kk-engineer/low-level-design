import datetime


class AvailabilityService:

    def check_availability(self, accommodation_id: str,
                           check_in_date: datetime,
                           check_out_date: datetime):
        print("Checking availability for check in date: ", check_in_date)
        return True  # Placeholder
