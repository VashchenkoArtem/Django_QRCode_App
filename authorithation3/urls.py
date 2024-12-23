from django.urls import path, include
from .views import render_authorithation3
from authorithation1.views import render_authorithation1
from authorithation2.views import render_authorithation2

urlpatterns = [
    path('succesauthorithation/', render_authorithation3),
    path('logininformation/', render_authorithation1),
    path('loginemail/', render_authorithation2)
]