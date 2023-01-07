from django import forms
from django.db.models import TextField
from django.forms import Textarea

from parking_lot.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['vehicle', 'entry_time', 'status', 'spot_number', 'floor_number']
        widgets = {
            'vehicle': Textarea(attrs={'cols': 10, 'rows': 1}),
        }