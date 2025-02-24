from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from qrgenerate_app.models import QR_Codes
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from dateutil import parser
from dateutil.relativedelta import relativedelta


from subscribe.models import UserSubscribe
@login_required
def render_my_codes(request: HttpRequest):
    specific_qrcode = None
    date_expire = None
    date = None
    delete = None

    if request.method == "POST":

        if request.POST.get("button-delete") is not None:
            delete = 1
        if request.POST.get("form-delete") is not None:
            try:
                qrcode_id = request.COOKIES["qrcode"]
                qrcode = QR_Codes.objects.get(id = qrcode_id)
                qrcode.delete()
                return redirect("my_codes")
            except:
                pass
        else:
            if request.COOKIES["specificQrcodeID"]:
                specific_qrcode_id = request.COOKIES["specificQrcodeID"]
                specific_qrcode = QR_Codes.objects.get(id = specific_qrcode_id)
                date_parse = parser.parse(specific_qrcode.date_created, dayfirst=True)
                date_expire = date_parse + relativedelta(months = 6)   
                date_expire_code = date_expire.strftime("%Y-%m-%d %H:%M:%S")
                date = f"{date_expire_code.split(':')[0].split('-')[2].split(' ')[0]}.{date_expire_code.split(':')[0].split('-')[1].split(' ')[0]} {date_expire_code.split(':')[0].split(' ')[1]}:{date_expire_code.split(':')[1].split('-')[0].split(' ')[0]}"


    return render(request, "my_codes/my_codes.html", context = {
        "User": User.objects.all(),
        "QR_Codes": QR_Codes.objects.all(),
        "specific_qrcode": specific_qrcode,
        "date_expired": date,
        "delete": delete,
        "date_expired": date
    })