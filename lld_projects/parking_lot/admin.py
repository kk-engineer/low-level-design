from django.contrib import admin
from parking_lot.models import ParkingLot
from parking_lot.models import ParkingFloor
from parking_lot.models import ParkingSpot
from parking_lot.models import Ticket
from parking_lot.models import Operator
from parking_lot.models import Vehicle
from parking_lot.models import ParkingSpot


# Register your models here.

def mark_ooo(model_admin, request, queryset):
    queryset.update(
        spot_status=ParkingSpot.SpotStatus.OUTOFORDER
    )


mark_ooo.short_description = "Mark Out Of Order"


class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['vehicle_type', 'spot_status', 'floor', 'lot_name', 'link']
    list_editable = ['vehicle_type', 'spot_status', 'floor', 'lot_name', ]
    list_display_links = ['link']
    list_filter = ['vehicle_type', 'spot_status', 'floor', 'lot_name', ]
    actions = [mark_ooo]


class TicketAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'entry_time', 'status', 'spot_number', 'floor_number', 'link']
    list_editable = ['vehicle', 'entry_time', 'status', 'spot_number', 'floor_number']
    list_display_links = ['link']
    #list_filter = ['vehicle', 'entry_time', 'status', 'spot_number', 'floor_number']


class VehicleAdmin(admin.ModelAdmin):
    search_fields = ['registration']


admin.site.register(ParkingLot)
admin.site.register(ParkingFloor)
admin.site.register(ParkingSpot, ParkingSpotAdmin)
admin.site.register(Operator)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Vehicle, VehicleAdmin)
