from django.db import models
from datetime import datetime
from books.models import Book



# Create your models here.
class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.FloatField(help_text = 'in US dollars $', default=0)
    date_create = models.DateTimeField(blank=True)

    def __str__(self):
        return f"id: {self.id}, book: {self.book.name}, quantity: {self.quantity}, price: {self.price}, date_created: {self.date_create}"