from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from series.models import Serie
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class SerieView(DetailView):
    model = Serie
    slug_url_kwarg = "not_slug"

class SerieList(ListView):
    model = Serie
    def get_queryset(self):
        qs = super().get_queryset()
        data = self.request.GET.get('key', None)
        if data != None:
            qs = qs.filter(serie__contains=data)
            return qs
        return qs

class CreateSerie(CreateView):
    model = Serie
    fields = ['serie']
    def get_success_url(self):
        redirect = self.request.POST.get('author-detail-list')
        return reverse_lazy('serie-detail-list')

class UpdateSerie(UpdateView):
    model = Serie
    fields = ['serie']
    success_url = reverse_lazy('serie-detail-list')

class DeleteSerie(DeleteView):
    model = Serie
    success_url = reverse_lazy('serie-detail-list')