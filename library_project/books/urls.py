# books/urls.py

from django.urls import path
from .views import BookList, BookCreate, BookDetail, AuthorList, AuthorCreate, AuthorDetail, ReservationList, \
    ReservationDetail

urlpatterns = [
    path('book_list/', BookList.as_view(), name='book_list'),
    path('add_book/', BookCreate.as_view(), name='add_book'),
    path('book_detail/<int:pk>/', BookDetail.as_view(), name=''),
    path('author_list/', AuthorList.as_view(), name='author_list'),
    path('add_author/', AuthorCreate.as_view(), name='add_author'),
    path('author_detail/<int:pk>/', AuthorDetail.as_view(), name=''),
    path('reservations_list/', ReservationList.as_view(), name='reservations'),
    path('reservations_detail/<int:pk>/', ReservationDetail.as_view(), name='reservations_detail'),
    path('reservations_detail/', ReservationDetail.as_view(), name='reservations_detail'),

]
