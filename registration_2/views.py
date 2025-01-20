from django.shortcuts import render
from django.core.mail import send_mail
from registration1.views import random_number
from registration1.models import Code_Number

# Create your views here.
def render_registration2(request):
    error = ''
    if request.method == "POST":
        code = request.POST.get("code")
        
    return render(request, "registration_2/index.html")
