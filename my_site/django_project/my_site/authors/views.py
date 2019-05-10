from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from authors.models import Author
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class AuthorView(DetailView):
    model = Author
    #template_name = 'directory/templates/author_details.html'
    slug_url_kwarg = "not_slug"

class AuthorList(ListView):
    model = Author
    def get_queryset(self):
        qs = super().get_queryset()
        data = self.request.GET.get('key', None)
        if data != None:
            qs = qs.filter(name__contains=data)
            return qs
        return qs
        #redirect = self.request.POST.get('detail')
        #if redirect:
        #    return reverse_lazy('author-create')

class CreateAuthor(CreateView):
    model = Author
    fields = ['name']
    def get_success_url(self):
        redirect = self.request.POST.get('detail')
        return reverse_lazy('author-detail-list')

class UpdateAuthor(UpdateView):
    model = Author
    fields = ['name']
    def get_success_url(self):
        redirect = self.request.POST.get('author-detail-list')
        return reverse_lazy('author-detail-list')

class DeleteAuthor(DeleteView):
    model = Author
    success_url = reverse_lazy('author-detail-list')