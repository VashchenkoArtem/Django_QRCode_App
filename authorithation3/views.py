# Імпортуємо усі необхідні модулі \ Import all necessary modules
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import  HttpRequest


# Створюємо функцію відображення render_authorithation3 \ Create the render_authorithation3 display function
def render_authorithation3(request: HttpRequest):
    # Створюємо умову, якщо користувач натиснув на кнопку \ We create a condition if the user clicks the button 
    if request.method == 'POST':
        # Переадресовуємо користувача на головну сторінку \ Redirect user to main page
        return redirect("/")
    # Відображаємо сторінку авторизаці3 \ Display the authorization3 page
    return render(request, "authorithation3/authorithation3.html")

# Створюємо функцію для вихoду з акаунту \ Create function for exit from acount
def logout_user(request: HttpRequest):
    # Виходимо з аканту \ Exit from acount
    logout(request)
    # Переадресовуємо користувача на головну сторінку \ Redirect user to main page
    return redirect("/")