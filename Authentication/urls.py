from django.urls import path
from .views import LoginFormView, Login, logoutBtn

urlpatterns = [
    path("login", LoginFormView.as_view(), name="Login"),
    path("login_request", Login.as_view(), name="LoginRequest"),
    path("logout", logoutBtn, name="Logout")
]