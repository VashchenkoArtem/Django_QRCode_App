from django.shortcuts import render
from django.contrib.auth.models import User
from qrgenerate_app.models import QR_Codes
from django.http import HttpResponse


def render_my_codes(request):
    
    return render(request, "my_codes/my_codes.html", context = {
        "User": User.objects.all(),
        "QR_Codes": QR_Codes.objects.all()
    })