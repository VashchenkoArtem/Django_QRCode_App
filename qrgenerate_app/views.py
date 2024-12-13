from django.shortcuts import render

# Create your views here.

def qr_generate_app(request):
    return render(request, "qrgenerate_app/index.html")