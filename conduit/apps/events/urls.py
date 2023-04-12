
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, TicketViewSet, OrganizerViewSet

router = DefaultRouter()
router.register('events', EventViewSet, basename='events')
router.register('tickets', TicketViewSet, basename='tickets')
router.register('organizers', OrganizerViewSet, basename='organizers')

urlpatterns = [
    path('', include(router.urls)),
    #path('api/', include(('conduit.apps.events.urls', 'events'), namespace='events')),
]
