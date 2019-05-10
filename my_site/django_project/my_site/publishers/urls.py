from django.urls import path, include
from django.contrib import admin
from publishers.views import PublisherList, PublisherView, UpdatePublisher, DeletePublisher, CreatePublisher

urlpatterns = [
    path('publisher/<int:pk>/', PublisherView.as_view(), name = 'publisher-detail-view'),
    path('publisher_list/', PublisherList.as_view(), name = 'publisher-detail-list'),
    path('create_publisher/', CreatePublisher.as_view(), name = 'publisher-create'),
    path('update_publisher/<int:pk>/', UpdatePublisher.as_view(), name = 'publisher-update'),
    path('delete_publisher/<int:pk>/', DeletePublisher.as_view(), name = 'publisher-delete'),
]