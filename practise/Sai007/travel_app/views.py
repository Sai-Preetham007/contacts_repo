from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest = Destination.objects.all()
    return render(request, "travel_app/index.html", {"destinations" : dest})

def login(request):
    return render(request, "travel_app/login.html")