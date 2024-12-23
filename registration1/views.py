from django.shortcuts import render

# Create your views here.

def render_registration1(request):
    return render(request, "registration1/index.html")