# Імпортуємо усі необхідні модулі \ Import all necessary modules
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import random
from registration1.models import Code_Number
from django.contrib.auth.models import User
from django.http import  HttpRequest


# Створюємо функцію відображення render_authorithation1 \ Create the render_authorithation1 display function
def render_authorithation1(request: HttpRequest):
    # Створюємо об'єкт помилки \ Creating an error object
    error = ""
    # Створюємо умову, якщо користувач відправив форму \ We create a condition if the user submitted the form
    if request.method == "POST":
        # Получаємо дані з input \ Getting data from the inputs
        username = request.POST.get("name")
        password = request.POST.get("password")
        # Перевіряємо, чи існує користувач у базі даних \ Checking if a user exists in the database
        user = authenticate(request, username= username, password = password)
        # Створюємо оператор try, щоб в разі помилки сервер не закрився \ We create a try statement so that in case of an error the server does not close
        try:
            # Якщо користувач існує - створюємо випадковий 6-значний код та переадресуємо його на 2 етап авторизації \ If the user exists - we generate a random 6-digit code and redirect it to the 2nd stage of authorization
            if user != None:
                # Авторизуємо користувача \ Login user
                login(request, user)
                # Створюємо випадковий 6-значний код та зберігаємо його в базі даних \ We generate a random 6-digit code and save it in the database
                random_number = random.randint(99999, 999999)
                Code_Number.objects.create(number = random_number, user_id = user.id)   
                # Переадресуємо користувача на 2 етап перевірки \ Redirect the user to the 2nd stage of verification
                return redirect('/authorithation/loginemail/')
            # Якщо користувача не знайдено \ If user does not exist
            else:
                # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
                error = "Не вірний пароль або ім'я"
        # Робимо виключення \ Throw an exception
        except:
            # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
            error = "Не вірний пароль або ім'я"
    # Відображаємо сторінку з додатковим параметром context, через який ми відображаємо на сторінці помилку \ We display the page with an additional context parameter, through which we display an error on the page
    return render(request, "authorithation1/index.html",  context= {"error": error})