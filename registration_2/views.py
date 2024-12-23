from django.shortcuts import render

# Create your views here.
def render_registration2(request):
    return render(request, "registration_2/index.html")