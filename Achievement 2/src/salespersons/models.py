from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Salesperson(models.Model):
    username = models.OneToOneField(User, on_delete = models.CASCADE, default = 'No username')
    name = models.CharField(max_length = 120, default = 'No name')
    bio = models.TextField(default = 'No bio...')


    def __str__(self):
        return str(self.name)