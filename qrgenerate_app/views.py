import PIL.Image
from django.shortcuts import render
import qrcode, io
from django.core.files.base import ContentFile
import qrcode.constants
from .models import QR_Codes
import os
import PIL
import datetime
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
    CircleModuleDrawer,
    SquareModuleDrawer,
    GappedSquareModuleDrawer,
    RoundedModuleDrawer,
    HorizontalBarsDrawer,
    VerticalBarsDrawer
)
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from django.contrib.auth.decorators import login_required
# Create your views here.
def hex_to_rgb(color):
    color_rgb = color.lstrip('#')
    r = int(color_rgb[0:2], 16)
    g = int(color_rgb[2:4], 16)
    b = int(color_rgb[4:6], 16)
    return r, g, b

        
@login_required
def qr_generate_app(request):
    qr_code = None
    error = None
    if request.method == "POST":
        name_code = request.POST.get("name")
        url_code = request.POST.get("url")
        bgcolor = request.POST.get("colorbg")
        qrcolor = request.POST.get("colorqr")
        image_input = request.FILES.get("image")
        form_input = request.POST.get("figure")
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 10,
            border = 4
        )
        
        qr.add_data(url_code)
        qr.make(fit = True)
        if form_input == "default":
            eye_module = SquareModuleDrawer()
            dots_module = SquareModuleDrawer()

        if form_input == "square":
            eye_module = GappedSquareModuleDrawer()
            dots_module = GappedSquareModuleDrawer()

        if form_input == "circle":
            eye_module = CircleModuleDrawer()
            dots_module = CircleModuleDrawer()

        if form_input == "vertical-line":
            eye_module = VerticalBarsDrawer()
            dots_module = VerticalBarsDrawer()

        if form_input == "horizontal-line":
            eye_module = HorizontalBarsDrawer()
            dots_module = HorizontalBarsDrawer()
            
        if form_input == "rounded":
            eye_module = RoundedModuleDrawer(radius_ratio = float(1))
            dots_module = RoundedModuleDrawer(radius_ratio= float(1)) 

        color_mask = RadialGradiantColorMask(back_color=(hex_to_rgb(bgcolor)) ,edge_color=(hex_to_rgb(qrcolor)) ,center_color=(hex_to_rgb(qrcolor)))
        img = qr.make_image(image_factory = StyledPilImage, module_drawer = dots_module, eye_drawer = eye_module, back_color = bgcolor, fill_color = qrcolor, color_mask = color_mask)

        if image_input:
            logo = PIL.Image.open(image_input)
            qr_size = img.size[0]
            logo = logo.resize((100, 100))
            
            logo_x = (qr_size - logo.size[0]) // 2
            logo_y = (qr_size - logo.size[0]) // 2

            rgba = logo.convert("RGBA")
            img.paste(logo, (logo_x, logo_y), rgba)

        user_folder = os.path.join('qr_codes', request.user.username)
        img_io = io.BytesIO()
        img.save(img_io, format = "PNG")
        img_content = ContentFile(content = img_io.getvalue(), name = f"{name_code}.png")
        
        file_path = os.path.join(user_folder, f"{name_code}.png")
        date_now = datetime.datetime.now()
        date = datetime.datetime.strftime(date_now, "%Y-%m-%d %H:%M:%S")
        format_date = f"{date.split(':')[0].split('-')[2].split(' ')[0]}.{date.split(':')[0].split('-')[1].split(' ')[0]} {date.split(':')[0].split('-')[2].split(' ')[1]}:{date.split(':')[1].split('-')[0].split(' ')[0]}"
        try: 
            qr_code = QR_Codes.objects.create(user = request.user ,name = name_code, url = url_code, date_created = format_date)
            qr_code.image.save(file_path, img_content)
            qr_code.save()
        except ValueError:
            error = "Ви не в акаунті. Будь ласка, авторизуйтесь!"
    return render(request, "qrgenerate_app/index.html", context = {"qr_code": qr_code, "error": error})