"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views
from directory.views import AuthorView
from directory.views import SerieView
from directory.views import GenreView
from directory.views import PublisherView
from books.views import BookView
from books.views import BookList, CreateBook
from directory.views import AuthorList
from directory.views import SerieList
from directory.views import GenreList
from directory.views import PublisherList, CreateAuthor, CreateSerie, CreateGenre, CreatePublisher


urlpatterns = [
    path('', views.home),
    path('contacts/', views.contacts),
    path('admin/', admin.site.urls),
    path('author/<int:pk>/', AuthorView.as_view(), name = 'author-detail-view'),
    path('serie/<int:pk>/', SerieView.as_view(), name = 'serie-detail-view'),
    path('genre/<int:pk>/', GenreView.as_view(), name = 'genre-detail-view'),
    path('publisher/<int:pk>/', PublisherView.as_view(), name = 'publisher-detail-view'),
    path('book/<int:pk>/', BookView.as_view(), name = 'book-detail-view'),
    path('author_list/', AuthorList.as_view(), name = 'author-detail-list'),
    path('serie_list/', SerieList.as_view(), name = 'serie-detail-list'),
    path('genre_list/', GenreList.as_view(), name = 'genre-detail-list'),
    path('publisher_list/', PublisherList.as_view(), name = 'publisher-detail-list'),
    path('book_list/', BookList.as_view(), name = 'book-detail-list'),
    path('create_author/', CreateAuthor.as_view(), name = 'author-create'),
    path('create_serie/', CreateSerie.as_view(), name = 'serie-create'),
    path('create_genre/', CreateGenre.as_view(), name = 'genre-create'),
    path('create_publisher/', CreatePublisher.as_view(), name = 'publisher-create'),
    path('create_book/', CreateBook.as_view(), name = 'book-create'),
]
