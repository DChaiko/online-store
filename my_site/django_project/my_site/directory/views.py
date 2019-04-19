from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from directory.models import Author
from directory.models import Serie
from directory.models import Genre
from directory.models import Publisher
# Create your views here.

class AuthorView(DetailView):
    model = Author
    #template_name = 'directory/templates/author_details.html'
    slug_url_kwarg = "not_slug"

class SerieView(DetailView):
    model = Serie
    slug_url_kwarg = "not_slug"

class GenreView(DetailView):
    model = Genre
    slug_url_kwarg = "not_slug"

class PublisherView(DetailView):
    model = Publisher
    slug_url_kwarg = "not_slug"

class AuthorList(ListView):
    model = Author

class SerieList(ListView):
    model = Serie

class GenreList(ListView):
    model = Genre

class PublisherList(ListView):
    model = Publisher