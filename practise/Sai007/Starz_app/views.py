from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "Starz_app/home.html", {"name" : "Sai Preetham"})

def add(request):
    val1 = request.POST.get("num1", 0)
    val2 = request.POST.get("num2", 0)
    res = int(val1) + int(val2)
    return render(request, "Starz_app/base.html", {"result" : res})