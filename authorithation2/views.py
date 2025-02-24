from django.shortcuts import render, redirect
import random
from django.core.mail import send_mail
from registration1.models import Code_Number
from django.http import  HttpRequest
# Create your views here.
def render_authorithation2(request: HttpRequest):
    error = ""
    try:
        if request.user.is_authenticated:
            random_number = Code_Number.objects.get(user_id = request.user.id).number
            print("123")
            send_mail(
                subject = "Код для підтвердження",
                message = f"Вітаємо!\n ваш код для підтвердження: {random_number}",
                from_email = "qrprojectdjangoteam2@gmail.com",
                recipient_list = [f"{request.user.email}"],
                fail_silently = False
                )
            print("123")
            if request.method == "POST":
                email_code = request.POST.get("email_code")
                if int(email_code) == random_number:
                    Code_Number.objects.get(user_id = request.user.id).delete()
                    return redirect("/authorithation/succesauthorithation/")
                else:
                    print("error")
                    error = "Код підтвердження не вірний!"
    except:
        Code_Number.objects.filter(user_id = request.user.id).delete()
    return render(request, "authorithation2/index.html", context= {"error": error})