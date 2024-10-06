from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("User/", views.login_verify, name="login_verify"),
    path("signup/", views.signup, name="signup"),
    path("register/", views.register, name="register")
    ]