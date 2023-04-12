#from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
import qrcode
from io import BytesIO
from django.core.files import File

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    city = models.CharField(max_length=100)
    organizer = models.ForeignKey('Organizer', on_delete=models.CASCADE)

class Ticket(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    
    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
           )
        qr.add_data(self.id)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img_buffer = BytesIO()
        img.save(img_buffer, format='PNG')
        self.qr_code.save(f"ticket_{self.id}.png", File(img_buffer), save=False)

class Organizer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    events = models.ManyToManyField('Event', related_name='organizers')

