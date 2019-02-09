from django.http import HttpResponse
from django.shortcuts import render
from .models import contact

def home(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contact = contact()
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()

    return render(request,'home.html')
