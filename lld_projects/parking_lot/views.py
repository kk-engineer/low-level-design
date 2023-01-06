from django.shortcuts import render
from datetime import datetime


# Create your views here.

def index_page(request):
    return render(request, 'index.html', context={
        'curr_date': str(datetime.now()),
    })
