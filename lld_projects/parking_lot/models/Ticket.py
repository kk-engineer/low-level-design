from django.db import models
from parking_lot.models.Vehicle import Vehicle
from parking_lot.models.VehicleType import VehicleType
from parking_lot.models.ParkingFloor import ParkingFloor
from parking_lot.models.ParkingSpot import ParkingSpot


class TicketStatus(models.TextChoices):
    DONE = 'DON', 'Done'
    PENDING = "PEN", 'Pending'


class Ticket(models.Model):
    ticket_id = models.TextField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    spot_number = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    floor_number = models.ForeignKey(ParkingFloor, on_delete=models.CASCADE)
    entry_time = models.DateTimeField
    exit_time = models.DateTimeField
    status = models.CharField(max_length=3,
                              choices=TicketStatus.choices,
                              default=TicketStatus.PENDING)

    def __str__(self):
        return self.ticket_id
