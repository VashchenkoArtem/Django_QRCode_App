import PIL.Image
from urllib.parse import urlparse
from django.shortcuts import render, redirect
import qrcode, io
from django.core.files.base import ContentFile
import qrcode.constants
from .models import QR_Codes, Redirect_QR
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
from django.http import HttpResponseRedirect
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from django.contrib.auth.decorators import login_required
from subscribe.models import UserSubscribe
from django.http import  HttpRequest
from subscribe.models import UserSubscribe


# Create your views here.
def hex_to_rgb(color: HttpRequest):
    color_rgb = color.lstrip('#')
    r = int(color_rgb[0:2], 16)
    g = int(color_rgb[2:4], 16)
    b = int(color_rgb[4:6], 16)
    return r, g, b

        
@login_required
def qr_generate_app(request: HttpRequest):
    qr_code = None
    error = None
    redirect_object = None
    if request.method == "POST":
        name_code = request.POST.get("name")
        url_code = request.POST.get("url")
        bgcolor = request.POST.get("colorbg")
        qrcolor = request.POST.get("colorqr")
        image_input = request.FILES.get("image")
        form_input = request.POST.get("figure")
        try:

            user_subscribe = UserSubscribe.objects.get(user_id=request.user.id)
            if len(QR_Codes.objects.filter(user_id=request.user.id)) < user_subscribe.max_count_qrs:
                date_now = datetime.datetime.now()
                date = datetime.datetime.strftime(date_now, "%Y-%m-%d %H:%M:%S")
                format_date = f"{date.split(':')[0].split('-')[2].split(' ')[0]}.{date.split(':')[0].split('-')[1].split(' ')[0]} {date.split(':')[0].split('-')[2].split(' ')[1]}:{date.split(':')[1].split('-')[0].split(' ')[0]}"

                qr_code = QR_Codes.objects.create(user=request.user, name=name_code, url=url_code, date_created=format_date)

                redirect_object = Redirect_QR.objects.create(qrcode=name_code, url=url_code, qr= QR_Codes.objects.get(id = qr_code.id))
            else:
                error = "Занадто багато QR-кодів!"
        except Exception as e:
            print(e)
            error = "Ви не в акаунті. Будь ласка, авторизуйтесь!"
        if qr_code and redirect_object: 
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4
            )
            qr.add_data(redirect_object.get_absolute_url())
            qr.make(fit=True)

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
                eye_module = RoundedModuleDrawer(radius_ratio=float(1))
                dots_module = RoundedModuleDrawer(radius_ratio=float(1))

            color_mask = RadialGradiantColorMask(
                back_color=hex_to_rgb(bgcolor),
                edge_color=hex_to_rgb(qrcolor),
                center_color=hex_to_rgb(qrcolor)
            )
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=dots_module, eye_drawer=eye_module,
                                back_color=bgcolor, fill_color=qrcolor, color_mask=color_mask)

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
            img.save(img_io, format="PNG")
            img_content = ContentFile(content=img_io.getvalue(), name=f"{name_code}.png")

            file_path = os.path.join(user_folder, f"{name_code}.png")

            if qr_code:
                qr_code.image.save(file_path, img_content)
                qr_code.save()
        else:
            error = "Занадто багато QR-кодів!"

    return render(request, "qrgenerate_app/index.html", context={"qr_code": qr_code, "error": error})


def render_check_qr(request: HttpRequest, qr_id: int):
    error = None
    qrcode = None
    try:
        qrcode = QR_Codes.objects.get(id = qr_id)
    except:
        error = "QR-Код не знайдено!"
    # try:
    subscribe_user = UserSubscribe.objects.get(user_id = request.user.id)

    if subscribe_user and subscribe_user.is_working:
        if qrcode.is_working == True:
            if qrcode.url.startswith("http") or subscribe_user.subscribe_type != "desktop":
                return redirect(qrcode.url)
        else:
            error = "Цей qr-код не працює, тому що ви вже створили можливу кількість qr-кодів!"
    else:
        error = "Ваша підписка завершилась або ви ще не придбали її! subscribe_user"
    # except:
    #     error = "Ваша підписка завершилась або ви ще не придбали її! except"
    
    return render(request, "redirect/redirect.html", context = {"error": error})