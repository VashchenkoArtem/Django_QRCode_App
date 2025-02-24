from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import  HttpRequest
# Create your views here.
def render_authorithation3(request: HttpRequest):
    if request.method == 'POST':
        return redirect("/")
    return render(request, "authorithation3/authorithation3.html")

def logout_user(request: HttpRequest):
    logout(request)
    return redirect("/")