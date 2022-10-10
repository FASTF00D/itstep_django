from django.db import models
from movies.models import Movie


class Actor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_born = models.DateField()
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.first_name + self.last_name