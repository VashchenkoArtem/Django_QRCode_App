from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.core.mail import send_mail
from .models import Code_Number
from django.contrib.auth import authenticate, login

import random
# Create your views here.
random_number = 0
def render_registration1(request):
    global random_number
    error = ""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            User.objects.create_user(username= name, email= email, password= password)
            error = ""
            return redirect("/registration/succesregistration/")
            
        except IntegrityError:
            error = "Такий користувач вже існує!"
        except ValueError:
            error = "Поля не можуть бути пустими!"
    return render(request, "registration1/registration1.html",  context= {"error": error})
