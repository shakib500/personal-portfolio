from django.http import HttpResponse
from django.shortcuts import render
from .models import contact

def home(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        print(name)

        contact_details = contact()
        contact_details.name = name
        contact_details.email = email
        contact_details.subject = subject
        contact_details.message = message
        contact_details.save()

    return render(request,'home.html')
