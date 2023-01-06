from django.db import models
from parking_lot.models.Operator import Operator
from parking_lot.models.ParkingLot import ParkingLot


class Gate(models.Model):
    location = models.TextField
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class EntryGate(Gate):
    operator = models.ManyToManyField(Operator)


class ExitGate(Gate):
    pass
