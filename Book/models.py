from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    title = models.CharField(max_length=254, verbose_name="book name")
    author = models.CharField(max_length=254, verbose_name="author name")
    
    class Meta:
        unique_together = ('title', 'author',)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name =  models.CharField(max_length=128, verbose_name="genre name")

    def __str__(self):
        return self.name

class GenreBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book', 'genre',)