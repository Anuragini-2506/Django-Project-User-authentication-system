from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib import messages
from django.contrib.auth.models import User

def loginUser(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      print(username, password)
      user = authenticate(username=username, password=password)
      if user is not None:
      # A backend authenticated the credentials
         messages.success(request, "Welcome " + str(user.get_username()) + " to the Icecream World :) ")
         login(request, user)
         return redirect("/")
      else:
         messages.warning(request, "Either the user is not registered or credentials are wrong :(")
         return render(request, 'login.html')
      # No backend authenticated the credentials# Create your views here.

   return render(request, 'login.html')

def logoutUser(request):
   logout(request)
   return redirect("/welcome")  


def signupUser(request):
   if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         print(username, password)
         user = authenticate(username=username, password=password)
         if user is not None:
         # A backend authenticated the credentials
            messages.warning(request, "User with username  " + str(user.get_username()) + " is already registered :) ")
            return redirect("/signup")
         else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "User with username "+str(username) +" created Successfully :) \n Kindly login once with your specified credentials")
            return render(request, 'login.html')
         # No backend authenticated the credentials# Create your views here.

   return render(request, 'signup.html')
