# Імпортуємо усі необхідні модулі \ Import all necessary modules
from django.shortcuts import render, redirect
from django.http import  HttpRequest


# Створюємо функцію відображення render_registration1 \ Create the render_registration1 display function
def render_registration3(request: HttpRequest):
    # Створюємо умову, якщо користувач натиснув на кнопку \ We create a condition if the user clicks the button 
    if request.method == 'POST':
        # Переадресуємо користувача на авторизацію \ Redirect user to autorithation page
        return redirect("/authorithation/logininformation/")
    # Відображаємо сторінку \ Display page
    return render(request, "registration3/registration3.html")

