from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from genres.models import Genre
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class GenreView(DetailView):
    model = Genre
    slug_url_kwarg = "not_slug"

class GenreList(ListView):
    model = Genre
    def get_queryset(self):
        qs = super().get_queryset()
        data = self.request.GET.get('key', None)
        if data != None:
            qs = qs.filter(genre__contains=data)
            return qs
        return qs

class CreateGenre(CreateView):
    model = Genre
    fields = ['genre']
    def get_success_url(self):
        redirect = self.request.POST.get('author-detail-list')
        return reverse_lazy('genre-detail-list')

class UpdateGenre(UpdateView):
    model = Genre
    fields = ['genre']
    success_url = reverse_lazy('genre-detail-list')

class DeleteGenre(DeleteView):
    model = Genre
    success_url = reverse_lazy('genre-detail-list')