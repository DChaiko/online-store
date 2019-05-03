from django.urls import path, include


from django.contrib import admin
from books.views import BookView
from books.views import BookList, CreateBook, UpdateBook, DeleteBook



urlpatterns = [
    path('create_book/', CreateBook.as_view(), name = 'book-create'),
    path('book_list/', BookList.as_view(), name = 'book-detail-list'),
    path('<int:pk>/', BookView.as_view(), name = 'book-detail-view'),
    path('update_book/<int:pk>/', UpdateBook.as_view(), name = 'book-update'),
    path('delete_book/<int:pk>/', DeleteBook.as_view(), name = 'book-delete'),
]


