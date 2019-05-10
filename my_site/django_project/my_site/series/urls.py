from django.urls import path, include
from django.contrib import admin
from series.views import SerieView, CreateSerie, UpdateSerie, DeleteSerie, SerieList

urlpatterns = [
    path('serie/<int:pk>/', SerieView.as_view(), name = 'serie-detail-view'),
    path('serie_list/', SerieList.as_view(), name = 'serie-detail-list'),
    path('create_serie/', CreateSerie.as_view(), name = 'serie-create'),
    path('update_serie/<int:pk>/', UpdateSerie.as_view(), name = 'serie-update'),
    path('delete_serie/<int:pk>/', DeleteSerie.as_view(), name = 'serie-delete'),
]