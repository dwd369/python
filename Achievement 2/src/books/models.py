from django.db import models
from django.shortcuts import reverse

genre_choices = (
    ('classic', 'Classic'),
    ('romantic', 'Romantic'),
    ('comic', 'Comic'),
    ('fantasy', 'Fantasy'),
    ('horror', 'Horror'),
    ('educational', 'Educational')
)

book_type_choices = (
    ('hardcover', 'Hard cover'),
    ('ebook', 'E-Book'),
    ('audiob', 'Audiobook')
)


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 120, default = 'No name...')
    price = (models.FloatField(help_text = 'in US dollars $', default = 0))
    genre = models.CharField(
        max_length = 12,
        choices = genre_choices,
        default = 'classic'
    )
    book_type = (
        models.CharField(
            max_length = 12,
            choices = book_type_choices,
            default = 'hardcopy'
        )
    )
    author_name = models.CharField(max_length = 120, null = True)
    pic = models.ImageField(upload_to = 'books', default = 'no_picture.jpg')

    def get_absolute_url(self):
       return reverse ('books:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.name)