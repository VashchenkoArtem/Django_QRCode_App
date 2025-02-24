from django.shortcuts import render
from django.http import  HttpRequest
def render_contacts(request: HttpRequest):
    return render(request, 'contacts_app/contacts.html')
