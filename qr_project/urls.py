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

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", render_home_app),
    path('codes/', include('my_codes.urls')),
    path('contacts/', render_contacts),
    path('registration/', include('registration1.urls')),
    path('authorithation/', include('authorithation3.urls'))
]