from django.shortcuts import render
from django.contrib.auth.models import User
from qrgenerate_app.models import QR_Codes
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from dateutil import parser
from dateutil.relativedelta import relativedelta
@login_required
def render_my_codes(request):
    specific_qrcode = None
    date_expire = None
    date = None
    if request.method == "POST":
        if request.POST.get("button-delete") is not None:
            try:
                qrcode_id = request.COOKIES["qrcode"]
                qrcode = QR_Codes.objects.get(id = qrcode_id)
                qrcode.delete()
            except:
                pass
        else:
            try:
                specific_qrcode_id = request.COOKIES["specificQrcodeID"]
                specific_qrcode = QR_Codes.objects.get(id = specific_qrcode_id)
                date_parse = parser.parse(specific_qrcode.date_created, dayfirst=True)
                date_expire = date_parse + relativedelta(months = 6)   
                date_expire_code = date_expire.strftime("%Y-%m-%d %H:%M:%S")
                date = f"{date_expire_code.split(':')[0].split('-')[2].split(' ')[0]}.{date_expire_code.split(':')[0].split('-')[1].split(' ')[0]} {date_expire_code.split(':')[0].split(' ')[1]}:{date_expire_code.split(':')[1].split('-')[0].split(' ')[0]}"
                   
            except:
                pass
    return render(request, "my_codes/my_codes.html", context = {
        "User": User.objects.all(),
        "QR_Codes": QR_Codes.objects.all(),
        "specific_qrcode": specific_qrcode,
        "date_expired": date
    })