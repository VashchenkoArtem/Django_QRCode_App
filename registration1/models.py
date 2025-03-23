# Імпортуємо модуль models з django \ Import the models module from django
from django.db import models

# Оголошуємо модель Code_Number \ Declare the Code_Number model
class Code_Number(models.Model):
    # Поле для збереження числа \ Field to store the number
    number = models.SmallIntegerField()
    # Поле для збереження ID користувача \ Field to store the user ID
    user_id = models.SmallIntegerField()
