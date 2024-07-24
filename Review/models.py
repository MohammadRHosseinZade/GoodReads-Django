from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from Account.models import User
from Book.models import Book


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating  = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('user', 'book',)

