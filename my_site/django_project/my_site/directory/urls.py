from django.urls import path, include
from django.contrib import admin
from directory.views import AuthorList, SerieList, GenreList
from directory.views import PublisherList, CreateAuthor, CreateSerie, CreateGenre, CreatePublisher
from directory.views import AuthorView, SerieView, GenreView, PublisherView
from directory.views import UpdateAuthor, UpdateGenre, UpdateSerie, UpdatePublisher
from directory.views import DeleteAuthor, DeleteGenre, DeleteSerie, DeletePublisher

urlpatterns = [
    path('author/<int:pk>/', AuthorView.as_view(), name = 'author-detail-view'),
    path('serie/<int:pk>/', SerieView.as_view(), name = 'serie-detail-view'),
    path('genre/<int:pk>/', GenreView.as_view(), name = 'genre-detail-view'),
    path('publisher/<int:pk>/', PublisherView.as_view(), name = 'publisher-detail-view'),
    path('author_list/', AuthorList.as_view(), name = 'author-detail-list'),
    path('serie_list/', SerieList.as_view(), name = 'serie-detail-list'),
    path('genre_list/', GenreList.as_view(), name = 'genre-detail-list'),
    path('publisher_list/', PublisherList.as_view(), name = 'publisher-detail-list'),
    path('create_author/', CreateAuthor.as_view(), name = 'author-create'),
    path('create_serie/', CreateSerie.as_view(), name = 'serie-create'),
    path('create_genre/', CreateGenre.as_view(), name = 'genre-create'),
    path('create_publisher/', CreatePublisher.as_view(), name = 'publisher-create'),
    path('update_author/<int:pk>/', UpdateAuthor.as_view(), name = 'author-update'),
    path('update_genre/<int:pk>/', UpdateGenre.as_view(), name = 'genre-update'),
    path('update_serie/<int:pk>/', UpdateSerie.as_view(), name = 'serie-update'),
    path('update_publisher/<int:pk>/', UpdatePublisher.as_view(), name = 'publisher-update'),
    path('delete_author/<int:pk>/', DeleteAuthor.as_view(), name = 'author-delete'),
    path('delete_genre/<int:pk>/', DeleteGenre.as_view(), name = 'genre-delete'),
    path('delete_serie/<int:pk>/', DeleteSerie.as_view(), name = 'serie-delete'),
    path('delete_publisher/<int:pk>/', DeletePublisher.as_view(), name = 'publisher-delete'),

]