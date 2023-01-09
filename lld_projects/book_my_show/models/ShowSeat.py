from django.db import models

from book_my_show.models.Seat import Seat
from book_my_show.models.Show import Show
from book_my_show.models.Transaction import Transaction


class ShowSeat(models.Model):

    class SeatStatus(models.TextChoices):
        AVAILABLE = 'AVL', 'Available'
        BOOKED = "BOK", 'Booked'

    seat = models.OneToOneField(Seat,
                                on_delete=models.CASCADE,
                                primary_key=True)
    show = models.OneToOneField(Show, on_delete=models.CASCADE)
    status = models.CharField(max_length=3,
                              choices=SeatStatus.choices,
                              default=SeatStatus.AVAILABLE)
    ticket = models.ForeignKey(Transaction, on_delete=models.CASCADE)
