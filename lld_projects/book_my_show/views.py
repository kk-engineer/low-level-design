from datetime import datetime

from django.shortcuts import render, redirect


# Create your views here.


def home_page(request):
    return render(request, 'bms/index.html', context={
        'curr_date': str(datetime.utcnow()),
    })


def book_ticket(request):
    return render(request, 'bms/book_ticket.html', context={
        'curr_date': str(datetime.utcnow()),
    })


def make_payment(request):
    pass
