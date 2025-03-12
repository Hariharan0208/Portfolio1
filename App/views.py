from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'Portfolio.html')

def submitform(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('contactEmail')
        subject = request.POST.get('contactSubject')
        description = request.POST.get('contactMessage')

        subject = 'Job Portfolio Update'
        message = f"Name : {name},\nEmail : {email}.\nSubject: {subject}\nDescription: {description}"
        recipient = 'hariharanmmh@gmail.com'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
        return redirect('index')
