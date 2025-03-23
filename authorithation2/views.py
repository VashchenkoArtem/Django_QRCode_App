# Імпортуємо усі необхідні модулі \ Import all necessary modules
from django.shortcuts import render, redirect
import random
from django.core.mail import send_mail
from registration1.models import Code_Number
from django.http import  HttpRequest


# Створюємо функцію відображення render_authorithation2 \ Create the render_authorithation2 display function
def render_authorithation2(request: HttpRequest):
    # Створюємо об'єкт помилки \ Creating an error object
    error = ""
    # Створюємо оператор try, щоб в разі помилки сервер не закрився \ We create a try statement so that in case of an error the server does not close
    try:
        # Перевіряємо чи користувач вже авторизований \ Checking if the user is already authenticated
        if request.user.is_authenticated:
            # Отримуємо з бази даних випадковий код за id користувача \ We get a random code from the database by user id
            random_number = Code_Number.objects.get(user_id = request.user.id).number
            # Відправляємо лист на електронну пошту з випадковим кодом \ We send an email with a random code
            send_mail(
                subject = "Код для підтвердження",
                message = f"Вітаємо!\n ваш код для підтвердження: {random_number}",
                from_email = "qrprojectdjangoteam2@gmail.com",
                recipient_list = [f"{request.user.email}"],
                fail_silently = False
                )
            # Створюємо умову, якщо користувач відправив форму \ We create a condition if the user submitted the form
            if request.method == "POST":
                # Получаємо дані з input \ Getting data from the inputs
                email_code = request.POST.get("email_code")
                # Перевіряємо чи введений код однаковий з випадковим \ Checking if the entered code matches the random one
                if int(email_code) == random_number:
                    # Видаляємо з бази даних старий код \ We delete the old code from the database
                    Code_Number.objects.get(user_id = request.user.id).delete()
                    # Відправляємо користувача на сторінку успішної авторизації \ We send the user to the success authorithation page
                    return redirect("/authorithation/succesauthorithation/")
                # Якщо код підтвердженян не співпадає з відправленим кодом на пошту \ If the confirmation code does not match the code sent to the email
                else:
                    # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
                    error = "Код підтвердження не вірний!"
    # Робимо виключення \ Throw an exception
    except:
        # Отримуємо всі старі коди по id користувача та видаляємо їх \ We get all old codes by user id and delete them 
        Code_Number.objects.filter(user_id = request.user.id).delete()
        # Відображаємо сторінку з додатковим параметром context, через який ми відображаємо на сторінці помилку \ We display the page with an additional context parameter, through which we display an error on the page
    return render(request, "authorithation2/index.html", context= {"error": error})