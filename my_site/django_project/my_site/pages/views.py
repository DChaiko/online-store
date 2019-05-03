from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


def contacts(request):
    return HttpResponse("<h1>Contacts</h1> \
        <table><tr><td>Чайко Дмитрий Сергеевич</td><td>+3753366***</td></tr><tr><td>Директор</td><td>+375********</td></tr></table>")

class HomeView(TemplateView):
    template_name = "home.html"