from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView


# Create your views here.

class LoginView(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True
    redirect_field_name = 'home'

class LogoutView(LogoutView):
    next_page = 'home'

class PasswordChangeView(PasswordChangeView):
    success_url = 'home'