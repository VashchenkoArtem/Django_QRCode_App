from django.shortcuts import render

# Create your views here.
def render_contacts(request):
    return render(request, 'contacts_app/contacts.html')