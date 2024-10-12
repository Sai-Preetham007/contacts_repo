from django.shortcuts import render, HttpResponse
from .models import User, Contact, User_Contacts

# Create your views here.
def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobilenumber")
        password = request.POST.get("password")

        user = User(First_Name=first_name, Last_Name=last_name, Email=email, Mobile_Number=mobile, Password=password)
        user.save()

        return render(request, "contacts_app/thanks.html")

    return render(request, "contacts_app/signup.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(Email=email)
            if user.Password == password:
                request.session["email"] = email
                global user_name
                user_name = user.First_Name
                return render(request, "contacts_app/home.html", {"user_name": user_name})
            else:
                return render(request, "contacts_app/login.html", {"error_msg":"Invalid email or password"})
        except User.DoesNotExist:
            return render(request, "contacts_app/login.html", {"error_msg":"Invalid email or password"})

    return render(request, "contacts_app/login.html")

def home(request):
    return render(request, "contacts_app/home.html", {"user_name": user_name})
    
def display(request):
    email = request.session.get("email")
    contacts = []

    try:
        user = User.objects.get(Email=email)
        contacts = User_Contacts.objects.filter(user=user)

        return render(request, "contacts_app/display.html", {"contacts": contacts, "user_name": user_name})

    except User.DoesNotExist:
        return render(request, "contacts_app/display.html", {"contacts": contacts, "user_name": user_name})


def add(request):
    if request.method == "POST":
        email = request.session.get("email")
        full_name = request.POST.get("full_name")
        mobile_number = request.POST.get("mobile_number")

        if not full_name or not mobile_number:
            return render(request, "contacts_app/add.html")

        try:
            user = User.objects.get(Email=email)

            contact, created = Contact.objects.get_or_create(Full_Name=full_name, Mobile_Number=mobile_number)
            User_Contacts.objects.get_or_create(user=user, contact=contact)

            return render(request, "contacts_app/home.html", {"user_name": user_name})

        except User.DoesNotExist:
            return render(request, "contacts_app/add.html", {"user_name": user_name})

    return render(request, "contacts_app/add.html", {"user_name": user_name})