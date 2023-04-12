from rest_framework import viewsets, filters
from .models import Event, Ticket, Organizer
from .serializers import EventSerializer, TicketSerializer, OrganizerSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, EventForm, TicketForm, OrganizerForm


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['city']

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

def event_list(request):
    = request.GET.get('city')
    if query:
        events = Event.objects.filter(location__icontains=query)
    else:
        events = Event.objects.all()
    context = {'events': events}
    return render(request, 'events/event_list.html', context)

@login_required
def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {'event': event}
    return render(request, 'events/event_detail.html', context)

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user.organizer
            event.save()
            messages.success(request, f'Votre événement a été créé avec succès!')
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

@login_required
def buy_ticket(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.event = event
            ticket.save()
            ticket.generate_qr_code()
            ticket.save()
            messages.success(request, f'Votre billet a été acheté avec succès!')
            return redirect('event_detail', event_id=event.id)
    else:
        form = TicketForm()
    return render(request, 'events/buy_ticket.html', {'form': form, 'event': event})

@login_required
def create_organizer(request):
    if request.method == 'POST':
        form = OrganizerForm(request.POST)
        if form.is_valid():
            organizer = form.save(commit=False)
            organizer.user = request.user
            organizer.save()
            messages.success(request, f'Votre compte organisateur a été créé avec succès!')
            return redirect('profile')
    else:
        form = OrganizerForm()
    return render(request, 'events/create_organizer.html', {'form': form})