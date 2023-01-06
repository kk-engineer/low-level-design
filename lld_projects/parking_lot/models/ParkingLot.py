from django.db import models


class ParkingLot(models.Model):
    name = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name
