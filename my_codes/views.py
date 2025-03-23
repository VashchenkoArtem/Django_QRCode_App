# Імпортуємо необхідні модулі \ Import necessary modules
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from qrgenerate_app.models import QR_Codes
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from dateutil import parser
from dateutil.relativedelta import relativedelta

from subscribe.models import UserSubscribe

# Декоратор login_required для обмеження доступу лише для авторизованих користувачів \ Login required decorator to restrict access to authenticated users only
@login_required
def render_my_codes(request: HttpRequest):
    # Створюємо необіхдні заглушки, щоб потім їх використовувати \ We create the necessary stubs to use them later
    specific_qrcode = None 
    date_expire = None 
    date = None
    delete = None 

    # Отримуємо інформацію про підписку користувача \ Fetch the user's subscription information
    subscribe_user = UserSubscribe.objects.get(user=request.user)
    
    # Якщо підписка не активна \ If the subscription is inactive
    if subscribe_user.is_working == False:
        all_user_qr = QR_Codes.objects.filter(user=request.user)

        # Деактивуємо всі QR-коди користувача \ Deactivate all user QR codes
        for qrcode in all_user_qr:
            qrcode.is_working = False
            qrcode.save()
        
        # Активуємо перший QR-код \ Activate the first QR code
        all_user_qr[0].is_working = True
        all_user_qr[0].save()

    # Якщо підписка активна \ If the subscription is active
    if subscribe_user.is_working == True:
        all_user_qr = QR_Codes.objects.filter(user=request.user)
        list_qrs = []  # Список для зберігання QR-кодів користувача \ List to store user QR codes
        
        # Для кожного QR-коду \ Iterate through each QR code
        for qrcode in all_user_qr:
            list_qrs.append(qrcode)
            # Якщо кількість QR-кодів менше максимального ліміту \ If the number of QR codes is less than the max allowed
            if len(list_qrs) < subscribe_user.max_count_qrs:
                qrcode.is_working = True
                qrcode.save()
                
    # Якщо кількість QR-кодів користувача перевищує максимальний ліміт \ If the number of user QR codes exceeds the max limit
    if len(QR_Codes.objects.filter(user_id=request.user.id)) > subscribe_user.max_count_qrs:

        all_user_qr = QR_Codes.objects.filter(user=request.user)
        
        # Деактивуємо всі QR-коди \ Deactivate all QR codes
        for qrcode in all_user_qr:
            qrcode.is_working = False
            qrcode.save()
        
        # Активуємо перший QR-код \ Activate the first QR code
        all_user_qr[0].is_working = True
        all_user_qr[0].save()
    
    # Якщо метод запиту POST \ If the request method is POST
    if request.method == "POST":
        all_user_qr = QR_Codes.objects.filter(user=request.user)
        
        # Активуємо перший QR-код \ Activate the first QR code
        all_user_qr[0].is_working = True
        all_user_qr[0].save()

        # Якщо натиснута кнопка для видалення QR-коду \ If the button to delete a QR code is pressed
        if request.POST.get("button-delete") is not None and request.POST.get("specific_qr") is None:
            delete = True  # Мітка для позначення видалення \ Flag to indicate deletion
        
        # Якщо натиснута кнопка для видалення форми \ If the delete form button is pressed
        if request.POST.get("form-delete") is not None:
            try:
                qrcode_id = request.COOKIES["qrcode"]
                qrcode = QR_Codes.objects.get(id=qrcode_id)
                qrcode.delete()  # Видаляємо QR-код \ Delete the QR code
                return redirect("my_codes")
            except:
                print("error")  # Виводимо помилку, якщо не вдалося знайти QR-код \ Print error if QR code not found

        # Якщо вибраний конкретний QR-код \ If a specific QR code is selected
        if request.POST.get("specific_qr") is not None:
            if request.COOKIES["specificQrcodeID"]:
                specific_qrcode_id = request.COOKIES["specificQrcodeID"]
                specific_qrcode = QR_Codes.objects.get(id=specific_qrcode_id)
                
                # Парсимо дату створення QR-коду \ Parse the QR code creation date
                date_parse = parser.parse(specific_qrcode.date_created, dayfirst=True)
                
                # Додаємо 6 місяців до дати створення \ Add 6 months to the creation date
                date_expire = date_parse + relativedelta(months=6)
                
                # Форматуємо дату закінчення \ Format the expiration date
                date_expire_code = date_expire.strftime("%Y-%m-%d %H:%M:%S")
                date = f"{date_expire_code.split(':')[0].split('-')[2].split(' ')[0]}.{date_expire_code.split(':')[0].split('-')[1].split(' ')[0]} {date_expire_code.split(':')[0].split(' ')[1]}:{date_expire_code.split(':')[1].split('-')[0].split(' ')[0]}"

    # Оновлюємо статус для активного QR-коду \ Update status for the active QR code
    all_user_qr = QR_Codes.objects.filter(user=request.user)
    if all_user_qr:
        all_user_qr[0].is_working = True
        all_user_qr[0].save()
    
    # Рендеримо шаблон \ Render the template
    return render(request, "my_codes/my_codes.html", context = {
        "User": User.objects.all(),  # Список всіх користувачів \ List of all users
        "QR_Codes": QR_Codes.objects.all(),  # Список всіх QR-кодів \ List of all QR codes
        "current_user": request.user,  # Поточний користувач \ Current user
        "specific_qrcode": specific_qrcode,  # Специфічний QR-код \ Specific QR code
        "date_expired": date,  # Дата закінчення терміну дії QR-коду \ QR code expiration date
        "delete": delete,  # Статус видалення QR-коду \ QR code deletion status
        "date_expired": date  # Дата закінчення терміну дії QR-коду \ QR code expiration date
    })
