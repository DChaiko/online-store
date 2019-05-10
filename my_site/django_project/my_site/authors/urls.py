from django.urls import path, include
from django.contrib import admin
from authors.views import AuthorList, CreateAuthor, UpdateAuthor, DeleteAuthor, AuthorView


urlpatterns = [
    path('author/<int:pk>/', AuthorView.as_view(), name = 'author-detail-view'),
    path('author_list/', AuthorList.as_view(), name = 'author-detail-list'),
    path('create_author/', CreateAuthor.as_view(), name = 'author-create'),
    path('update_author/<int:pk>/', UpdateAuthor.as_view(), name = 'author-update'),
    path('delete_author/<int:pk>/', DeleteAuthor.as_view(), name = 'author-delete'),
]