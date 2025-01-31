from django.shortcuts import render
import qrcode, io
from django.core.files.base import ContentFile
import qrcode.constants
from .models import QR_Codes
# Create your views here.

def qr_generate_app(request):
    qr_code = None
    if request.method == "POST":
        name_code = request.POST.get("name")
        url_code = request.POST.get("url")

        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 4
        )
        
        qr.add_data(url_code)
        qr.make(fit = True)

        img = qr.make_image(fill_color = "black", fill_back = "white")
        
        img_io = io.BytesIO()
        img.save(img_io, format = "PNG")
        img_content = ContentFile(content = img_io.getvalue(), name = f"{name_code}.png")
        
        qr_code = QR_Codes.objects.create(name = name_code, url = url_code)
        qr_code.image.save(f"{name_code}.png", img_content)
        qr_code.save()
        
        
    return render(request, "qrgenerate_app/index.html", context = {"qr_code": qr_code})