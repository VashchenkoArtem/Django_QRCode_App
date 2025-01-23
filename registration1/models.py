from django.db import models

# Create your models here.
class Code_Number(models.Model):
    number = models.SmallIntegerField()
    user_id = models.SmallIntegerField()
