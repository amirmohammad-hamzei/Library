from django.contrib import admin
from .models import Author, Book, Reservation


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_date')
    #search_fields = ('name',)
    #list_filter = ('birth_date',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    #search_fields = ('title',)
    #list_filter = ('publication_date', 'author')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'start_date', 'end_date')
    search_fields = ('book__title', 'user__username')
    list_filter = ('start_date', 'end_date')