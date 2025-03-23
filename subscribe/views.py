from django.shortcuts import render
from .models import UserSubscribe
from django.http import  HttpRequest
import datetime
from dateutil.relativedelta import relativedelta
# Create your views here.

def render_subscribe(request: HttpRequest):
    message = None
    subscribe_desktop = None
    date_now = datetime.datetime.now()
    date_month_next = date_now + relativedelta(months = 1)
    try:
        if date_now > date_month_next:
            user_subscribe = UserSubscribe.objects.get(user = request.user)
            user_subscribe.is_working = False
            user_subscribe.save()
        elif date_now < date_month_next:
            user_subscribe = UserSubscribe.objects.get(user = request.user)
            user_subscribe.is_working = True
            user_subscribe.save()      
    except:
        pass
    if request.method == "POST":
        card_number = request.POST.get("card")
        cvv_code = request.POST.get("cvv")
        expiration_date = request.POST.get("date")
        try:
            if request.COOKIES["subscribeType"]  == "free":
                if len(UserSubscribe.objects.filter(user_id =  request.user.id)) == 0:
                    UserSubscribe.objects.create(user_id = request.user.id,
                                                subscribe_type = "free",
                                                card_number = card_number,
                                                date_expired = expiration_date,
                                                max_count_qrs = 1,   
                                                cvv_code = cvv_code,
                                                date_expired_subscribe = date_month_next                   
                                                )
                    message = "Задана підписка Free!"
                else:
                    UserSubscribe.objects.filter(user_id = request.user.id).delete()
                    UserSubscribe.objects.create(user_id = request.user.id,
                                                subscribe_type = "free",
                                                card_number = card_number,
                                                date_expired = expiration_date,
                                                max_count_qrs = 1,   
                                                cvv_code = cvv_code,
                                                date_expired_subscribe = date_month_next                   
                                                )
                    message = "Підписка успішно змінена на Free!"
            if request.COOKIES["subscribeType"]  == "standart":
                if len(UserSubscribe.objects.filter(user_id =  request.user.id)) == 0:
                    UserSubscribe.objects.create(user_id = request.user.id,
                                                subscribe_type = "standart",
                                                card_number = card_number,
                                                date_expired = expiration_date,
                                                max_count_qrs = 10,   
                                                cvv_code = cvv_code ,
                                                date_expired_subscribe = date_month_next                      
                                                )
                    message = "Задана підписка Standart!"
                else:
                    UserSubscribe.objects.filter(user_id = request.user.id).delete()
                    UserSubscribe.objects.create(user_id = request.user.id,
                                                subscribe_type = "standart",
                                                card_number = card_number,
                                                date_expired = expiration_date,
                                                max_count_qrs = 10,   
                                                cvv_code = cvv_code,
                                                date_expired_subscribe = date_month_next                       
                                                )
                    message = "Підписка успішно змінена на Standart!"
            if request.COOKIES["subscribeType"]  == "pro":
                if len(UserSubscribe.objects.filter(user_id =  request.user.id)) == 0:
                    UserSubscribe.objects.create(user_id = request.user.id,
                                                subscribe_type = "pro",
                                                card_number = card_number,
                                                date_expired = expiration_date,
                                                max_count_qrs = 100,   
                                                cvv_code = cvv_code,
                                                date_expired_subscribe = date_month_next                       
                                                )
                    message = "Задана підписка Pro!"
                else:
                    UserSubscribe.objects.filter(user_id = request.user.id).delete()
                    UserSubscribe.objects.create(user_id = request.user.id,
                                                subscribe_type = "pro",
                                                card_number = card_number,
                                                date_expired = expiration_date,
                                                max_count_qrs = 100,   
                                                cvv_code = cvv_code,
                                                date_expired_subscribe = date_month_next                       
                                                )
                    message = "Підписка успішно змінена на Pro!"
        except:
            pass
    try:
        if request.COOKIES["subscribeType"]  == "desktop":
            subscribe_desktop = True
            if request.method == "POST":
                card_number = request.POST.get("card")
                cvv_code = request.POST.get("cvv")
                expiration_date = request.POST.get("date")
                count_qrs = request.POST.get("count")
                if len(UserSubscribe.objects.filter(user_id =  request.user.id)) == 0:
                    UserSubscribe.objects.create(
                        user_id = request.user.id,
                        subscribe_type = "desktop",
                        card_number = card_number,
                        date_expired = expiration_date,
                        max_count_qrs = count_qrs,   
                        cvv_code = cvv_code,
                        date_expired_subscribe = date_month_next    
                    )
                    message = "Задана підписка Desktop!"
                else:
                    UserSubscribe.objects.filter(user_id = request.user.id).delete()
                    UserSubscribe.objects.create(
                        user_id = request.user.id,
                        subscribe_type = "desktop",
                        card_number = card_number,
                        date_expired = expiration_date,
                        max_count_qrs = count_qrs,   
                        cvv_code = cvv_code,
                        date_expired_subscribe = date_month_next   
                    )
                    message = "Підписка успішно замінена на Desktop!"
    except:
        pass
    return render(request, 'subscribe/subscribe.html', context = {"message":message, "subscribe_desktop": subscribe_desktop})