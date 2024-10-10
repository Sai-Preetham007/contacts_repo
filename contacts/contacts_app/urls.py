from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("thanks/", views.thanks, name="thanks"),
    path("login/", views.login, name="login"),
    path("home/", views.login_verified, name="login_verified"),
    path("home/display", views.display, name="display")
]