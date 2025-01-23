from django.urls import path, include
from .views import render_authorithation3, logout_user
from authorithation1.views import render_authorithation1
from authorithation2.views import render_authorithation2


urlpatterns = [
    path('succesauthorithation/', render_authorithation3, name = "authorithation3"),
    path('logininformation/', render_authorithation1, name = "authorithation1"),
    path('loginemail/', render_authorithation2, name = "authorithation2"),
    path('logout/', logout_user, name = "logout")
]