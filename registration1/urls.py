from django.urls import path, include
from .views import render_registration1
from registration3.views import render_registration3
from registration_2.views import render_registration2


urlpatterns = [
    path('informationabout/', render_registration1),
    path('sendingemail/', render_registration2),
    path('succesregistration/', render_registration3)
]