from django.shortcuts import render, HttpResponse
from .models import User, User_Contacts

# Create your views here.
def index(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "contacts_app/signup.html")

def thanks(request):
    first_name = request.POST.get("firstname")
    last_name = request.POST.get("lastname")
    email = request.POST.get("email")
    mobile = request.POST.get("mobilenumber")
    password = request.POST.get("password")

    user = User(First_Name=first_name, Last_Name=last_name, Email=email, Mobile_Number=mobile, Password=password)
    user.save()

    return render(request, "contacts_app/thanks.html")
    
def login(request):
    return render(request, "contacts_app/login.html")

def login_verified(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    
    try:
        user = User.objects.get(Email=email)
        if User.objects.get(Password=password):
            user_name = user.First_Name
            return render(request, "contacts_app/home.html", {"user_name": user_name})
        else:
            return render(request, "contacts_app/login.html", {"error_msg":"Invalid email or password"})
    except User.DoesNotExist:
        return render(request, "contacts_app/login.html", {"error_msg":"Invalid email or password"})
    
def display(request):
    contacts = User_Contacts.objects.all().values("Full_Name", "Mobile_Number")
    return render(request, "contacts_app/display.html", {"contacts": contacts})