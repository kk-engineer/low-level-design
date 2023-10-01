import datetime


class AccommodationDetailsService:

    def update_accommodation_details(self, accommodation_id: str,
                                     check_in_date: datetime,
                                     check_out_date: datetime):
        # Logic to update accommodation details
        print("Updated accommodation details: ", accommodation_id)
