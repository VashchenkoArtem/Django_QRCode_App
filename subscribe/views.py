from django.shortcuts import render
from .models import UserSubscribe
from datetime import datetime
from django.contrib.auth.models import User
# Create your views here.

def render_subscribe(request):
    message = None
    if request.method == "POST":
        card_number = request.POST.get("card")
        cvv_code = request.POST.get("cvv")
        expiration_date = request.POST.get("date")
        if request.COOKIES["subscribeType"]  == "free":
            if len(UserSubscribe.objects.filter(user_id =  request.user.id)) == 0:
                UserSubscribe.objects.create(user_id = request.user.id,
                                            subscribe_type = "free",
                                            card_number = card_number,
                                            date_expired = expiration_date,
                                            max_count_qrs = 1,   
                                            cvv_code = cvv_code                     
                                            )
                message = "Підписку успішно задано!"
            else:
                UserSubscribe.objects.filter(user_id = request.user.id).delete()
                UserSubscribe.objects.create(user_id = request.user.id,
                                            subscribe_type = "free",
                                            card_number = card_number,
                                            date_expired = expiration_date,
                                            max_count_qrs = 1,   
                                            cvv_code = cvv_code                     
                                            )
                message = "Підписка успішно змінена!"
        if request.COOKIES["subscribeType"]  == "standart":
            if len(UserSubscribe.objects.filter(user_id =  request.user.id)) == 0:
                UserSubscribe.objects.create(user_id = request.user.id,
                                            subscribe_type = "standart",
                                            card_number = card_number,
                                            date_expired = expiration_date,
                                            max_count_qrs = 10,   
                                            cvv_code = cvv_code                     
                                            )
                message = "Підписку успішно задано!"
            else:
                UserSubscribe.objects.filter(user_id = request.user.id).delete()
                UserSubscribe.objects.create(user_id = request.user.id,
                                            subscribe_type = "standart",
                                            card_number = card_number,
                                            date_expired = expiration_date,
                                            max_count_qrs = 10,   
                                            cvv_code = cvv_code                     
                                            )
                message = "Підписка успішно змінена!"
        if request.COOKIES["subscribeType"]  == "pro":
            if len(UserSubscribe.objects.filter(user_id =  request.user.id)) == 0:
                UserSubscribe.objects.create(user_id = request.user.id,
                                            subscribe_type = "pro",
                                            card_number = card_number,
                                            date_expired = expiration_date,
                                            max_count_qrs = 100,   
                                            cvv_code = cvv_code                     
                                            )
                message = "Підписку успішно задано!"
            else:
                UserSubscribe.objects.filter(user_id = request.user.id).delete()
                UserSubscribe.objects.create(user_id = request.user.id,
                                            subscribe_type = "pro",
                                            card_number = card_number,
                                            date_expired = expiration_date,
                                            max_count_qrs = 100,   
                                            cvv_code = cvv_code                     
                                            )
                message = "Підписка успішно змінена!"

    return render(request, 'subscribe/subscribe.html', context = {"message":message})