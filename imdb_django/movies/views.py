from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import MovieForm
from .models import Movie
from category.models import Category
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

# Create your views here.
def movie(request):
    movies = Movie.objects.all()
    cates = Category.objects.all()
    context = {
        'movies': movies,
        'categories': cates,
    }
    return render(request, 'movies/index.html', context)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid() and form.check_name():
            movie = form.save(commit=False)
            if movie.logo == "" or movie.logo == 'None':
                movie.logo = "http://3i5l7a3z22cj3ekuoz27ji2k.wpengine.netdna-cdn.com/wp-content/uploads/2018/12/Aquaman.jpg"
            if movie.trailer == "" or movie.trailer == 'None':
                movie.trailer = "https://www.youtube.com/watch?v=y66QKqto3qE"
            movie.save()
            form.save_m2m()
            return redirect('movie')
    else:
        form = MovieForm()
    return render(request, 'movies/form.html', {'form': form})

def edit_movie(request, movie_id=None):
    item = get_object_or_404(Movie, id=movie_id)
    form = MovieForm(request.POST or None, instance=item)
    if form.is_valid():
        movie = form.save(commit=False)
        if movie.logo == "" or movie.logo == 'None':
            movie.logo = "http://3i5l7a3z22cj3ekuoz27ji2k.wpengine.netdna-cdn.com/wp-content/uploads/2018/12/Aquaman.jpg"
        if movie.trailer == "" or movie.trailer == 'None':
            movie.trailer = "https://www.youtube.com/watch?v=y66QKqto3qE"
        movie.save()
        form.save_m2m()
        return redirect('movie')
    return render(request, 'movies/form.html', {'form': form})

def delete_movie(request, movie_id=None):
    Movie.objects.get(id=movie_id).delete()
    return redirect('movie')
