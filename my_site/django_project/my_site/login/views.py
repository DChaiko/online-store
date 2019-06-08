from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

class LoginView(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True
    redirect_field_name = 'home'

class LogoutView(LogoutView):
    next_page = 'home'

class PasswordChangeView(PasswordChangeView):
    success_url = 'home'

class UserPage(DetailView):
    model = User