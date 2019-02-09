from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print(request.method)
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        print(name,email,subject,message)
    return render(request,'home.html')
