from django.db import models
from parking_lot.models.ParkingLot import ParkingLot


class ParkingFloor(models.Model):
    floor_number = models.IntegerField
    name = models.TextField()
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
