from django.contrib import admin
from parking_lot.models import ParkingLot
from parking_lot.models import ParkingFloor
from parking_lot.models import ParkingSpot
from parking_lot.models import Ticket
from parking_lot.models import Operator
from parking_lot.models import Vehicle

# Register your models here.

admin.site.register(ParkingLot)
admin.site.register(ParkingFloor)
admin.site.register(ParkingSpot)
admin.site.register(Operator)
admin.site.register(Ticket)
admin.site.register(Vehicle)