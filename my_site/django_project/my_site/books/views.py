from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from books.models import Book
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class CreateBook(CreateView):
    model = Book
    fields = ['book_name', 'cover', 'price', 'author', 'serie', 'genre', 'pub_year', 'pages',  
    'binding', 'form', 'isbn', 'weigth', 'publisher', 'availability', 'activ', 'rating']
    def get_success_url(self):
        #redirect = self.request.POST.get('author-detail-list')
        return reverse_lazy('book-detail-list')

class UpdateBook(UpdateView):
    model = Book
    fields = ['book_name', 'cover', 'price', 'author', 'serie', 'genre', 'pub_year', 'pages',  
    'binding', 'form', 'isbn', 'weigth', 'publisher', 'availability', 'activ', 'rating']
    success_url = reverse_lazy('book-detail-list')

class DeleteBook(DeleteView):
    model = Book
    success_url = reverse_lazy('book-detail-list')

class BookCard(ListView):
    model = Book
    template_name = 'home.html'