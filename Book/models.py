from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from Account.models import User


class Book(models.Model):
    title = models.CharField(max_length=254, verbose_name="book name")
    author = models.CharField(max_length=254, verbose_name="author name")
    
    class Meta:
        unique_together = ('title', 'author',)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating  = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('user', 'book',)

class Genre(models.Model):
    name =  models.CharField(max_length=254, verbose_name="genre name")

class GenreBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)