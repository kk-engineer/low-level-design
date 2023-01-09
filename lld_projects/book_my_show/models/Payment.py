import uuid

from django.db import models

from book_my_show.models import MovieTicket


class Payment(models.Model):
    class PaymentMode(models.TextChoices):
        NETBANKING = 'NET', 'Net Banking'
        DEBIT = "DBT", 'Debit Card'
        CREDIT = 'CRD', 'Credit Card'
        UPI = 'UPI', 'Unified Payment Interface'

    class PaymentStatus(models.TextChoices):
        SUCCESS = 'SUC', 'Success'
        FAILURE = 'FAL', 'Failure'

    payment_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    #ticket = models.OneToOneField(MovieTicket, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    mode = models.CharField(max_length=3,
                            choices=PaymentMode.choices,
                            default=PaymentMode.UPI)
    status = models.CharField(max_length=3,
                              choices=PaymentStatus.choices,
                              default=PaymentStatus.SUCCESS)

    def __str__(self):
        return str(self.payment_id)