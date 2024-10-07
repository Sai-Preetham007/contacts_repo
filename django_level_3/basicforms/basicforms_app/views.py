from django.shortcuts import render
from .forms import form_name

# Create your views here.
def index(request):
    return render(request, "index.html")

def forms(request):
    form = form_name(request.POST)
    if form.is_valid():
        print("Name : " + form.cleaned_data["name"])
        print("Email : " + form.cleaned_data["email"])
        print("Text : " + form.cleaned_data["text"])


    return render(request, "forms.html", context={"form" : form})