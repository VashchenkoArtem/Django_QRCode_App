from django.shortcuts import render

# Create your views here.

def render_my_codes(request):
    return render(request, "my_codes/my_codes.html")