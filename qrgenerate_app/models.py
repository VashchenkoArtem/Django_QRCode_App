# Імпортуємо модулі для роботи з моделями, користувачами та URL \ Import modules for working with models, users, and URLs
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Створюємо модель QR_Codes \ Create QR_Codes model
class QR_Codes(models.Model):
    # Поле для збереження користувача, який створив QR-код \ Field to store the user who created the QR code
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    # Поле для збереження назви QR-коду \ Field to store the name of the QR code
    name = models.CharField(max_length = 255, null = True)
    # Поле для збереження URL, пов'язаного з QR-кодом \ Field to store the URL associated with the QR code
    url = models.TextField(null = True)
    # Поле для збереження зображення QR-коду \ Field to store the image of the QR code
    image = models.ImageField(upload_to = "", null = True)
    # Поле для збереження дати створення QR-коду \ Field to store the creation date of the QR code
    date_created = models.CharField(max_length = 15)
    # Поле для визначення чи працює QR-код \ Field to determine if the QR code is active
    is_working = models.BooleanField(default = True)
    # Строкове представлення об'єкта QR_Codes \ String representation of the QR_Codes object
    def __str__(self):
        return self.name

# Створюємо модель Redirect_QR \ Create Redirect_QR model
class Redirect_QR(models.Model):
    # Поле для збереження коду QR \ Field to store the QR code
    qrcode = models.CharField(max_length = 255)
    # Поле для збереження URL перенаправлення \ Field to store the redirect URL
    url = models.URLField()
    # Однонаправлене посилання на модель QR_Codes \ One-to-one link to QR_Codes model
    qr = models.OneToOneField(to = QR_Codes, on_delete= models.CASCADE, null = True)
    # Метод для отримання абсолютного URL для редиректу \ Method to get the absolute URL for the redirect
    def get_absolute_url(self):
        return reverse('checking', args=[self.qr_id])
