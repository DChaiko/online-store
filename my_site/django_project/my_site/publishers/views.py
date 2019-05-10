from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from publishers.models import Publisher
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class PublisherView(DetailView):
    model = Publisher
    slug_url_kwarg = "not_slug"

class PublisherList(ListView):
    model = Publisher
    def get_queryset(self):
        qs = super().get_queryset()
        data = self.request.GET.get('key', None)
        if data != None:
            qs = qs.filter(pub__contains=data)
            return qs
        return qs

class CreatePublisher(CreateView):
    model = Publisher
    fields = ['pub']
    def get_success_url(self):
        redirect = self.request.POST.get('author-detail-list')
        return reverse_lazy('publisher-detail-list')

class UpdatePublisher(UpdateView):
    model = Publisher
    fields = ['pub']
    success_url = reverse_lazy('publisher-detail-list')

class DeletePublisher(DeleteView):
    model = Publisher
    success_url = reverse_lazy('publisher-detail-list')