# Всі views.py з точним описом, які ми створили в нашому проєкті \ All views.py with precise description that we created in our project

## Додаток home_app \ Home_app application

```python
# Імпортуємо усі необхідні модулі \ Import all necessary modules
from django.shortcuts import render
from django.http import  HttpRequest

# Створюємо функцію відображення render_home_app \ Create the render_home_app display function
def render_home_app(request: HttpRequest):
    # Повертаємо нашу відоборажену сторінку \ Returning our displayed page 
    return render(request, "home_app/home.html")
```

## Додаток registration1 \ Registration1 application

```python
# Імпортуємо усі необхідні модулі \ Import all necessary modules
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.core.mail import send_mail
from .models import Code_Number
from django.contrib.auth import authenticate, login
from django.http import  HttpRequest


# Створюємо функцію відображення render_registration1 \ Create the render_registration1 display function
def render_registration1(request: HttpRequest):
    # Створюємо об'єкт помилки \ Creating an error object
    error = ""
    # Створюємо умову, якщо користувач відправив форму \ We create a condition if the user submitted the form
    if request.method == "POST":
        # Получаємо дані з input \ Getting data from the inputs
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")
        # Якщо поле пароля та поле підтвердження пароля однакові \ If the password field and the password confirmation field are the same
        if password == confirm_password:      
            # Створюємо оператор try, щоб в разі помилки сервер не закрився \ We create a try statement so that in case of an error the server does not close
            try:
                # Створюємо нового користувача з введеними даними \ Сreate a new user with the entered data
                User.objects.create_user(username= name, email= email, password= password)
                error = ""
                # Переадресуємо користувача на сторінку успішної реєстрації \ Redirect the user to the successful registration page
                return redirect("/registration/succesregistration/")
            # Робимо виключення, якщо користувач вже існує \ Throw an exception if the user already exists
            except IntegrityError:
                # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
                error = "Такий користувач вже існує!"
            # Робимо виключення, якщо форма пуста \ Throw an exception if the form is empty
            except ValueError:
                # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
                error = "Поля не можуть бути пустими!"
            # Робимо виключення \ Throw an exception
            except:
                # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
                error = "Користувача не знайдено"
        # Якщо поля не співпадають \ If the fields do not match
        else:
            #                 # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
            error = "Паролі не співпадають"
    # Відображаємо сторінку з додатковим параметром context, через який ми відображаємо на сторінці помилку \ We display the page with an additional context parameter, through which we display an error on the page
    return render(request, "registration1/registration1.html",  context= {"error": error})
```

## Додаток registration3 \ Registration3 application

```python
# Імпортуємо усі необхідні модулі \ Import all necessary modules
from django.shortcuts import render, redirect
from django.http import  HttpRequest


# Створюємо функцію відображення render_registration3 \ Create the render_registration3 display function
def render_registration3(request: HttpRequest):
    # Створюємо умову, якщо користувач натиснув на кнопку \ We create a condition if the user clicks the button 
    if request.method == 'POST':
        # Переадресуємо користувача на авторизацію \ Redirect user to autorithation page
        return redirect("/authorithation/logininformation/")
    # Відображаємо сторінку \ Display page
    return render(request, "registration3/registration3.html")
```

## Додаток authorithation1 \ Authorithation1 application

```python
# Імпортуємо усі необхідні модулі \ Import all necessary modules
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import random
from registration1.models import Code_Number
from django.contrib.auth.models import User
from django.http import  HttpRequest


# Створюємо функцію відображення render_authorithation1 \ Create the render_authorithation1 display function
def render_authorithation1(request: HttpRequest):
    # Створюємо об'єкт помилки \ Creating an error object
    error = ""
    # Створюємо умову, якщо користувач відправив форму \ We create a condition if the user submitted the form
    if request.method == "POST":
        # Получаємо дані з input \ Getting data from the inputs
        username = request.POST.get("name")
        password = request.POST.get("password")
        # Перевіряємо, чи існує користувач у базі даних \ Checking if a user exists in the database
        user = authenticate(request, username= username, password = password)
        # Створюємо оператор try, щоб в разі помилки сервер не закрився \ We create a try statement so that in case of an error the server does not close
        try:
            # Якщо користувач існує - створюємо випадковий 6-значний код та переадресуємо його на 2 етап авторизації \ If the user exists - we generate a random 6-digit code and redirect it to the 2nd stage of authorization
            if user != None:
                # Авторизуємо користувача \ Login user
                login(request, user)
                # Створюємо випадковий 6-значний код та зберігаємо його в базі даних \ We generate a random 6-digit code and save it in the database
                random_number = random.randint(99999, 999999)
                Code_Number.objects.create(number = random_number, user_id = user.id)   
                # Переадресуємо користувача на 2 етап перевірки \ Redirect the user to the 2nd stage of verification
                return redirect('/authorithation/loginemail/')
            # Якщо користувача не знайдено \ If user does not exist
            else:
                # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
                error = "Не вірний пароль або ім'я"
        # Робимо виключення \ Throw an exception
        except:
            # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
            error = "Не вірний пароль або ім'я"
    # Відображаємо сторінку з додатковим параметром context, через який ми відображаємо на сторінці помилку \ We display the page with an additional context parameter, through which we display an error on the page
    return render(request, "authorithation1/index.html",  context= {"error": error})
```

## Додаток authorithation2 \ Authorithation2 application

```python
# Імпортуємо усі необхідні модулі \ Import all necessary modules
from django.shortcuts import render, redirect
import random
from django.core.mail import send_mail
from registration1.models import Code_Number
from django.http import  HttpRequest


# Створюємо функцію відображення render_authorithation2 \ Create the render_authorithation2 display function
def render_authorithation2(request: HttpRequest):
    # Створюємо об'єкт помилки \ Creating an error object
    error = ""
    # Створюємо оператор try, щоб в разі помилки сервер не закрився \ We create a try statement so that in case of an error the server does not close
    try:
        # Перевіряємо чи користувач вже авторизований \ Checking if the user is already authenticated
        if request.user.is_authenticated:
            # Отримуємо з бази даних випадковий код за id користувача \ We get a random code from the database by user id
            random_number = Code_Number.objects.get(user_id = request.user.id).number
            # Відправляємо лист на електронну пошту з випадковим кодом \ We send an email with a random code
            send_mail(
                subject = "Код для підтвердження",
                message = f"Вітаємо!\n ваш код для підтвердження: {random_number}",
                from_email = "qrprojectdjangoteam2@gmail.com",
                recipient_list = [f"{request.user.email}"],
                fail_silently = False
                )
            # Створюємо умову, якщо користувач відправив форму \ We create a condition if the user submitted the form
            if request.method == "POST":
                # Получаємо дані з input \ Getting data from the inputs
                email_code = request.POST.get("email_code")
                # Перевіряємо чи введений код однаковий з випадковим \ Checking if the entered code matches the random one
                if int(email_code) == random_number:
                    # Видаляємо з бази даних старий код \ We delete the old code from the database
                    Code_Number.objects.get(user_id = request.user.id).delete()
                    # Відправляємо користувача на сторінку успішної авторизації \ We send the user to the success authorithation page
                    return redirect("/authorithation/succesauthorithation/")
                # Якщо код підтвердженян не співпадає з відправленим кодом на пошту \ If the confirmation code does not match the code sent to the email
                else:
                    # Записуємо в об'єкт помилки текст помилки \ Write the error text to the error object
                    error = "Код підтвердження не вірний!"
    # Робимо виключення \ Throw an exception
    except:
        # Отримуємо всі старі коди по id користувача та видаляємо їх \ We get all old codes by user id and delete them 
        Code_Number.objects.filter(user_id = request.user.id).delete()
         # Відображаємо сторінку з додатковим параметром context, через який ми відображаємо на сторінці помилку \ We display the page with an additional context parameter, through which we display an error on the page
    return render(request, "authorithation2/index.html", context= {"error": error})
```

## Додаток authorithation3 \ Authorithation3 application

```python
# Імпортуємо усі необхідні модулі \ Import all necessary modules
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import  HttpRequest


# Створюємо функцію відображення render_authorithation3 \ Create the render_authorithation3 display function
def render_authorithation3(request: HttpRequest):
    # Створюємо умову, якщо користувач натиснув на кнопку \ We create a condition if the user clicks the button 
    if request.method == 'POST':
        # Переадресовуємо користувача на головну сторінку \ Redirect user to main page
        return redirect("/")
    # Відображаємо сторінку авторизаці3 \ Display the authorization3 page
    return render(request, "authorithation3/authorithation3.html")

# Створюємо функцію для вихoду з акаунту \ Create function for exit from acount
def logout_user(request: HttpRequest):
    # Виходимо з аканту \ Exit from acount
    logout(request)
    # Переадресовуємо користувача на головну сторінку \ Redirect user to main page
    return redirect("/")
```
## Додаток qrgenerate_app \ Qrgenerate_app application

```python
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
```