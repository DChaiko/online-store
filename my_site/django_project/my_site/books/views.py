from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from books.models import Book
# Create your views here.

class BookView(DetailView):
    model = Book
    #template_name = 'directory/templates/author_details.html'
    slug_url_kwarg = "not_slug"

class BookList(ListView):
    model = Book
    def get_queryset(self):
        qs = super().get_queryset()
        data = self.request.GET.get('key', None)
        if data != None:
            qs = qs.filter(book_name__contains=data)
            return qs
        return qs