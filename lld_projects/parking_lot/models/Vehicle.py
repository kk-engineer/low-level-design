from django.db import models
from parking_lot.models.VehicleType import VehicleType


class Vehicle(models.Model):
    registration = models.CharField(max_length=10, primary_key=True)
    vehicle_type = models.CharField(max_length=1,
                                    choices=VehicleType.choices,
                                    default=VehicleType.SMALL)

    def __str__(self):
        return self.registration
