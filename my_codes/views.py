from django.shortcuts import render
from django.contrib.auth.models import User
from qrgenerate_app.models import QR_Codes
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# @login_required
def render_my_codes(request):
    if request.method == "POST":
        try:
            qrcode_id = request.COOKIES["qrcode"]
            qrcode = QR_Codes.objects.get(id = qrcode_id)
            qrcode.delete()
        except:
            pass
    return render(request, "my_codes/my_codes.html", context = {
        "User": User.objects.all(),
        "QR_Codes": QR_Codes.objects.all()
    })