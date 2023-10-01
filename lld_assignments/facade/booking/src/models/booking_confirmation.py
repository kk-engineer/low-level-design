import datetime


class BookingConfirmation:

    def __init__(self, user_id: str,
                 accommodation_id: str,
                 check_in_date: datetime,
                 check_out_date: datetime):
        self._user_id = user_id
        self._accommodation_id = accommodation_id
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date

    # Getters

    def get_user_id(self):
        return self._user_id

    def get_accommodation_id(self):
        return self._accommodation_id

    def get_check_in_date(self):
        return self._check_in_date

    def get_check_out_date(self):
        return self._check_out_date
