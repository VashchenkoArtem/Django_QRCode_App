from django.db import models
from django.contrib.auth.models import User


class UserSubscribe(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    subscribe_type = models.CharField(max_length= 20)
    card_number = models.CharField(max_length= 100)
    cvv_code = models.SmallIntegerField(null=True)
    date_confirmed = models.DateField(auto_now_add=True)
    date_expired = models.CharField(max_length = 20)
    max_count_qrs = models.SmallIntegerField(null= True)
    