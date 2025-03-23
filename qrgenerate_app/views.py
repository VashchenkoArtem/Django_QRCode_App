# Імпортуємо усі необхідні модулі \ Import all necessary modules
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


# Створюємо функцію, яка перероблює тип з hex в rgb \ Create a function that converts the type from hex to rgb
def hex_to_rgb(color):
    # Отримаємо колір \ Get color
    color_rgb = color.lstrip('#')
    # Перетворюємо перші 2 символи в змінну r \ Convert the first 2 characters into the variable r
    r = int(color_rgb[0:2], 16)
    # Перетворюємо наступні 2 символи в змінну g \ Convert the next 2 characters into the variable g
    g = int(color_rgb[2:4], 16)
    # Перетворюємо останні 2 символи в змінну b \ Convert the last 2 characters into the variable b
    b = int(color_rgb[4:6], 16)
    # Повертаємо r, g та b \ Return r, g and b
    return r, g, b

# Створюємо декоратор, який відкриє сторінку тільки якщо користувач авторизований \ We create a decorator that will open the page only if the user is authorized
@login_required
# Створюємо функцію відображення qr_generate_app \ Create the qr_generate_app display function
def qr_generate_app(request: HttpRequest):
    # Створюємо необіхдні заглушки, щоб потім їх використовувати \ We create the necessary stubs to use them later
    qr_code = None
    error = None
    redirect_object = None
    # Створюємо умову, якщо користувач відправив форму \ We create a condition if the user submitted the form
    if request.method == "POST":
        # Получаємо дані з input \ Getting data from the inputs
        name_code = request.POST.get("name")
        url_code = request.POST.get("url")
        bgcolor = request.POST.get("colorbg")
        qrcolor = request.POST.get("colorqr")
        image_input = request.FILES.get("image")
        form_input = request.POST.get("figure")
        # Створюємо оператор try, щоб в разі помилки сервер не закрився \ We create a try statement so that in case of an error the server does not close
        try:
            # Створюємо об'єкт підписки та отримаємо підписку по id користувача \ Create a subscription object and get the subscription by user id
            user_subscribe = UserSubscribe.objects.get(user_id=request.user.id)
            # Створюємо умову, якщо користувач ще не створив максимальну кількість qr-кодів \ We create a condition if the user has not yet created the maximum number of QR codes
            if len(QR_Codes.objects.filter(user_id=request.user.id)) < user_subscribe.max_count_qrs:
                # Знаходимо теперешній час \ Finding the present tense
                date_now = datetime.datetime.now()
                # Форматуємо його у потрібний формат \ Format it in the desired format
                date = datetime.datetime.strftime(date_now, "%Y-%m-%d %H:%M:%S")
                format_date = f"{date.split(':')[0].split('-')[2].split(' ')[0]}.{date.split(':')[0].split('-')[1].split(' ')[0]} {date.split(':')[0].split('-')[2].split(' ')[1]}:{date.split(':')[1].split('-')[0].split(' ')[0]}"
                # Створюємо об'єкт qr-кода в базі даних \ Create qrcode object in database
                qr_code = QR_Codes.objects.create(user=request.user, name=name_code, url=url_code, date_created=format_date)
                # Створюємо об'єкт редіректа цього qr-кода \ We create a redirect object for this qr code
                redirect_object = Redirect_QR.objects.create(qrcode=name_code, url=url_code, qr= QR_Codes.objects.get(id = qr_code.id))
            # Якщо користувач створив максимальну кількість qr-кодів \ If the user has created the maximum number of QR codes
            else:
                # Створюємо об'єкт помилки \ Creating an error object
                error = "Занадто багато QR-кодів!"
        # Створюємо виключення, якщо користувач авторизований \ Create an exception if the user is authorized
        except Exception:
            # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
            error = "Ви не в акаунті. Будь ласка, авторизуйтесь!"
        # Створюмєо умову, якщо уснує, і qr-код, і його редірект-об'єкт
        if qr_code and redirect_object: 
            # Створюємо картинку qr-кода з об'єкта qrcode \ Create qrcode image from qrcode object
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4
            )
            # Задаємо йому посилання \ Give him a link 
            qr.add_data(redirect_object.get_absolute_url())
            # Відображаємо qr-код \ Displaying the QR code
            qr.make(fit=True)
            # Якщо користувач обрав звичайну форму крапок \ If the user chose the regular dots form
            if form_input == "default":
                # Задаємо звичайну форму \ Set the default form
                eye_module = SquareModuleDrawer()
                dots_module = SquareModuleDrawer()
            # Якщо користувач обрав квадратну форму \ If the user selected a square shape
            if form_input == "square":
                # Задаємо квадратні крапки \ Set the square dots
                eye_module = GappedSquareModuleDrawer()
                dots_module = GappedSquareModuleDrawer()
            # Якщо користувач обрав круглі крапки \ If the user selected a circle dots
            if form_input == "circle":
                # Задаємо круглі крапки \ Set the circle dots
                eye_module = CircleModuleDrawer()
                dots_module = CircleModuleDrawer()
            # Якщо користувач обрав форму у вигляді вертикальних ліній \ If the user selected a shape in the form of vertical lines
            if form_input == "vertical-line":
                # Задаємо форму у вигляді вертикальних ліній \ We set the shape in the form of vertical lines
                eye_module = VerticalBarsDrawer()
                dots_module = VerticalBarsDrawer()
            # Якщо користувач обрав форму у вигляді горизонтальних ліній \ If the user selected a shape in the form of horizontal lines
            if form_input == "horizontal-line":
                # Задаємо форму у вигляді горизонтальних ліній \ We set the shape in the form of horizontal lines
                eye_module = HorizontalBarsDrawer()
                dots_module = HorizontalBarsDrawer()
            # Якщо користувач обрав скгрулену форму \ If the user has selected a rounded shape
            if form_input == "rounded":
                # Задаємо скруглену форму \ We set the rounded shape
                eye_module = RoundedModuleDrawer(radius_ratio=float(1))
                dots_module = RoundedModuleDrawer(radius_ratio=float(1))
            # Створюємо маску кольорів \ Creating a color mask
            color_mask = RadialGradiantColorMask(
                back_color=hex_to_rgb(bgcolor),
                edge_color=hex_to_rgb(qrcolor),
                center_color=hex_to_rgb(qrcolor)
            )
            # Створюємо зображення qr-кода
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=dots_module, eye_drawer=eye_module,
                                back_color=bgcolor, fill_color=qrcolor, color_mask=color_mask)
            # Якщо користувач заповнив поле зображення \ If the user filled in the image field
            if image_input:
                # Створюємо об'єкт логотипа \ Create logo object
                logo = PIL.Image.open(image_input)
                # Отримаємо розмір qr кода \ Get size qr code
                qr_size = img.size[0]
                # Задаємо розмір логотипу \ Set size to logo
                logo = logo.resize((100, 100))
                # Задаємо логотипу координати по центру qr кода \ We set the coordinates of the logo to the center of the QR code 
                logo_x = (qr_size - logo.size[0]) // 2
                logo_y = (qr_size - logo.size[0]) // 2
                # Перетворюємо логотип у формат RGBA \  Convert logo into format RGBA
                rgba = logo.convert("RGBA")
                # Вставляємо логотип в зображення \ Paste logo in image
                img.paste(logo, (logo_x, logo_y), rgba)
            # Створюємо дерикторію до папки, де храняться всі qr коди користувача \ We create a directory to the folder where all the user's QR codes are stored
            user_folder = os.path.join('qr_codes', request.user.username)
            # Перетворюємо зображення в  IO \ Convert image into IO
            img_io = io.BytesIO()
            # Зберігаємо зображення у форматі png \ Convert image into png format
            img.save(img_io, format="PNG")
            # Перетворюємо зображення в формат ContentFile \ Convert image into format ContentFile 
            img_content = ContentFile(content=img_io.getvalue(), name=f"{name_code}.png")
            # Створюмєо шлях до файлу \ Create path to file
            file_path = os.path.join(user_folder, f"{name_code}.png")
            # Створюємо умову, якщо qr код існує \ Створюємо умову, якщо qr код існує
            if qr_code:
                # Зберігаємо зображення qr кода \ Save qr code image
                qr_code.image.save(file_path, img_content)
                # Зберігаємо qr код \  Save qr code
                qr_code.save()
        # Якщо у користувача максимальна кількість qr кодів \ If the user has the maximum number of QR codes
        else:
            # Створюємо об'єкт помилки \ Creating an error object 
            error = "Занадто багато QR-кодів!"
    # Відображаємо сторінку з додатковим параметром context, через який ми відображаємо на сторінці помилку \ We display the page with an additional context parameter, through which we display an error on the page
    return render(request, "qrgenerate_app/index.html", context={"qr_code": qr_code, "error": error})
# Створюємо сторінку для перевірки \ Create page for verification
def render_check_qr(request: HttpRequest, qr_id: int):
    # Створюємо необіхдні заглушки, щоб потім їх використовувати \ We create the necessary stubs to use them later
    error = None
    qrcode = None
    # Створюємо оператор try, щоб в разі помилки сервер не закрився \ We create a try statement so that in case of an error the server does not close
    try:
        # Знаходимо qr код з бази даних \ Find the qr code in the database
        qrcode = QR_Codes.objects.get(id = qr_id)
    # Якщо qr код не знайдено \ If qr code does not exist
    except:
        # Створюємо об'єкт помилки \ Creating an error object
        error = "QR-Код не знайдено!"
    # Знаходимо підписку користувача \ Find user subscribe
    subscribe_user = UserSubscribe.objects.get(user_id = request.user.id)
    # Якщо підписка існує та is_working дорівнює True \ If the subscription exists and is_working is True
    if subscribe_user and subscribe_user.is_working:
        # Якщо qr код працює \ If qr code is working
        if qrcode.is_working == True:
            # Якщо qr код починається з http та її тип не desktop \ If the qr code starts with http and its type is not desktop
            if qrcode.url.startswith("http") or subscribe_user.subscribe_type != "desktop":
                # Переадресовуємо користувача на сторінку, яку він вказав в qr коді
                return redirect(qrcode.url)
        # Якщо qr код не працює \ If qr code does not work
        else:
            # Створюємо об'єкт помилки \ Creating an error object
            error = "Цей qr-код не працює, тому що ви вже створили можливу кількість qr-кодів!"
    # Якщо підписка завершилась або її зе не придбали \ If the subscription has expired or has not been purchased
    else:
        # Створюємо об'єкт помилки \ Creating an error object
        error = "Ваша підписка завершилась або ви ще не придбали її! subscribe_user"
    # Відображаємо сторінку з додатковим параметром context, через який ми відображаємо на сторінці помилку \ We display the page with an additional context parameter, through which we display an error on the page
    return render(request, "redirect/redirect.html", context = {"error": error})