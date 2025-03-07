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

    subscribe_user = UserSubscribe.objects.get(user = request.user)
    if subscribe_user.is_working == False:
        all_user_qr = QR_Codes.objects.filter(user = request.user)

        for qrcode in all_user_qr:
            qrcode.is_working = False
            qrcode.save()
        all_user_qr[0].is_working = True
        all_user_qr[0].save()
    if subscribe_user.is_working == True:
        all_user_qr = QR_Codes.objects.filter(user = request.user)
        list_qrs = []
        for qrcode in all_user_qr:
            list_qrs.append(qrcode)
            if len(list_qrs) < subscribe_user.max_count_qrs:
                qrcode.is_working = True
                qrcode.save()
                
    if len(QR_Codes.objects.filter(user_id=request.user.id)) > subscribe_user.max_count_qrs:

        all_user_qr = QR_Codes.objects.filter(user = request.user)
        for qrcode in all_user_qr:
            qrcode.is_working = False
            qrcode.save()
        all_user_qr[0].is_working = True
        all_user_qr[0].save()
    if request.method == "POST":
        all_user_qr = QR_Codes.objects.filter(user = request.user)
        all_user_qr[0].is_working = True
        all_user_qr[0].save()
        if request.POST.get("button-delete") is not None and request.POST.get("specific_qr") is None:
            delete = True
        if request.POST.get("form-delete") is not None:
            try:
                qrcode_id = request.COOKIES["qrcode"]
                qrcode = QR_Codes.objects.get(id=qrcode_id)
                qrcode.delete()
                return redirect("my_codes")
            except:
                print("error")

        if request.POST.get("specific_qr") is not None:
            if request.COOKIES["specificQrcodeID"]:
                specific_qrcode_id = request.COOKIES["specificQrcodeID"]
                specific_qrcode = QR_Codes.objects.get(id=specific_qrcode_id)
                date_parse = parser.parse(specific_qrcode.date_created, dayfirst=True)
                date_expire = date_parse + relativedelta(months=6)
                date_expire_code = date_expire.strftime("%Y-%m-%d %H:%M:%S")
                date = f"{date_expire_code.split(':')[0].split('-')[2].split(' ')[0]}.{date_expire_code.split(':')[0].split('-')[1].split(' ')[0]} {date_expire_code.split(':')[0].split(' ')[1]}:{date_expire_code.split(':')[1].split('-')[0].split(' ')[0]}"

    all_user_qr = QR_Codes.objects.filter(user = request.user)
    if all_user_qr:
        all_user_qr[0].is_working = True
        all_user_qr[0].save()
    return render(request, "my_codes/my_codes.html", context = {
        "User": User.objects.all(),
        "QR_Codes": QR_Codes.objects.all(),
        "current_user": request.user,
        "specific_qrcode": specific_qrcode,
        "date_expired": date,
        "delete": delete,
        "date_expired": date
    })
