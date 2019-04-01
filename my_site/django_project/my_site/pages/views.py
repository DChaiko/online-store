from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, world.</h1>")

def contacts(request):
    return HttpResponse("<h1>Contacts</h1> \
        <table><tr><td>Чайко Дмитрий Сергеевич</td><td>+3753366***</td></tr><tr><td>Директор</td><td>+375********</td></tr></table>")
