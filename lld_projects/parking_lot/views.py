from django.shortcuts import render, redirect
from datetime import datetime, timezone

# Create your views here.
from parking_lot.forms import TicketForm
from parking_lot.models import ParkingSpot, Vehicle


def index_page(request):
    return render(request, 'parkingLot/index.html', context={
        'curr_date': str(datetime.utcnow()),
    })


def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(data=request.POST)
        #vehicle = request.vehicle
        #Vehicle.objects.get_or_create(testkey=Vehicle(registration=vehicle.registration))
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = TicketForm()
    return render(request, 'parkingLot/ticket.html', {'form': form})



def get_spots(request):
    spots = ParkingSpot.objects.all()
    return render(request, 'parkingLot/display.html', {'spots': spots})
