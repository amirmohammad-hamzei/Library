# books/serializers.py

from rest_framework import serializers
from .models import Author, Book, Reservation


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'genre', 'author', 'is_available', 'published_date']
        read_only_fields = ['id']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'nationality', 'books', 'biography']
        read_only_fields = ['id', 'books']


class ReservationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Reservation
        fields = ['book', 'user','start_date', 'end_date']
        read_only_fields = ['id', 'start_date']

