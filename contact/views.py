from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
    return render(request,'home.html')
