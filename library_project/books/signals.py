from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Reservation, Book

@receiver(post_delete, sender=Reservation)
def update_book_availability(sender, instance, **kwargs):
    # Update book availability after reservation is deleted

    book = instance.book
    book.is_available = True
    book.save()
