import uuid

from django.db import models

from book_my_show.models.Screen import Screen
from book_my_show.models.Theatre import Theatre


class Seat(models.Model):
    class SeatType(models.TextChoices):
        ROYAL = 'RYL', 'Royale'
        CLUB = 'CLB', 'Club'
        EXECUTIVE = 'EXC', 'Executive'

    seat_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    row = models.CharField(max_length=1)
    column = models.IntegerField()
    type = models.CharField(max_length=3,
                            choices=SeatType.choices,
                            default=SeatType.EXECUTIVE)
    screen = models.ManyToManyField(Screen)
    theatre = models.ManyToManyField(Theatre)

    def __str__(self):
        return str(self.row) + str(self.column)