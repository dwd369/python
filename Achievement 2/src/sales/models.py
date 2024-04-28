from django.db import models
from datetime import datetime


# Create your models here.
class Sale(models.Model):
    # book = models.ForeignKey(Book, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    price = models.FloatField(default = 0)
    date_create = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.name)