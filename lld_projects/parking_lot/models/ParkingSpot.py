from django.db import models

from parking_lot.models.ParkingFloor import ParkingFloor
from parking_lot.models.VehicleType import VehicleType


class ParkingSpot(models.Model):

    class SpotStatus(models.TextChoices):
        AVAILABLE = 'AVL', 'Available'
        OCCUPIED = 'OCU', 'Occupied'
        OUTOFORDER = 'OOO', 'OutOfOrder'

    spot_id = models.IntegerField
    floor = models.ForeignKey(ParkingFloor, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=1,
                                    choices=VehicleType.choices,
                                    default=VehicleType.SMALL)
    spot_status = models.CharField(max_length=3,
                                   choices=SpotStatus.choices,
                                   default=SpotStatus.AVAILABLE)

    def __str__(self):
        return str(self.get_vehicle_type_display()) + " : " +\
               str(self.get_spot_status_display())