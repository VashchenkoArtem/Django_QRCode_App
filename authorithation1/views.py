from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import random
from registration1.models import Code_Number
from django.contrib.auth.models import User
from django.http import  HttpRequest
# Create your views here.
def render_authorithation1(request: HttpRequest):
    error = ""
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")

        user = authenticate(request, username= username, password = password)
        try:
            if user != None:
                login(request, user)
                random_number = random.randint(99999, 999999)
                Code_Number.objects.create(number = random_number, user_id = user.id)   

                return redirect('/authorithation/loginemail/')
            else:
                error = "Не вірний пароль або ім'я"
        except:
            error = "Не вірний пароль або ім'я"
    return render(request, "authorithation1/index.html",  context= {"error": error})