from django.shortcuts import render
from django.http import  HttpRequest


def render_home_app(request: HttpRequest):
    return render(request, "home_app/home.html")
