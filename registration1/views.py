# Імпортуємо усі необхідні модулі \ Import all necessary modules
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.core.mail import send_mail
from .models import Code_Number
from django.contrib.auth import authenticate, login
from django.http import  HttpRequest


# Створюємо функцію відображення render_registration1 \ Create the render_registration1 display function
def render_registration1(request: HttpRequest):
    # Створюємо об'єкт помилки \ Creating an error object
    error = ""
    # Створюємо умову, якщо користувач відправив форму \ We create a condition if the user submitted the form
    if request.method == "POST":
        # Получаємо дані з input \ Getting data from the inputs
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")
        # Якщо поле пароля та поле підтвердження пароля однакові \ If the password field and the password confirmation field are the same
        if password == confirm_password:      
            # Створюємо оператор try, щоб в разі помилки сервер не закрився \ We create a try statement so that in case of an error the server does not close
            try:
                # Створюємо нового користувача з введеними даними \ Сreate a new user with the entered data
                User.objects.create_user(username= name, email= email, password= password)
                error = ""
                # Переадресуємо користувача на сторінку успішної реєстрації \ Redirect the user to the successful registration page
                return redirect("/registration/succesregistration/")
            # Робимо виключення, якщо користувач вже існує \ Throw an exception if the user already exists
            except IntegrityError:
                # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
                error = "Такий користувач вже існує!"
            # Робимо виключення, якщо форма пуста \ Throw an exception if the form is empty
            except ValueError:
                # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
                error = "Поля не можуть бути пустими!"
            # Робимо виключення \ Throw an exception
            except:
                # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
                error = "Користувача не знайдено"
        # Якщо поля не співпадають \ If the fields do not match
        else:
            #                 # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
            error = "Паролі не співпадають"
    # Відображаємо сторінку з додатковим параметром context, через який ми відображаємо на сторінці помилку \ We display the page with an additional context parameter, through which we display an error on the page
    return render(request, "registration1/registration1.html",  context= {"error": error})
