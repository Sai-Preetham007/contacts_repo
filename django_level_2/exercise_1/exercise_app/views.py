from django.shortcuts import render
# from exercise_app.models import User
from .forms import NewUser

# Create your views here.
def index(request):
    return render(request, "index.html")

# def users(request):
#     users_list = User.objects.order_by("first_name")
#     print(users_list)
#     users_dict = {"user" : users_list}
#     return render(request, "users.html", context=users_dict)


def users(request):
    form = NewUser()
    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Form is Invalid.")
    return render(request, "users.html", {"form" : form})