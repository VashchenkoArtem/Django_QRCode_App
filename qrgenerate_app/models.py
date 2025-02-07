from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class QR_Codes(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 255, null = True)
    url = models.TextField(null = True)
    image = models.ImageField(upload_to = "", null = True)
    date_created = models.DateTimeField(auto_now = True)