from django.shortcuts import render, redirect

# Create your views here.
def render_authorithation3(request):
    if request.method == 'POST':
        return redirect("/")
    return render(request, "authorithation3/authorithation3.html")