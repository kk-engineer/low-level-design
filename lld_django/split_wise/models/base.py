from django.db import models
from django.utils.timezone import now

class Base(models.Model):
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)