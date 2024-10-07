from django.shortcuts import render
from second_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    date_dict = {"access_records" : AccessRecord.objects.order_by("date")}
    return render(request, "index.html", context = date_dict)