import uuid

from django.db import models


class Operator(models.Model):
    operator_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.TextField()
    email = models.EmailField()
    phone_number = models.TextField()

    def __str__(self):
        return self.name
