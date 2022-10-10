from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateField(null=True)
    photo = models.FileField(null=True, blank=True)
    description = models.TextField()
    rating = models.FloatField(default=0, validators=[
        MinValueValidator(0.0, message='Min value shuld be less then 0'),
        MaxValueValidator(10.0, message='Max value should be not higher then 10')
    ])
    genres = models.ManyToManyField(
        Genre
    )

    def __str__(self):
        return self.title
