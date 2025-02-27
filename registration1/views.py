from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.core.mail import send_mail
from .models import Code_Number
from django.contrib.auth import authenticate, login
from django.http import  HttpRequest
import random
# Create your views here.
random_number = 0
def render_registration1(request: HttpRequest):
    global random_number
    error = ""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")
        
        if password == confirm_password:           
            try:
                User.objects.create_user(username= name, email= email, password= password)
                error = ""
                return redirect("/registration/succesregistration/")
                
            except IntegrityError:
                error = "Такий користувач вже існує!"
            except ValueError:
                error = "Поля не можуть бути пустими!"
            except:
                error = "Користувача не знайдено"
        else:
            error = "Паролі не співпадають"
    return render(request, "registration1/registration1.html",  context= {"error": error})
