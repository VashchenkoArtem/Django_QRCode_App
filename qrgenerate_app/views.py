from django.shortcuts import render
import qrcode, io
from django.core.files.base import ContentFile
import qrcode.constants
from .models import QR_Codes
import os
# Create your views here.


def qr_generate_app(request):
    qr_code = None
    if request.method == "POST":
        name_code = request.POST.get("name")
        url_code = request.POST.get("url")
        bgcolor = request.POST.get("colorbg")
        qrcolor = request.POST.get("colorqr")
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 4
        )
        
        qr.add_data(url_code)
        qr.make(fit = True)

        img = qr.make_image(back_color = bgcolor, fill_color = qrcolor)
        
        user_folder = os.path.join('qr_codes', request.user.username)
        img_io = io.BytesIO()
        img.save(img_io, format = "PNG")
        img_content = ContentFile(content = img_io.getvalue(), name = f"{name_code}.png")
        
        file_path = os.path.join(user_folder, f"{name_code}.png")

        qr_code = QR_Codes.objects.create(user = request.user ,name = name_code, url = url_code )
        qr_code.image.save(file_path, img_content)
        qr_code.save()
        
        
    return render(request, "qrgenerate_app/index.html", context = {"qr_code": qr_code})