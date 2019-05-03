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
from django.urls import path, include
from pages import views
from pages.views import HomeView
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
    path('', HomeView.as_view() ),
    path('contacts/', views.contacts),
    path('admin/', admin.site.urls),
    path('book/', include('books.urls')),
    path('', include('directory.urls')),
    
]

