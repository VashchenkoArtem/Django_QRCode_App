from django.shortcuts import render, redirect
from django.http import  HttpRequest
# Create your views here.

def render_registration3(request: HttpRequest):
    if request.method == 'POST':
        return redirect("/authorithation/logininformation/")
    return render(request, "registration3/registration3.html")

