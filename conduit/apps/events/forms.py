from django import forms
from .models import Event, Ticket, Organizer

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'organizer']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['event', 'user']

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['name']