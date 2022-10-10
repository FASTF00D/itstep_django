from django.shortcuts import render
from movies.models import Movie
from movies.forms import MovieForm

def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies_list.html', {'movies': movies})


def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'movie_detail.html', {'movie': movie})


def movie_create(request):
    form = MovieForm()
    return render(request, 'movie_create.html', {'form': form})