from django.shortcuts import render

# Create your views here.

def render_subscribe(request):
    return render(request, 'subscribe/subscribe.html')