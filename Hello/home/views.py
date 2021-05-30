from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def index(request):
   # context = {
   #    'variable1':"This is sent",
   #    'variable2':"THIs isj kasdjfk"
   # }
   # return render(request, 'index.html', context)
   print("Hello")
   if request.user.is_anonymous:
      print("aksdj")
      return redirect("/welcome")
   return render(request, 'index.html')


def about(request):
   return render(request, 'about.html')
   # return HttpResponse('This is about page')

def services(request):
   return render(request, 'services.html')


def contact(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      message = request.POST.get('message')
      contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
      contact.save()
      messages.success(request, "Your message has been sent successfully...\nEnjoy you icecream day :)")
   return render(request, 'contact.html')


def welcome(request):
   return render(request, 'welcome.html')