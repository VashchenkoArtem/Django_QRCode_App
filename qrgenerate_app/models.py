from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class QR_Codes(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 255, null = True)
    url = models.TextField(null = True)
    image = models.ImageField(upload_to = "", null = True)
    date_created = models.CharField(max_length = 15)
    is_working = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class Redirect_QR(models.Model):
    qrcode = models.CharField(max_length = 255)
    url = models.URLField()
    qr = models.OneToOneField(to = QR_Codes, on_delete= models.CASCADE, null = True)

    def get_absolute_url(self):
        return reverse('checking', args=[self.qr_id])
