
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, TicketViewSet, OrganizerViewSet
from . import views

router = DefaultRouter()
router.register('events', EventViewSet, basename='events')
router.register('tickets', TicketViewSet, basename='tickets')
router.register('organizers', OrganizerViewSet, basename='organizers')

urlpatterns = [
    path('', include(router.urls)),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/<int:event_id>/buy_ticket/', views.buy_ticket, name='buy_ticket'),
    path('events/organizer/create/', views.create_organizer, name='create_organizer'),
    #path('api/', include(('conduit.apps.events.urls', 'events'), namespace='events')),
    #path('api/', include(('conduit.apps.events.urls', 'events'), namespace='events')),
]

