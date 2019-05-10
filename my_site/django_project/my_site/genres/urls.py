from django.urls import path, include
from django.contrib import admin
from genres.views import GenreList, CreateGenre, GenreView, UpdateGenre, DeleteGenre

urlpatterns = [
    path('genre/<int:pk>/', GenreView.as_view(), name = 'genre-detail-view'),
    path('genre_list/', GenreList.as_view(), name = 'genre-detail-list'),
    path('create_genre/', CreateGenre.as_view(), name = 'genre-create'),
    path('update_genre/<int:pk>/', UpdateGenre.as_view(), name = 'genre-update'),
    path('delete_genre/<int:pk>/', DeleteGenre.as_view(), name = 'genre-delete'),
]