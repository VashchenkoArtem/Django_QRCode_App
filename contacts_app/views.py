# Імпортуємо усі необхідні модулі \ Import all necessary modules
from django.shortcuts import render
from django.http import  HttpRequest

# Створюємо функцію відображення render_home_app \ Create the render_home_app display function
def render_contacts(request: HttpRequest):
    # Повертаємо нашу відоборажену сторінку \ Returning our displayed page 
    return render(request, 'contacts_app/contacts.html')
