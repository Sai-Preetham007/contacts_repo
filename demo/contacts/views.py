from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "contacts/signup.html")

def register(request):
    first_name = request.POST.get("firstname")
    last_name = request.POST.get("lastname")
    email = request.POST.get("email")
    mobile_number = request.POST.get("mobilenumber")
    password = request.POST.get("password")

    model = User(First_Name=first_name, Last_Name=last_name, Email=email, Mobile_Number=mobile_number, Password=password)
    model.save()

    return render(request, "contacts/thanks.html")

def login(request):
    return render(request, "contacts/login.html")

def login_verify(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(Email = email)
            if user.Password == password:
                user_name = user.First_Name
                return render(request, "contacts/home.html", {"user_name":user_name})
            else:
                return HttpResponse("Invalid email or password")
        except User.DoesNotExist:
            return HttpResponse("Invalid email or password")