from django.urls import path
from qrgenerate_app.views import qr_generate_app
from .views import render_my_codes

urlpatterns = [
    path('qrgenerate/', qr_generate_app, name = "generate"),
    path('my_codes/', render_my_codes, name = "my_codes")
]