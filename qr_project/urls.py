"""
URL configuration for qr_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home_app.views import render_home_app
from contacts_app.views import render_contacts
from authorithation3.views import render_authorithation3
from subscribe.views import render_subscribe
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", render_home_app, name="home_app"),
    path('codes/', include('my_codes.urls'), name="my_codes_urls"),
    path('contacts/', render_contacts, name="contacts"),
    path('registration/', include('registration1.urls'), name="registration1_urls"),
    path('authorithation/', include('authorithation3.urls'), name="authorithation3_urls"),
    path('subscribe/', render_subscribe, name="subscribe")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)