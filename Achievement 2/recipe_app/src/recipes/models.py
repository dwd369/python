from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length = 120, default = 'No name...')
    cook_time = models.PositiveIntegerField(default = 0)
    ingredients = models.CharField(help_text = "enter ingredient(s) separate by comma", default = '', max_length = 500,)
    description = models.CharField(default = '', max_length = 500)

    def __str__(self):
        return str(self.name)