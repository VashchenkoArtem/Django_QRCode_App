# Всі index.html в проєкті

## Додаток home_app \ Home_app application
```html
{% extends "base.html" %}

{% load static %}

{% block link %}
    <link href="https://fonts.googleapis.com/css2?family=Arimo&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://indestructibletype.com/fonts/Jost.css" type="text/css" charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Anonymous+Pro:ital,wght@0,400;0,700;1,400;1,700&family=Jura:wght@300..700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'home_app/home.css' %}">
{% endblock %}

{% block title%}
Головна сторінка
{% endblock %}
{% block content %}
    <div class =  "Screen">

        <div class = "hat"; style="flex-wrap: nowrap;">
            <h1 class = "h1Generate">Генератор <span class = "spanQR">QR</span>-кодів</h1>
            <div class = "urls">
                <div class = "mainUrl">
                    <a href = "" class = "mainPage">Головна</a>
                </div>
                {% if request.user.is_authenticated %}
                    <a href="{% url 'my_codes' %}" class = "MyQRCodesPage" >Мої QR-коди</a>
                    <a href = "{% url 'logout' %}"class = "logout-button">Вийти з акаунту</a>
                {% else %}
                    <a href="/codes/my_codes/" class = "MyQRCodesPage" >Мої QR-коди</a>
                    <a href="/registration/informationabout/" class = "registrationPage">Реєстрація</a>
                    <a href="/authorithation/logininformation/"class = "authorizationPage">Авторизація</a>

                {% endif %}
                <h1 class = "user-h1">{{request.user.username}}</h1>
            </div>
        </div>

        <div class = "subscribe">
            <div class = "subscribeFree">
                <a class = "freeButton" href="{% url 'subscribe' %}">
                    <h1 class = "buttonFree" >Free</h1>
                </a>

                <h1 class = "descritpionFree">Безкоштовно Один QR-код на 6 місяців</h1>
            </div>
            <div class = "lineBetweenFreeAndStandart"></div>
            
            <div class = "subscribeStandart">
                <a  class = "buttonStandart"href="{% url 'subscribe' %}">
                    <h1 class = "h1Standart">Standart</h1>
                </a>

                <h1 class = "descriptionStandart">2$ на місяць 10 кастомізованих <br>QR-кодів</h1>
            </div>

            <div class = "lineBetweenStandartAndPro"></div>

            <div class = "subscribePro">
                <a class = "proButton" href="{% url 'subscribe' %}">
                    <h1 class = "h1Pro">Pro</h1>    
                </a>
                
                <h1 class = "descriptionPro">10$ на місяць До 100 <br>QR-кодів</h1>
            </div>
            <div class = "secondRow">
                <div class="subscribeDesktop">
                    <a href="{% url 'subscribe' %}" class="desktopButton">
                        <h1 class="h1Desktop">Desktop</h1>
                    </a>

                    <h1 class="descriptionDesktop"><ul>
                        <li>5 QR-кодів</li>
                        <li>10 QR-кодів</li>
                        <li>20 QR-кодів</li>
                    </ul>
                </h1>

                </div>
                <div class = "lineAfterDesktop"></div>
                <div class = "generateButton">
                    <div class = "bgGenerateButton">
                        <a href = "/codes/qrgenerate/" class = "h1GenerateButton">Згенерувати QR-код</a>
                    </div>
                </div>
            </div>
        </div>

        <div class = "contacts">
            <div class = "allIcons">
                <a href="{% url 'contacts' %}">
                    <img class = "imageTelegram" src="{% static 'images/telegramIcon.png' %}" alt="">
                </a>
                <a href="{% url 'contacts' %}">
                    <img class = "imageViber" src="{% static 'images/viberIcon.png' %}" alt="">
                </a>
                <a href="{% url 'contacts' %}">
                    <img class = "imageCall" src="{% static 'images/callIcon.png' %}" alt="">
                </a>

            </div>
        </div>

    </div>
    <script src="{% static 'js/home.js'%}"></script>
{% endblock %}
```
## Додаток registration1 \ Registration1 application

```html
{% extends 'base.html'%}
{% load static %}

{% block link %}
    <link href="https://fonts.googleapis.com/css2?family=Arimo&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://indestructibletype.com/fonts/Jost.css" type="text/css" charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Anonymous+Pro:ital,wght@0,400;0,700;1,400;1,700&family=Jura:wght@300..700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'registration1/registration1.css' %}">
{% endblock %}
{% block content %}
    <div class = "Screen">
        <div class = "hat"; style="height: 136px; gap:200px;">
            <h1 class = "h1Generate">Реєстрація</h1>
            <div class = "urls">
                <a href = "{% url 'home_app' %}" class = "mainPage">Головна</a>
                <a href="{% url 'my_codes'%}" class = "my-codes">Мої QR-коди</a>
                <div class = "myQRCodesPage">
                    <a href="{% url 'registration1' %}"class = "">Реєстрація</a>
                </div>
                <a href="{% url 'authorithation1'%}"class = "autorithation">Авторизація</a>

            </div>
        </div>
        <div class="registration-form">
            <div class="registration-frame">
                <h1 class="info-text">Інформація про вас</h1>

                <form method = "post">
                    {% csrf_token %}
                    <div class="name-form-frame">
                        <label class="text-name">Ім'я</label>
                        <input class="name-form" type="text" name = "name" required>
                        <h5 class="under-name">Наприклад: Artem</h5>
                    </div>
                    <div class="email-form-frame">
                        <label class="text-name">Пошта</label>
                        <input class="name-form" type="email" name="email" required>
                        <h5 class="under-name">Наприклад: example123@gmail.com</h5>
                    </div>
                    <div class="password-form-frame">
                        <label class="text-name">Пароль</label>
                        <input class="name-form" type="password" name="password" required minlength="8">
                        <h5 class="under-name">Не менше 8 символів</h5>
                    </div>
                    <div class="password-form-frame confirm-password">
                        <label class="text-name">Підтвердження пароля</label>
                        <input class="name-form" type="password" name="confirm-password" required minlength="8">
                        <h5 class="under-name">Не менше 8 символів</h5>
                    </div>
                    <h1 class = "error">{{error}}</h1>
                    <button class="under-button-frame" type="submit">Надіслати</button>
                </form>
            </div>
        </div>
        <div class = "contacts" style="padding-top: 51px;">
            <div class = "allIcons">
                <img class = "imageTelegram" src="{% static 'images/telegramIcon.png' %}" alt="">
                <img class = "imageViber" src="{% static 'images/viberIcon.png' %}" alt="">
                <img class = "imageCall" src="{% static 'images/callIcon.png' %}" alt="">
            </div>
        </div>
    </div>
{% endblock %}
```
## Додаток registration3 \ Registration3 application
```html
{% extends 'base.html'%}
{% load static %}

{% block link %}
    <link href="https://fonts.googleapis.com/css2?family=Arimo&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://indestructibletype.com/fonts/Jost.css" type="text/css" charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Anonymous+Pro:ital,wght@0,400;0,700;1,400;1,700&family=Jura:wght@300..700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'registration3/registration3.css' %}">
{% endblock %}
{% block content %}
    <div class = "Screen">
        <div class = "hat"; style="height: 136px; ">
            <h1 class = "h1Generate">Реєстрація</h1>
            <div class = "urls">
                <div class = "mainUrl">
                    <a href = "{% url 'home_app' %}" class = "mainPage">Головна</a>
                </div>
                <a href="{% url 'my_codes' %}" class = "my-codes">Мої QR-коди</a>
                <a href="{% url 'registration3' %}" class = "MyQRCodesPage" >Реєстрація</a>
                <a href="{% url 'authorithation1' %}"class = "autorithation">Авторизація</a>
                
            </div>
        </div>
        <div class="registration-form">
            <div class="registration-frame">
                <img class = "image-icon"src="{% static 'images/succesregistration.png' %}" alt="">
                <form method = "post">
                    {% csrf_token %}
                    <div class = "frame-succes">
                        <h1 class = 'h1'>Вітаємо! <br>Ви успішно зареєструвалися!</h1>
                    </div>

                    <button class="under-button-frame" type="submit">Авторизація</button>
                </form>
            </div>
        </div>
        <div class = "contacts" style="padding-top: 51px">
            <div class = "allIcons">
                <img class = "imageTelegram" src="{% static 'images/telegramIcon.png' %}" alt="">
                <img class = "imageViber" src="{% static 'images/viberIcon.png' %}" alt="">
                <img class = "imageCall" src="{% static 'images/callIcon.png' %}" alt="">
            </div>
        </div>
    </div>
{% endblock %}
```
## Додаток authorithation1 \ Authorithation1 application
```html
{% extends 'base.html'%}
{% load static %}

{% block link %}
    <link href="https://fonts.googleapis.com/css2?family=Arimo&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://indestructibletype.com/fonts/Jost.css" type="text/css" charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Anonymous+Pro:ital,wght@0,400;0,700;1,400;1,700&family=Jura:wght@300..700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'authorithation1/authorithation1.css' %}">
{% endblock %}
{% block content %}
    <div class = "Screen">
        <div class = "hat"; style="height: 136px; gap:233px">
            <h1 class = "h1Generate">Авторизація</h1>
            <div class = "urls">
                <div class = "mainUrl">
                    <a href = "{% url 'home_app' %}" class = "mainPage">Головна</a>
                </div>

                <a href="{% url 'my_codes' %}" class = "codes">Мої QR-коди</a>
                <a href="{% url 'registration1' %}" class = "registration">Реєстрація</a>
                <a href="{% url 'authorithation1' %}"class = "MyQRCodesPage">Авторизація</a>
            </div>
        </div>
        <div class="registration-form">
            <div class="registration-frame">
                <h1 class="info-text">Інформація про вас</h1>
                <form method = "post">
                    {% csrf_token%}
                    <div class="name-form-frame">
                        <label class="text-name">Ім'я</label>
                        <input class="name-form" type="text" name="name" required>
                        <h5 class="under-name">Наприклад: Artem</h5>
                    </div>
                    <div class="password-form-frame">
                        <label class="text-name">Пароль</label>
                        <input class="name-form" type="password" name="password">
                        <h5 class="under-name">Не менше 8 символів</h5>
                    </div>
                    <h1 class = "error">{{error}}</h1>
                    <button class="under-button-frame" type="submit">Надіслати
                    </button>
                </form>

            </div>
        </div>
        <div class = "contacts" style="padding-top: 51px;">
            <div class = "allIcons">
                <img class = "imageTelegram" src="{% static 'images/telegramIcon.png' %}" alt="">
                <img class = "imageViber" src="{% static 'images/viberIcon.png' %}" alt="">
                <img class = "imageCall" src="{% static 'images/callIcon.png' %}" alt="">
            </div>
        </div>
    </div>
{% endblock %}
```

## Додаток authorithation2 \ Authorithation2 application

```html
{% extends 'base.html'%}
{% load static %}

{% block link %}
    <link href="https://fonts.googleapis.com/css2?family=Arimo&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://indestructibletype.com/fonts/Jost.css" type="text/css" charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Anonymous+Pro:ital,wght@0,400;0,700;1,400;1,700&family=Jura:wght@300..700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'authorithation2/authorithation2.css' %}">
{% endblock %}
{% block content %}
    <div class = "Screen">
        <div class = "hat"; style="height: 136px; gap:233px">
            <h1 class = "h1Generate">Авторизація</h1>
            <div class = "urls">
                <div class = "mainUrl">
                    <a href = "{% url 'home_app' %}" class = "mainPage">Головна</a>
                </div>

                <a href="{% url 'my_codes' %}" class = "codes">Мої QR-коди</a>
                <a href="{% url 'registration1' %}" class = "registration">Реєстрація</a>
                <a href="{% url 'authorithation1' %}"class = "MyQRCodesPage">Авторизація</a>
            </div>
        </div>
        <div class="authorithation-form">
            <div class="authorithation-frame">
                <div class="emailImgFrame">
                    <img class="emailImg" src="{% static 'images/emailicon.png' %}" alt="">
                </div>
                <h1 class="info-text">На вашу пошту надійшло повідомлення! <br>Будь ласка введіть код для підтвердження</h1>
                <form method = "post" class = "frame">
                    {% csrf_token %}
                    <div class="email-form-frame">
                        <label class="text-name">Код з пошти</label>
                        <input class="name-form" type="text" required minlength="6" maxlength="6" name="email_code">
                        <h5 class="under-name">Наприклад: 123456</h5>
                    </div>
                    <h1 class = "error">{{error}}</h1>
                    <button class="under-button-frame" type="submit">Ввійти в акаунт</button>
                </form>
            </div>
        </div>
        <div class = "contacts"  style="padding-top: 51px;">
            <div class = "allIcons">
                <img class = "imageTelegram" src="{% static 'images/telegramIcon.png' %}" alt="">
                <img class = "imageViber" src="{% static 'images/viberIcon.png' %}" alt="">
                <img class = "imageCall" src="{% static 'images/callIcon.png' %}" alt="">
            </div>
        </div>
    </div>
{% endblock %}
```
## Додаток authorithation3 \ Authorithation3 application

```html
{% extends 'base.html'%}
{% load static %}

{% block link %}
    <link rel="stylesheet" href="{% static 'authorithation3/authorithation3.css' %}">
    <link rel="stylesheet" href="https://indestructibletype.com/fonts/Jost.css" type="text/css" charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Anonymous+Pro:ital,wght@0,400;0,700;1,400;1,700&family=Jura:wght@300..700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'authorithation2/authorithation2.css' %}">
{% endblock %}
{% block content %}
    <div class = "Screen">
        <div class = "hat"; style="height: 136px; gap:222px;">
            <h1 class = "h1Generate">Авторизація</h1>
            <div class = "urls">
                <div class = "mainUrl">
                    <a href = "{% url 'home_app' %}" class = "mainPage" style="margin-left:-10px">Головна</a>
                </div>
                <a href="{% url 'my_codes' %}" class = "my-codes">Мої QR-коди</a>
                <a href="{% url 'registration1' %}" class = "registration">Реєстрація</a>
                <a href="{% url 'authorithation1' %}"class = "MyQRCodesPage">Авторизація</a>

            </div>
        </div>
        <div class="registration-form">
            <div class="registration-frame">
                <img src="{% static 'images/succesregistration.png' %}" style="padding-top: 75px" alt="">
                <form method = "POST">
                    {% csrf_token %}
                    <div class = "frame-succes">
                        <h1 class = 'h1'>Вітаємо! <br>Ви успішно авторизувалися!</h1>
                    </div>

                    <button class="under-button-frame" type="submit">На головну</button>
                </form>
            </div>
        </div>
        <div class = "contacts"  style="padding-top: 51px;">
            <div class = "allIcons">
                <img class = "imageTelegram" src="{% static 'images/telegramIcon.png' %}" alt="">
                <img class = "imageViber" src="{% static 'images/viberIcon.png' %}" alt="">
                <img class = "imageCall" src="{% static 'images/callIcon.png' %}" alt="">
            </div>
        </div>
    </div>
{% endblock %}
```
## Додаток qrgenerate_app \ Qrgenerate_app application
```html
{% extends 'base.html'%}
{% load static %}

{% block link %}
    <link rel="stylesheet" href="{% static 'authorithation3/authorithation3.css' %}">
    <link rel="stylesheet" href="https://indestructibletype.com/fonts/Jost.css" type="text/css" charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Anonymous+Pro:ital,wght@0,400;0,700;1,400;1,700&family=Jura:wght@300..700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'authorithation2/authorithation2.css' %}">
{% endblock %}
{% block content %}
    <div class = "Screen">
        <div class = "hat"; style="height: 136px; gap:222px;">
            <h1 class = "h1Generate">Авторизація</h1>
            <div class = "urls">
                <div class = "mainUrl">
                    <a href = "{% url 'home_app' %}" class = "mainPage" style="margin-left:-10px">Головна</a>
                </div>
                <a href="{% url 'my_codes' %}" class = "my-codes">Мої QR-коди</a>
                <a href="{% url 'registration1' %}" class = "registration">Реєстрація</a>
                <a href="{% url 'authorithation1' %}"class = "MyQRCodesPage">Авторизація</a>

            </div>
        </div>
        <div class="registration-form">
            <div class="registration-frame">
                <img src="{% static 'images/succesregistration.png' %}" style="padding-top: 75px" alt="">
                <form method = "POST">
                    {% csrf_token %}
                    <div class = "frame-succes">
                        <h1 class = 'h1'>Вітаємо! <br>Ви успішно авторизувалися!</h1>
                    </div>

                    <button class="under-button-frame" type="submit">На головну</button>
                </form>
            </div>
        </div>
        <div class = "contacts"  style="padding-top: 51px;">
            <div class = "allIcons">
                <img class = "imageTelegram" src="{% static 'images/telegramIcon.png' %}" alt="">
                <img class = "imageViber" src="{% static 'images/viberIcon.png' %}" alt="">
                <img class = "imageCall" src="{% static 'images/callIcon.png' %}" alt="">
            </div>
        </div>
    </div>
{% endblock %}
```
## Додаток my_codes \ My_codes application
```html
{% extends 'base.html' %}

{% load static %}

{% block link %}
    <link href="https://fonts.googleapis.com/css2?family=Arimo&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://indestructibletype.com/fonts/Jost.css" type="text/css" charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Anonymous+Pro:ital,wght@0,400;0,700;1,400;1,700&family=Jura:wght@300..700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'my_codes_app/my_codes.css' %}">
{% endblock %}

{% block title %}
    Мої QR-коди
{% endblock %}

{% block content %}
<script src="{% static 'js/my_codes.js'%}" defer></script>
    <div class="Screen">
        <div class="hat">
            <h1 class="h1Generate">Мої <span class="spanQR">QR</span>-коди</h1>
            <div class="urls">

                <div class="mainUrl">
                    <a href="{% url 'home_app' %}" class="mainPage">Головна</a>
                </div>
                {% if request.user.is_authenticated %}
                    <a href="{% url 'my_codes' %}" class="MyQRCodesPage" >Мої QR-коди</a>
                    <a href="{% url 'logout' %}" class="logout-button">Вийти з акаунту</a>
                {% else %}
                    <a href="/codes/my_codes/" class="MyQRCodesPage" >Мої QR-коди</a>    
                    <a href="{% url 'registration1' %}" class="registrationPage">Реєстрація</a>
                    <a href="{% url 'authorithation1' %}"class="authorizationPage">Авторизація</a>
                {% endif %}
                <h1 class="user-h1">{{request.user.username}}</h1>
            </div>
        </div>
            <div class = "flex-wraper">
                <div class="codes">
                {% if specific_qrcode %}
                        {% if specific_qrcode.is_working == True %}
                            <div class = "bg"></div>
                            <div class="form-qr">
                                <div class="qr-objects">
                                    <img src="{% static 'images/close.png'%}" class = "close-button" alt="">
                                    <h1 class="specific-title">Назва: {{specific_qrcode.name}}</h1>
                                    <h2 class="specific-url"><span class = "h1-url">Посилання: </span> {{specific_qrcode.url}}</h2>
                                    <h2 class="specific-date-created">Дата створення: {{specific_qrcode.date_created}}</h2>
                                    <h2 class="specific-date-expired">Дата видалення: {{date_expired}}</h2>
                                    <img class="specific-image" src="/media/{{specific_qrcode.image}}" alt=""> 
                                </div>
                            </div>
                        {% else %}
                        <div class = "bg"></div>
                        <div class="form-qr error-form">
                            <img src="{% static 'images/close.png'%}" class = "close-button for-error" alt="">
                            <div class="qr-objects">
                                <h1 class = "error-specific-text">Цей qr-код не працює! <br>Поповніть або повисіть підписку!</h1>
                            </div>
                        </div>
                        {% endif %}
                {% endif %}
                
                {% if delete %}
                        <form class="bg-form" method="post">
                            {% csrf_token %}
                            <div class="bg-form">
                                <div class="form-confirmed">
                                    <h1 class="h1-confirmed">Ви дійсно хочете видалити<br> цей QR-код?</h1>
                                    <button type="submit" class="confirm-delete">Так</button>
                                    <input type="text" name="form-delete" hidden>
                                </div>
                            </div>
                        </form>
                    {% endif %}

                    {% for user in User %}
                        {% if user.id == current_user.id %}
                            {% for qrcode in QR_Codes %}
                                {% if user.id == qrcode.user_id %}
                                        <div class="bg-qr-сode">
                                            {% if qrcode.is_working %}
                                                <div class="qr-code">
                                                    <form method="post" class="form1">
                                                        {% csrf_token %}
                                                        <img src="/media/{{qrcode.image}}" alt="" class="qr-code-img">
                                                        <button class="qr-code-title" type="submit" id="{{qrcode.id}}">{{qrcode.name}}</button>
                                                        <h2 class="qr-code-date"><span>Дата створення: <br> </span>{{qrcode.date_created}}</h2>
                                                        <input type="text" name = "specific_qr" hidden value="11">
                                                    </form>
                                                    <form method="post" class="form2">
                                                        {% csrf_token %}
                                                        <div class="buttons-download-delete">
                                                            <a class="qr-code-button" type="submit" href="/media/qr_codes/{{user.username}}/{{qrcode.name}}.png" download="{{qrcode.name}}.png">Скачати</a>
                                                            <button class="button-delete" id="{{qrcode.id}}">
                                                                <img class="bin-image" src="{% static 'images/bin.png' %}" alt="">
                                                            </button>
                                                            <input type="hidden" name="button-delete">
                                                        </div>
                                                    </form>
                                                </div>
                                            {% else %}
                                                <div class="qr-code">
                                                    <form method="post" class="form1">
                                                        {% csrf_token %}
                                                        <img src="/media/{{qrcode.image}}" alt="" class="qr-code-img doesnt-work">
                                                        <div class = "error-name">
                                                            <img src="{% static 'images/icon_error.png'%}" class = "error-image"alt="">
                                                            <button class="qr-code-title error-button" type="submit" id="{{qrcode.id}}">{{qrcode.name}}</button>
                                                            
                                                        </div>
                                                        <h2 class="qr-code-date"><span>Дата створення: <br> </span>{{qrcode.date_created}}</h2>
                                                        <input type="text" name = "specific_qr" hidden value="11">
                                                    </form>
                                                    <form method="post" class="form2">
                                                        {% csrf_token %}
                                                        <div class="buttons-download-delete">
                                                            <a class="qr-code-button" type="submit" href="/media/qr_codes/{{user.username}}/{{qrcode.name}}.png" download="{{qrcode.name}}.png">Скачати</a>
                                                            <button class="button-delete" id="{{qrcode.id}}">
                                                                <img class="bin-image" src="{% static 'images/bin.png' %}" alt="">
                                                            </button>
                                                            <input type="hidden" name="button-delete">
                                                        </div>
                                                    </form>
                                                </div>
                                            {% endif %}
                                        </div>

                                {% endif %}
                            {% endfor %}
                        {% endif %}
                    {% endfor %}
                </div>
            </div>
        <div class="contacts" style="padding-top: 29px;">
            <div class="allIcons">
                <img class="imageTelegram" src="{% static 'images/telegramIcon.png' %}" alt="">
                <img class="imageViber" src="{% static 'images/viberIcon.png' %}" alt="">
                <img class="imageCall" src="{% static 'images/callIcon.png' %}" alt="">
            </div>
        </div>
    </div>

    <script src="{% static 'js/my_codes.js'%}"></script>
{% endblock %}
```

## Додаток contacts_app \ Contacts_app application
```html
{% extends 'base.html' %}

{% load static %}

{% block link %}
    <link href="https://fonts.googleapis.com/css2?family=Arimo&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://indestructibletype.com/fonts/Jost.css" type="text/css" charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Anonymous+Pro:ital,wght@0,400;0,700;1,400;1,700&family=Jura:wght@300..700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'contacts_app/contacts.css' %}">
{% endblock %}

{% block title %}
    Сторінка контактів
{% endblock %}

{% block content %}
    <div class = "Screen">
        <div class = "hat">
            <h1 class = "h1Generate">Виникли питання? <br> Звертайся до служби підтримки!
            </h1>
            <div class = "urls">
                <div class = "mainUrl">
                    <a href = "{% url 'home_app'%}" class = "mainPage">Головна</a>
                </div>
                {% if request.user.is_authenticated %}
                    <h1 class = "user-h1">{{request.user.username}}</h1>
                    <a href="{% url 'my_codes' %}" class = "MyQRCodesPage" >Мої QR-коди</a>
                    <a href = "{% url 'logout' %}"class = "logout-button">Вийти з акаунту</a>
                {% else %}
                    <a href="/codes/my_codes/" class = "MyQRCodesPage" >Мої QR-коди</a>    
                    <a href="/registration/informationabout/" class = "registrationPage">Реєстрація</a>
                    <a href="/authorithation/logininformation/"class = "authorizationPage">Авторизація</a>
                    
                {% endif %}
                </div>
            </div>
        <main>
            <div class="main-form">
                <div class="gmail-form">
                    <h2 class="gmail-text">Електронна пошта:</h2>
                    <h2 class="gmail">qrprojectdjangoteam2@gmail.com</h2>
                </div>
                <div class="phone-form">
                    <h2 class="phone-text">Номер телефона:</h2>
                    <h2 class="phone">+380 68 206 79 59</h2>
                </div>
            </div>
            <div class = "contacts" style="padding-top: 86px;">
                <div class = "allIcons">
                    <img class = "imageTelegram" src="{% static 'images/telegramIcon.png' %}" alt="">
                    <img class = "imageViber" src="{% static 'images/viberIcon.png' %}" alt="">
                    <img class = "imageCall" src="{% static 'images/callIcon.png' %}" alt="">
                </div>
            </div>
        </main>
    </div>
{% endblock %}
```
## Додаток subscribe \ Subscribe application

```html
{% extends 'base.html' %}
{% load static %}

{% block title %}
    Підписка
{% endblock %}

{%  block link %}
    <link href="https://fonts.googleapis.com/css2?family=Arimo&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://indestructibletype.com/fonts/Jost.css" type="text/css" charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Anonymous+Pro:ital,wght@0,400;0,700;1,400;1,700&family=Jura:wght@300..700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Anonymous+Pro:ital,wght@0,400;0,700;1,400;1,700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Jura:wght@300..700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'subscribe/css/subscribe.css' %}">
{% endblock %}
{% block content %}
    <div class = "screen">
        <div class = "hat">
            <h1 class = "subscribe-text">Підписка</h1>
            <div class = "urls">
                <div class = "mainUrl">
                    <a href = "{% url 'home_app' %}" class = "mainPage">Головна</a>
                </div>
                {% if request.user.is_authenticated %}

                    <a href="{% url 'my_codes' %}" class = "MyQRCodesPage" >Мої QR-коди</a>
                    <a href = "{% url 'logout' %}"class = "logout-button">Вийти з акаунту</a>
                {% else %}
                    <a href="/codes/my_codes/" class = "" >Мої QR-коди</a>    
                    <a href="{% url 'registration1' %}" class = "registrationPage">Реєстрація</a>
                    <a href="{% url 'authorithation1' %}"class = "authorizationPage">Авторизація</a>
                    
                {% endif %}
                <h1 class = "user-h1">{{request.user.username}}</h1>
            </div>
        </div>
        {% if message %}
            <div class = "bg"></div>
            <div class="form-qr">

                <div class="qr-objects">
                    <img src="{% static 'images/close.png'%}" class = "close-button" alt="">
                    <h1 class = "h1-vitannya">Вітаємо!</h1>
                    <h1 class = "subscribe-type">{{message}}</h1>
                    <a class = "url-home" href="{% url 'home_app'%}">На головну</a>
                </div>
            </div>
        {% endif %}
        <form method="post" class = "subscribe-form">
            {% csrf_token%}
            <div class = "form"> 
                    <h1 class = "subscribe-buy">Оформлення підписки</h1>    

                    <div class = "form-inputs">

                        <div class = "input-number">
                            <h1 class = "number-text">Номер платіжної карти</h1>
                            <input  class = "number-input" name = "card" type="text">
                            <h1 class = "number-clue">Наприклад: 1234 5678 9012 3456</h1>
                        </div>

                        <div class = "input-cvv">
                            <h1 class = "cvv-text">CVV/CVC код</h1>
                            <input class = "cvv-input" name = "cvv" type="password">
                            <h1 class = "cvv-clue">Наприклад: 123</h1>
                        </div>
                        <div class = "input-expiration">
                            <h1 class = "expiration-text">Термін придатності</h1>
                            <input class = "expiration-input" name = "date" type="month">
                            <h1 class = "expiration-clue">Наприклад: 12/24</h1>
                        </div>
                        {% if subscribe_desktop%}
                            <div class = "count-input">
                                <h1 class = "count-qrs">Кількість QR-кодів</h1>
                                <select name="count" class = "input-count">
                                    <option value="5">5 QR-кодів(0.5$)</option>
                                    <option value="10">10 QR-кодів(1$)</option>
                                    <option value="20">20 QR-кодів(2$)</option>
                                </select>
                            </div>
                        {% endif %}
                    </div>
                    <div class = "subscribe-button" >
                        <button class = "button" id = "button" type="submit">Оформити підписку</button>
                    </div>
            </div>
        </form>
        <div class = "contacts" style="padding-top: 25px;">
            <div class = "allIcons">
                <img class = "imageTelegram" src="{% static 'images/telegramIcon.png' %}" alt="">
                <img class = "imageViber" src="{% static 'images/viberIcon.png' %}" alt="">
                <img class = "imageCall" src="{% static 'images/callIcon.png' %}" alt="">
            </div>
        </div>
    </div>
    <script src = "{% static 'subscribe/js/subscribe.js'%}"></script>
{% endblock %}
```