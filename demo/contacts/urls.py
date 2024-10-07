from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("User/", views.login_verify, name="login_verify"),
    path("signup/", views.signup, name="signup"),
    path("register/", views.register, name="register"),
    path("display/", views.display, name="display"),
    path("add/", views.add, name="add"),
    path("modify/", views.modify, name="modify"),
    path("delete/", views.delete, name="delete")
    ]