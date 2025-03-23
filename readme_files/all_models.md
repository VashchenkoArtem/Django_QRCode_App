# Всі models.py в проєкті \ All models.py at project

## Code_Number
```python
# Імпортуємо модуль models з django \ Import the models module from django
from django.db import models

# Оголошуємо модель Code_Number \ Declare the Code_Number model
class Code_Number(models.Model):
    # Поле для збереження числа \ Field to store the number
    number = models.SmallIntegerField()
    # Поле для збереження ID користувача \ Field to store the user ID
    user_id = models.SmallIntegerField()
```
Ця таблиця необхідна для **генерування** кода, який **відправляється** на **пошту** користувачу під час **авторизації** \ This table is needed to **generate** a code that is sent to the user's **email** during **authorization**.

## QR_Codes
```python
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
```
Ця таблиця **створена** для **збереження QR кодів** в ній \ This table **was created** to **store QR codes** in it
## Redirect_QR
```python
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
```
Ця таблиця **створена** для **збереження** в ній **адреси динамічного QR кода** \ This table **was created** to **store** the **dynamic QR code address**

## UserSubscribe
```python
# Імпортуємо модулі для роботи з моделями та користувачами \ Import modules for working with models and users
from django.db import models
from django.contrib.auth.models import User


# Створюємо модель UserSubscribe \ Create UserSubscribe model
class UserSubscribe(models.Model):
    # Поле для збереження користувача, який підписався \ Field to store the user who subscribed
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    # Поле для збереження типу підписки \ Field to store the subscription type
    subscribe_type = models.CharField(max_length= 20)
    # Поле для збереження номеру картки \ Field to store the card number
    card_number = models.CharField(max_length= 100)
    # Поле для збереження CVV коду \ Field to store the CVV code
    cvv_code = models.SmallIntegerField(null=True)
    # Поле для збереження дати підтвердження підписки \ Field to store the subscription confirmation date
    date_confirmed = models.DateField(auto_now_add=True)
    # Поле для збереження дати закінчення підписки \ Field to store the subscription expiration date
    date_expired = models.CharField(max_length = 20)
    # Поле для збереження дати закінчення терміну дії підписки \ Field to store the subscription expiration date
    date_expired_subscribe = models.DateField(null = True)
    # Поле для збереження максимальної кількості QR-кодів, доступних для користувача \ Field to store the max number of QR codes available to the user
    max_count_qrs = models.SmallIntegerField(null= True)
    # Поле для визначення, чи активна підписка \ Field to determine if the subscription is active
    is_working = models.BooleanField(default=True)
```
Ця таблиця **створеня** для **збереження** в ній **підписок** та **дані про підписку** кожного **користувача** \ This table **is** created to **store** each **user's** **subscriptions** and **subscription data** in it