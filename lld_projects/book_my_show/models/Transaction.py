import uuid

from django.db import models

from book_my_show.models.MovieTicket import MovieTicket
from book_my_show.models.Payment import Payment


class Transaction(models.Model):
    class TransactionStatus(models.TextChoices):
        INPROGRESS = 'PRG', 'In Progress'
        SUCCESS = 'SUC', 'Success'
        FAILURE = 'FAL', 'Failure'

    transaction_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    ticket = models.ForeignKey(MovieTicket, on_delete=models.CASCADE, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=3,
                              choices=TransactionStatus.choices,
                              default=TransactionStatus.INPROGRESS)
