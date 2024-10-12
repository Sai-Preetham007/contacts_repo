from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("home/", views.home, name="home"),
    path("home/display", views.display, name="display"),
    path("home/add", views.add, name="add")
]