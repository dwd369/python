from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length = 120, default = 'No name...')
    cook_time = models.PositiveIntegerField(default = 0)
    ingredients = models.CharField(help_text = "enter ingredient(s) separate by comma", default = '', max_length = 500,)
    description = models.CharField(default = '', max_length = 500)
    date_create = models.DateTimeField(auto_now_add = True)
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def get_absolute_url(self):
       return reverse ('recipes:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.name)