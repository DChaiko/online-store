from django.shortcuts import render
from django.views.generic.detail import DetailView
from books.models import Book
# Create your views here.

class BookView(DetailView):
    model = Book
    #template_name = 'directory/templates/author_details.html'
    slug_url_kwarg = "not_slug"