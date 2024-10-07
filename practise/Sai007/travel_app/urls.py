from django.urls import path
from . import views

urlpatterns = [
    path("travel/", views.index),
    path("travel/login/", views.login, name="login")
    ]