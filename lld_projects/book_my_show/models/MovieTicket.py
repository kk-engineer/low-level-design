import uuid

from django.db import models

from book_my_show.models.User import User


class MovieTicket(models.Model):
    ticket_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ticket_id)
