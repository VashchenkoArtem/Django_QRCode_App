from django.urls import path, include
from .views import render_registration1
from registration3.views import render_registration3


urlpatterns = [
    path('informationabout/', render_registration1, name = "registration1"),
    path('succesregistration/', render_registration3, name = "registration3")
]