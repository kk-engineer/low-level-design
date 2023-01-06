from django.db import models
from parking_lot.models.Gate import EntryGate


class DisplayBoard(models.Model):
    entry_gate = models.ForeignKey(EntryGate, on_delete=models.CASCADE)
