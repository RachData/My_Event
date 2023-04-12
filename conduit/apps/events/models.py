#from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    city = models.CharField(max_length=100)
    organizer = models.ForeignKey('Organizer', on_delete=models.CASCADE)

class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes/')

class Organizer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
